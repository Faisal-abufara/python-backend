import json
import os
from datetime import datetime

DATA_FILE = 'logs.json'

def load_transactions():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    return []

def save_transactions(transactions):
    with open(DATA_FILE, 'w') as f:
        json.dump(transactions, f, indent=4)

def add_transaction(transactions):
    try:
        amount = float(input("Enter amount (positive for income, negative for expense): "))
    except ValueError:
        print("Invalid amount! Please enter a numeric value.")
        return

    category = input("Enter category (e.g., Salary, Groceries, Rent): ").strip()
    if not category:
        print("Category cannot be empty.")
        return

    date_str = input("Enter date (YYYY-MM-DD) or leave blank for today: ").strip()
    if not date_str:
        date_str = datetime.today().strftime('%Y-%m-%d')
    else:
        try:
            datetime.strptime(date_str, '%Y-%m-%d')
        except ValueError:
            print("Invalid date format! Use YYYY-MM-DD.")
            return

    transaction = {
        'amount': amount,
        'category': category,
        'date': date_str
    }
    transactions.append(transaction)
    save_transactions(transactions)
    print("Transaction added successfully!")

def view_transactions(transactions):
    if not transactions:
        print("No transactions recorded.")
        return

    print(f"\n{'Date':<12} {'Category':<15} {'Amount':>10}")
    print("-" * 40)
    for t in transactions:
        date = t['date']
        category = t['category']
        amount = t['amount']
        print(f"{date:<12} {category:<15} {amount:>10.2f}")
    print()

def financial_summary(transactions):
    total_income = sum(t['amount'] for t in transactions if t['amount'] > 0)
    total_expenses = sum(t['amount'] for t in transactions if t['amount'] < 0)
    net_balance = total_income + total_expenses

    print("\nFinancial Summary:")
    print(f"Total Income:   ${total_income:.2f}")
    print(f"Total Expenses: ${abs(total_expenses):.2f}")
    print(f"Net Balance:    ${net_balance:.2f}\n")

def main():
    transactions = load_transactions()

    while True:
        print("----- Personal Finance Tracker -----")
        print("1. Add Transaction")
        print("2. View Transactions")
        print("3. Financial Summary")
        print("4. Exit")
        choice = input("Choose an option: ").strip()

        if choice == '1':
            add_transaction(transactions)
        elif choice == '2':
            view_transactions(transactions)
        elif choice == '3':
            financial_summary(transactions)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please choose 1-4.")

if __name__ == "__main__":
    main()