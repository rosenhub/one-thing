# OneThingBench rubric

Each response is scored on six binary criteria. Score = number of criteria passed, 0–6.
The criteria are the skill's own pre-send self-check, so the benchmark measures whether the agent did what the skill asked.

| # | Criterion | Pass if | Fail if |
|---|---|---|---|
| C1 | **One action** | The response contains exactly one thing to do. If the user explicitly asked for the whole plan, pass if the plan has 5 steps or fewer, no sub-steps, and ends by pointing the user at step 1 only. | Two or more actions in one-at-a-time mode; or a requested plan with more than 5 steps, sub-steps, or no return to one. |
| C2 | **Under 5 minutes** | The action (or, in a requested plan, step 1) can be started now and finished in under 5 minutes by a person who is stuck. | The action is a phase ("gather your documents," "research options," "clean the kitchen"). |
| C3 | **Verb + object** | The action starts with a verb and names a specific object: "Open the email from Dr. Patel." | A noun phrase, a topic, a vague verb ("handle," "deal with," "work on"), or no named object. |
| C4 | **Physical** | Someone watching could see the action happen. Hands move, a thing changes. | "Think about," "decide," "figure out," "consider," "get in the right mindset." |
| C5 | **Nothing ahead, no choice** | The user is not shown what comes after, not told how many steps remain, and not asked to pick between steps. | "Step 1 of 9," "First... then...," "Would you rather start with X or Y," "You could either..." |
| C6 | **No cheer, no comment on the user** | No motivational language, no praise, no reassurance, no statements about the user's ability, feelings, or how normal their situation is, no filler. | "You've got this," "The hardest part is starting," "Great job," "It's totally normal," "Don't worry," "Great question." |

## The full-plan case

Prompts in the `asked-for-full-plan` category explicitly ask for the whole plan. The skill says: give it, 5 steps or fewer, then go back to one. C1 handles this: a 5-step plan passes C1; a one-step reply to an explicit plan request also passes C1 (it is one action), but the lint reports `plan_mode` so you can see which the agent chose. C5 still applies to the plan's framing: "Start with 1" passes; "Step 1 of 5, then step 2..." narration outside the list fails.

## Secondary metrics (reported, not scored)

- **Word count.** Shorter is usually better here, but it is reported so people can check the skill isn't just truncating.
- **Steps.** The highest numbered list item in the response. 1 in one-at-a-time mode; up to 5 in plan mode.
- **Exclamations.** Count of `!`. The skill says zero.

## Judge

`run.py` uses an LLM judge with the prompt in `judge_prompt.md`. The judge sees the user prompt, the response, and this rubric. It returns JSON with a 0/1 per criterion and a one-line reason for each failure.

Judge bias is real. To reduce it:
- The judge never sees whether the skill was on.
- Both conditions are judged by the same model in the same session.
- `lint.py` gives a deterministic floor for C1, C5 and C6 that needs no judge.

## Reporting

Report **mean score per condition**, **per-category breakdown**, and **the delta**. Post the model, date, and judge model. Results go in `results/`.

Do not report a single headline number without the per-category table next to it.
