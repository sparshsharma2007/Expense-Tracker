import csv
from datetime import datetime

FILE_NAME = "expenses.csv"


# Load expenses from file
def load_expenses():

    expenses = []

    try:
        with open(FILE_NAME, "r") as file:

            reader = csv.DictReader(file)

            for row in reader:
                expenses.append(row)

    except FileNotFoundError:
        pass

    return expenses


# Save expenses to file
def save_expense(expense):

    file_exists = False

    try:
        with open(FILE_NAME, "r"):
            file_exists = True

    except FileNotFoundError:
        pass

    with open(FILE_NAME, "a", newline="") as file:

        fieldnames = ["date", "category", "amount", "description"]

        writer = csv.DictWriter(file, fieldnames=fieldnames)

        if not file_exists:
            writer.writeheader()

        writer.writerow(expense)


# Add Expense
def add_expense():

    category = input("Enter Category (Food/Travel/etc): ")

    amount = input("Enter Amount: ")

    description = input("Enter Description: ")

    date = datetime.now().strftime("%Y-%m-%d")

    expense = {
        "date": date,
        "category": category,
        "amount": amount,
        "description": description
    }

    save_expense(expense)

    print("Expense Added Successfully!")


# View Expenses
def view_expenses(expenses):

    if not expenses:
        print("No expense records found")
        return

    print("\n===== Expense Records =====")

    for expense in expenses:

        print(
            expense["date"],
            "|",
            expense["category"],
            "| ₹" + expense["amount"],
            "|",
            expense["description"]
        )


# Calculate Total Expense
def total_expense(expenses):

    total = 0

    for expense in expenses:
        total += float(expense["amount"])

    print("\nTotal Expense: ₹", total)


# Filter by Category
def filter_category(expenses):

    category = input("Enter category to search: ")

    found = False

    for expense in expenses:

        if expense["category"].lower() == category.lower():

            print(
                expense["date"],
                "| ₹" + expense["amount"],
                "|",
                expense["description"]
            )

            found = True

    if not found:
        print("No records found")


# Main Menu
def main():

    while True:

        expenses = load_expenses()

        print("\n===== Expense Tracker =====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Total Expense")
        print("4. Filter by Category")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_expense()

        elif choice == "2":
            view_expenses(expenses)

        elif choice == "3":
            total_expense(expenses)

        elif choice == "4":
            filter_category(expenses)

        elif choice == "5":
            print("Thank You!")
            break

        else:
            print("Invalid Choice")


main()
