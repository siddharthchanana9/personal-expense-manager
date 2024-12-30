expenses = []

while True:
    expense = float(input("Enter expense amount: "))
    category = input("Enter category: ")
    expenses.append({"amount": expense, "category": category})
    more = input("Add another expense? (yes/no): ").lower()
    if more != "yes":
        break

print("Expenses:", expenses)