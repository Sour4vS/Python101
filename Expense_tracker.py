def load_expenses():
    expenses = []
    try:
        file = open("expenses.txt", "r")
        for line in file:
            expenses.append(int(line.strip()))
        file.close()
    except FileNotFoundError:
        pass
    return expenses
expenses = load_expenses()

def save_expenses(expenses):
    file = open("expenses.txt", "w")
    for num in expenses:
        file.write(str(num) + "\n")
    file.close()

def add_expense(expenses):
     amount = int(input("Enter expense amount: "))
     expenses.append(amount)
     save_expenses(expenses)
     print("Expense added.")

def view_expenses(expenses):
    if not expenses:
        print("No expenses recorded.")
    else:
        count = 1
        total = 0
        for num in expenses:
            print(f"Expense {count}: {num}")
            total += num
            count += 1
        print(f"Total: {total}")

while True:
    print('''
==== Expense Tracker ====
1. Add Expense
2. View Expenses
3. Exit
''')

    try:
        choice = int(input("Select option: "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    if choice == 1:
        add_expense(expenses)

    elif choice == 2:
        view_expenses(expenses)

    elif choice == 3:
        print("Exiting...")
        break

    else:
        print("Invalid option.")
