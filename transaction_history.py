USER_FILE = 'users.txt'

from datetime import datetime

# To store transactions as a list of dictionaries
transactions = []

# Sample for adding deposit, withdrawal, and expense transactions to the history
def add_transaction(transaction_type, amount, category=None):
    transaction = {
        'type': transaction_type,
        'amount': amount,
        'date': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'category': category
    }
    transactions.append(transaction)

# Function to display the transaction history
def view_transaction_history():
    if not transactions:
        print("No transactions found.")
        return
    
    print("\n---- Transaction History ----")
    for transaction in transactions:
        print(f"{transaction['date']} - {transaction['type']} - ₱{transaction['amount']:.2f} - Category: {transaction['category'] if transaction['category'] else 'N/A'}")
    print("-----------------------------")

# Example function for printing a receipt
def print_receipt(transaction_type, amount, balance, category=None):
    print("\n------ Receipt ------")
    print(f"Transaction Type: {transaction_type}")
    print(f"Amount: ₱{amount:.2f}")
    print(f"Current Balance: ₱{balance:.2f}")
    if category:
        print(f"Category: {category}")
    print("--------------------")
