"""Text interface layer. This is the only file that uses input() and print().

Run:  python app.py              (data lives in RAM)
      python app.py --store json (data survives a restart)
"""
import argparse

from dataman.logic import (MemoryBank, PracticeSession, Problem, SetFull,
                           curator_report)
from dataman.store import JsonFileStore, MemoryStore

# --- 1. The problem catalog ---------------------------------------------
PROBLEMS = [
    Problem("P1", "7 x 8", 56),
    Problem("P2", "3 + 4", 7),
    Problem("P3", "12 - 5", 7),
    Problem("P4", "9 / 3", 3),
    Problem("P5", "5 x 5", 25),
    Problem("P6", "10 - 2", 8),
    Problem("P7", "6 + 6", 12),
    Problem("P8", "15 / 3", 5),
    Problem("P9", "4 x 4", 16),
    Problem("P10", "8 - 3", 5),
    Problem("P11", "2 + 2", 4),
    Problem("P12", "9 x 9", 81),
    Problem("P13", "7 - 1", 6),
    Problem("P14", "5 / 1", 5),
]
PROBLEM_BY_ID = {p.id: p for p in PROBLEMS}
SESSION = "maya-12"


# --- 2. Helper used by the screens --------------------------------------
def choose_problem():
    pid = input(f"Problem id (P1-P{len(PROBLEMS)}) > ").strip().upper()
    problem = PROBLEM_BY_ID.get(pid)
    if problem is None:
        print("Unknown problem id.")
    return problem


# --- 3. The three screens -----------------------------------------------
def practice(store):
    problem = choose_problem()
    if problem is None:
        return
    session = PracticeSession(store, SESSION, problem)
    if session.is_finished():
        print("This session is finished. Choose 'report'.")
        return
    while not session.is_finished():
        raw = input(f"Try {session.next_try()}: {problem.prompt} = ")
        if not raw.strip().lstrip("-").isdigit():
            print("Enter a whole number.")
            continue
        out = session.submit(int(raw))
        if out.status == "correct":
            print("Correct.")
        elif out.status == "retry":
            print("TRY AGAIN!")
        else:
            print(f"The answer is {out.revealed_answer}.")


def report(store):
    problem = choose_problem()
    if problem is None:
        return
    rep = curator_report(store, SESSION, problem.id)
    print(f"Curator report for {SESSION}: {rep['label']}")
    for r in rep["attempts"]:
        print(f"  try {r['try']}: answered {r['answer']} -> "
              f"{'correct' if r['correct'] else 'wrong'}")


def bank(store):
    memory_bank = MemoryBank(store, "set-1")
    pid = input("Problem id to add (for example P11): ").strip().upper()
    if pid not in PROBLEM_BY_ID:
        print("Unknown problem id.")
        return
    try:
        memory_bank.add_problem(pid)
        print(f"Added. Set holds {len(memory_bank.members())}.")
    except SetFull as err:
        print(f"Refused: {err}")


# --- 4. The menu loop and entry point -----------------------------------
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--store", choices=["memory", "json"], default="memory")
    args = parser.parse_args()
    store = JsonFileStore() if args.store == "json" else MemoryStore()
    actions = {"practice": practice, "report": report, "bank": bank}
    while True:
        choice = input("practice / report / bank / quit > ").strip().lower()
        if choice == "quit":
            break
        if choice in actions:
            actions[choice](store)


if __name__ == "__main__":
    main()