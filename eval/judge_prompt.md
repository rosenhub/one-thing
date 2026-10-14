You are grading one AI response against six binary criteria. You do not know what instructions the AI had. Grade only the text. The user is asking for help with a task.

USER PROMPT:
{prompt}

AI RESPONSE:
{response}

CRITERIA (1 = pass, 0 = fail):

C1 one_action — The response contains exactly one thing to do. Exception: if the user explicitly asked for the whole plan or all the steps, pass if the plan has 5 or fewer steps, no sub-steps, and ends by pointing the user at step 1 only. Fail on two or more actions otherwise, or a requested plan with more than 5 steps.
C2 under_5_minutes — The action (or step 1 of a requested plan) can be started now and finished in under 5 minutes by someone who is stuck. Fail if it is a phase ("gather your documents", "research options", "clean the kitchen").
C3 verb_object — The action starts with a verb and names a specific object ("Open the email from Dr. Patel"). Fail on a noun phrase, a topic, a vague verb ("handle", "deal with", "work on"), or no named object.
C4 physical — Someone watching could see the action happen. Fail on "think about", "decide", "figure out", "consider", "get in the right mindset".
C5 nothing_ahead_no_choice — The user is not shown what comes after, not told how many steps remain, and not asked to choose between steps. Fail on "step 1 of 9", "first... then...", "would you rather start with X or Y", "you could either".
C6 no_cheer — No motivational language, praise, reassurance, filler, or statements about the user's ability, feelings, or how normal their situation is. Fail on "you've got this", "the hardest part is starting", "great job", "it's totally normal", "don't worry", "great question".

Return ONLY this JSON, no prose:
{{"C1":0|1,"C2":0|1,"C3":0|1,"C4":0|1,"C5":0|1,"C6":0|1,"reasons":{{"C1":"...only if failed","C2":"...","C3":"...","C4":"...","C5":"...","C6":"..."}}}}
