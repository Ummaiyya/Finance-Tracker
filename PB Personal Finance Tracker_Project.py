import csv
import os
import matplotlib.pyplot as plt
from datetime import datetime

FILE_NAME = "finance_data.csv"

# INITIALIZE FILE
def initialize_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["type", "category", "amount", "date"])


# ADD INCOME
def add_income():
    category = input("Enter income category: ")

    try:
        amount = float(input("Enter amount: "))
        if amount <= 0:
            print("Amount must be greater than 0!")
            return

        date = datetime.now().strftime("%Y-%m-%d")

        with open(FILE_NAME, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["income", category, amount, date])

        print("Income added successfully!")

    except ValueError:
        print("Invalid amount!")


# ADD EXPENSE
def add_expense():
    category = input("Enter expense category: ")

    try:
        amount = float(input("Enter amount: "))
        if amount <= 0:
            print("Amount must be greater than 0!")
            return

        date = datetime.now().strftime("%Y-%m-%d")

        with open(FILE_NAME, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["expense", category, amount, date])

        print("Expense added successfully!")

    except ValueError:
        print("Invalid amount!")


# LOAD DATA
def load_data():
    income = 0
    expense = 0

    if not os.path.exists(FILE_NAME):
        return 0, 0

    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)
        next(reader, None)

        for row in reader:
            if len(row) != 4:
                continue

            t_type = row[0].lower()

            try:
                amount = float(row[2])
            except ValueError:
                continue

            if t_type == "income":
                income += amount
            elif t_type == "expense":
                expense += amount

    return income, expense

#Monthly summary
def monthly_summary():
    monthly_data = {}

    try:
        with open("finance_data.csv", "r") as file:
            reader = csv.reader(file)
            next(reader, None)

            for row in reader:
                if len(row) != 4:
                    continue

                t_type = row[0].lower()
                amount = float(row[2])
                month = row[3][:7]  # YYYY-MM

                if month not in monthly_data:
                    monthly_data[month] = {"income": 0, "expense": 0}

                if t_type == "income":
                    monthly_data[month]["income"] += amount
                elif t_type == "expense":
                    monthly_data[month]["expense"] += amount

        print("\n===== MONTHLY SUMMARY =====")

        for m, data in monthly_data.items():
            balance = data["income"] - data["expense"]

            print(f"\nMonth: {m}")
            print(f"Income : {data['income']}")
            print(f"Expense: {data['expense']}")
            print(f"Balance: {balance}")

    except FileNotFoundError:
        print("No data found.")

# SHOW BREAKDOWN
def show_breakdown():
    income = 0
    expense = 0

    income_categories = {}
    expense_categories = {}

    try:
        with open("finance_data.csv", "r") as file:
            reader = csv.reader(file)
            next(reader, None)

            for row in reader:
                if len(row) != 4:
                    continue

                t_type = row[0].lower()
                category = row[1]
                amount = float(row[2])

                if t_type == "income":
                    income += amount
                    income_categories[category] = income_categories.get(category, 0) + amount

                elif t_type == "expense":
                    expense += amount
                    expense_categories[category] = expense_categories.get(category, 0) + amount

        balance = income - expense

        print("\n===== FINANCIAL BREAKDOWN =====")

        print("\n==== TOTALS ====")
        print(f"Total Income : {income}")
        print(f"Total Expense: {expense}")
        print(f"Balance      : {balance}")

        print("\n==== INCOME BY CATEGORY ====")
        for c, amt in income_categories.items():
            print(f"{c}: {amt}")

        print("\n==== EXPENSE BY CATEGORY ====")
        for c, amt in expense_categories.items():
            print(f"{c}: {amt}")

    except FileNotFoundError:
        print("No data found.")
    if expense > income:
     print("⚠ Warning: Expenses exceed income!")
   
# GRAPH
def show_graph():
    income, expense = load_data()

    if income == 0 and expense == 0:
        print("No data to display.")
        return

    labels = ["Income", "Expense"]
    values = [income, expense]

    plt.bar(labels, values)
    plt.title("Income vs Expense")
    plt.ylabel("Amount")
    plt.show()

# MENU
def menu():
    initialize_file()

    while True:
        print("\n===== PERSONAL FINANCE TRACKER =====")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. Show Breakdown")
        print("4. Show Graph")
        print("5. Mothly Summary")
        print("6. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            add_income()
        elif choice == "2":
            add_expense()
        elif choice == "3":
            show_breakdown()
        elif choice == "4":
            show_graph()
        elif choice == "5":
            monthly_summary()
        elif choice == "6":
             break
        else:
            print("Invalid choice!")

# RUN PROGRAM
menu()