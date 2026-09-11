"""
Expense Tracker Program
------------------------
Why it matters: This teaches the "accumulator" pattern — repeatedly
updating one variable by adding new values to it. This is the same
logic behind backend calculations like running totals, invoice sums,
and account balances.

Key Skill: Math operations & Accumulators (total = total + new_expense).
"""

def get_expense():
    """Ask the user for one expense amount and return it as a float."""
    while True:
        entry = input("Enter an expense amount (or 'done' to finish): ").strip()

        if entry.lower() == "done":
            return None

        try:
            amount = float(entry)
            if amount < 0:
                print("Expense cannot be negative. Try again.")
                continue
            return amount
        except ValueError:
            print("Please enter a valid number (e.g., 100, 50, 20).")


def main():
    total = 0.0     # accumulator, starts at zero
    count = 0

    print("--- EXPENSE TRACKER ---")
    print("Enter your expenses one at a time. Type 'done' when finished.\n")

    while True:
        expense = get_expense()

        if expense is None:   # user typed "done"
            break

        total = total + expense   # <-- the accumulator step
        count += 1
        print(f"Added: {expense:.2f}  |  Running Total: {total:.2f}\n")

    print("\n--- SUMMARY ---")
    print(f"Number of expenses entered: {count}")
    print(f"Total Spent: {total:.2f}")


if __name__ == "__main__":
    main()
