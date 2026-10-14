#!/usr/bin/env python3
"""
Deterministic one-thing lint. No API key needed.

Checks a response for the patterns the skill bans and that can be detected
without a judge: motivational language and comments on the person (C6),
plan framing and numbering ahead (C5), filler openers/closers (C6), and a
measured check: more than one numbered list item is a finding unless the
response's first line contains the word "plan" (rule 9, the asked-for-the-plan
case).

Usage:
    python lint.py response.md [more.md ...]
    python lint.py --json response.md
    cat response.md | python lint.py -

Exit code is the number of files with at least one finding (max 1 per file),
so it works as a CI gate.
"""
import json
import re
import sys

FILLER = [
    r"\bgreat question\b", r"\bgood question\b", r"\babsolutely!?\b", r"\bcertainly!?\b",
    r"\bi'?d be happy to\b", r"\bhappy to help\b", r"\bof course!\b",
    r"\bhope (this|that) helps\b", r"\blet me know if\b", r"\bfeel free to\b",
    r"\bdon'?t hesitate\b", r"\bthanks for (asking|reaching out)\b",
    r"\btotally understandable\b", r"\bdon'?t worry\b", r"\bno worries\b",
    r"\bgood news is\b", r"\bgreat job\b", r"\bnice work\b", r"\bwell done\b",
]

MOTIVATIONAL = [
    r"\byou'?ve got this\b", r"\byou can do (it|this)\b", r"\byou got this\b",
    r"\bi believe in you\b", r"\bthe hardest part is\b", r"\bsmall steps\b",
    r"\bprogress over perfection\b", r"\blet'?s do this\b", r"\byou'?ll feel\b",
    r"\byou'?re not alone\b", r"\bno shame\b", r"\bbe proud\b", r"\bproud of\b",
    r"\bone step at a time\b(?![^.]*\bget them\b)", r"\bit'?s (totally |completely )?normal to\b",
    r"\beveryone (struggles|gets like this|puts this off)\b", r"\bnobody'?s favorite\b",
    r"\byou deserve\b", r"\bbe kind to yourself\b", r"\bgive yourself (credit|grace)\b",
    r"\bmomentum\b", r"\bmanageable\b", r"\bless daunting\b", r"\bnot that bad\b",
]

PLAN_FRAMING = [
    r"\bhere'?s a plan\b", r"\bhere is a plan\b", r"\bhere'?s how i'?d\b",
    r"\blet'?s break (this|it) down\b", r"\bbreak (this|it) down into\b",
    r"\bbreak (this|it) (up )?into\b", r"\bmanageable (pieces|chunks|steps)\b",
    r"\bstep[- ]by[- ]step\b", r"\bgame plan\b", r"\broadmap\b",
    r"\byou'?ll want to\b", r"\bnext steps\b",
]

NUMBERING_AHEAD = [
    r"\bstep (1|one) of\b", r"\bstep [2-9]\b", r"\bstep (two|three|four|five|six)\b",
    r"\bfirst,?\b[^.\n]*\bthen\b", r"\bafter that,?\b", r"\bonce (that'?s|you'?ve|you have)\b[^.\n]*,",
    r"\bfinally,?\b", r"\blastly,?\b", r"\bthe (next|following) steps?\b",
    r"\b(more|remaining) steps?\b(?![^.]*\bone at a time\b)",
]

CHOICE = [
    r"\bwould you (rather|prefer|like to start with)\b", r"\byou could (either|start with)\b",
    r"\bwhichever (you|feels)\b", r"\bpick (one|whichever|a room)\b", r"\bup to you\b",
    r"\beither\b[^.\n]*\bor\b[^.\n]*\?",
]

CHECKS = [
    ("C6 filler", FILLER),
    ("C6 motivational", MOTIVATIONAL),
    ("C5 plan framing", PLAN_FRAMING),
    ("C5 numbering ahead", NUMBERING_AHEAD),
    ("C5 user must choose", CHOICE),
]

NUMBERED_ITEM = re.compile(r"^\s*(\d+)[.)]\s", re.M)


def lint(text: str) -> dict:
    findings = []
    low = text.lower()
    for label, patterns in CHECKS:
        for pat in patterns:
            for m in re.finditer(pat, low):
                findings.append({"check": label, "match": text[m.start():m.end()], "pos": m.start()})
    # Measured check: numbered list items beyond the first are a finding
    # unless the first line says "plan" (the user asked for the whole plan).
    first_line = low.strip().splitlines()[0] if low.strip() else ""
    plan_mode = bool(re.search(r"\bplan\b", first_line))
    items = [m for m in NUMBERED_ITEM.finditer(text) if int(m.group(1)) >= 2]
    if items and not plan_mode:
        m = items[0]
        findings.append({"check": "C1 more than one step", "match": text[m.start():m.end()].strip(),
                         "pos": m.start()})
    findings.sort(key=lambda f: f["pos"])
    words = len(text.split())
    steps = max([int(m.group(1)) for m in NUMBERED_ITEM.finditer(text)] or [1 if text.strip() else 0])
    exclamations = text.count("!")
    return {
        "words": words,
        "steps": steps,
        "exclamations": exclamations,
        "plan_mode": plan_mode,
        "findings": findings,
        "clean": not findings,
    }


def main(argv):
    as_json = "--json" in argv
    paths = [a for a in argv if not a.startswith("--")]
    if not paths:
        print(__doc__)
        return 2
    failed = 0
    out = {}
    for p in paths:
        text = sys.stdin.read() if p == "-" else open(p, encoding="utf-8").read()
        r = lint(text)
        out[p] = r
        if not r["clean"]:
            failed += 1
        if not as_json:
            status = "CLEAN" if r["clean"] else f"{len(r['findings'])} finding(s)"
            print(f"{p}: {status}  [{r['words']} words, {r['steps']} step(s), "
                  f"{r['exclamations']} exclamation(s)]")
            for f in r["findings"]:
                print(f"    {f['check']:<26} \"{f['match']}\"")
    if as_json:
        print(json.dumps(out, indent=2))
    return min(failed, 1)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
