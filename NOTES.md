# NOTES: Three Layers



Fill each TODO. Write plain, short sentences. Do not delete the headings.

## Part 1. Predict, then find [S1]

Write your prediction before you open any code. Then search. In the last column, write each file the search finds and what that file does.

| Action | Search word | My prediction (file) | Files found and what each does |
|---|---|---|---|
| Prints "Not yet. Try again." | `Not yet` | app.py | app.py |
| Decides that the second miss shows the answer | `reveal` | logic.py | logic.py |
| Saves one attempt | `save_attempt` | | store.py|
| Refuses the 11th problem | `SetFull` | logic.py | logic.py |

Search command: `grep -rn "SEARCH WORD" --include=*.py .`

## Part 2. What the program remembered [S1]

After the restart, what did the program remember? store.py

Which file made that possible? Jsonfile

## Part 3. The interface change [S1]

What did you change in `app.py`? Message

Why did no test need to change? No change

## Part 4. The rule in the real library [S2]

The same 10-problem rule exists in the real library. Write the file and the function name. File: dataman/logic.py. Function: MemoryBank.add_problem.

## Part 5. The red test [S2]

With the rule removed from the library, what did the screen show? Error

With the rule removed, which test failed? TODO

## Part 6. The data swap [S2]

A real database would replace which file? TODO

Which file holds the rules and does not change when the database changes? TODO

## Reflection [S2]

Write 3 to 5 sentences. Pick one layer. Say what you changed in it. Say what stayed the same in the other two layers. TODO

## Beta feedback (optional) (55)

This bonus is a beta test. Which step took longer than its time? What confused you? Write it here. Your answer helps the next class.

