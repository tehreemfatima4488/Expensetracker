
# Expense Tracker
# A simple program to add, view, and calculate expenses.


# List to store all expenses
expenses = []


# Function to add an expense
def add_expense():
    """Add a new expense to the expense list."""

    name = input("Enter expense name: ").strip()

    # Check if expense name is empty
    if not name:
        print("Expense name cannot be empty.")
        return

    # Get and validate the expense amount
    try:
        amount = float(input("Enter expense amount: "))

        if amount <= 0:
            print("Amount must be greater than 0.")
            return

    except ValueError:
        print("Please enter a valid number.")
        return

    # Create an expense dictionary
    expense = {
        "name": name,
        "amount": amount
    }

    # Add the expense to the list
    expenses.append(expense)

    print("Expense added successfully!")


# Function to display all expenses
def view_expenses():
    """Display all saved expenses."""

    if not expenses:
        print("\nNo expenses added yet.")
        return

    print("\n--- Your Expenses ---")

    for number, expense in enumerate(expenses, start=1):
        print(
            f"{number}. {expense['name']} - "
            f"Rs. {expense['amount']:.2f}"
        )


# Function to calculate and display total expenses
def show_total():
    """Calculate and display the total expenses."""

    if not expenses:
        print("\nNo expenses added yet.")
        return

    total = sum(expense["amount"] for expense in expenses)

    print(f"\nTotal Expenses: Rs. {total:.2f}")


# Function to display the menu
def show_menu():
    """Display the main menu."""

    print("\n===== EXPENSE TRACKER =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Show Total")
    print("4. Exit")


# Main function
def main():
    """Run the Expense Tracker program."""

    while True:
        show_menu()

        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            add_expense()

        elif choice == "2":
            view_expenses()

        elif choice == "3":
            show_total()

        elif choice == "4":
            print("\nThank you for using Expense Tracker!")
            break

        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")


# Start the program
if __name__ == "__main__":
    main()
