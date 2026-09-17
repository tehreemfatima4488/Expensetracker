
expenses = []

while True:
    print("\n--- Expense Tracker ---")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Show Total")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter expense name: ")
        amount = float(input("Enter expense amount: "))

        expense = {
            "name": name,
            "amount": amount
        }

        expenses.append(expense)

        print("Expense added successfully!")

    elif choice == "2":
        if len(expenses) == 0:
            print("No expenses added yet.")
        else:
            print("\n--- Your Expenses ---")

            for expense in expenses:
                print(expense["name"], ":", expense["amount"])

    elif choice == "3":
        total = 0

        for expense in expenses:
            total = total + expense["amount"]

        print("Total Expenses:", total)

    elif choice == "4":
        print("Thank you for using Expense Tracker!")
        break

    else:
        print("Invalid choice. Please try again.")