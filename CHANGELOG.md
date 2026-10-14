# Changelog

## 1.0.0 — 2026-10-13

- Initial release: 12 rules, pre-send self-check, 16 hosts.
- Rule 9 handles the asked-for-the-whole-plan case: 5 steps max, then back to one.
- Rule 12 handles stalls: smaller step, not longer message.
- OneThingBench: 48 prompts, 8 categories, LLM judge + deterministic lint with a measured numbered-list check.
- `install.sh` with `--project` and `--dry-run`.
