expenses = []

while True:
    expense = float(input("Enter expense amount: "))
    category = input("Enter category: ")
    expenses.append({"amount": expense, "category": category})
    more = input("Add another expense? (yes/no): ").lower()
    if more != "yes":
        break

print("Expenses:", expenses)

import json

def save_expenses(expenses):
    with open("expenses.json", "w") as f:
        json.dump(expenses, f)

def load_expenses():
    try:
        with open("expenses.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

expenses = load_expenses()
while True:
    expense = float(input("Enter expense amount: "))
    category = input("Enter category: ")
    expenses.append({"amount": expense, "category": category})
    more = input("Add another expense? (yes/no): ").lower()
    if more != "yes":
        break

save_expenses(expenses)
print("Expenses saved!")
