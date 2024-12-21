# This constant likely represents the name of a file intended for storing user-related data, although it is not used in this snippet.
USER_FILE = 'users.txt'

from datetime import datetime

# To store transactions as a list of dictionaries
# This global variable stores a list of transaction dictionaries, serving as the in-memory transaction history.
transactions = []

#  Adding deposit, withdrawal, and expense transactions to the history
#  This function logs a new transaction by creating a dictionary with details like type, amount, date, and category, and appends it to the global transactions list.
def add_transaction(transaction_type, amount, category=None):
    transaction = {
        'type': transaction_type,
        'amount': amount,
        'date': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'category': category
    }
    transactions.append(transaction)

# Function to display the transaction history
# This function displays all transactions stored in the transactions list, showing details like date, type, amount, and category.
def view_transaction_history():
    if not transactions:
        print("No transactions found.")
        return
    
    print("\n---- Transaction History ----")
    for transaction in transactions:
        print(f"{transaction['date']} - {transaction['type']} - ₱{transaction['amount']:.2f} - Category: {transaction['category'] if transaction['category'] else 'N/A'}")
    print("-----------------------------")

# Function for printing a receipt
# This function prints a formatted receipt for a specific transaction, including details like transaction type, amount, current balance, and category.
def print_receipt(transaction_type, amount, balance, category=None):
    print("\n------ Receipt ------")
    print(f"Transaction Type: {transaction_type}")
    print(f"Amount: ₱{amount:.2f}")
    print(f"Current Balance: ₱{balance:.2f}")
    if category:
        print(f"Category: {category}")
    print("--------------------")
