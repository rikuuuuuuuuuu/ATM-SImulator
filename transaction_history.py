# Existing Data
budgetcategories = []
budgetlimits = []
expenses = []
transactions = []  # This will store the transaction history

USER_FILE = 'users.txt'

def register():
    username = input("Enter username: ")
    password = input("Enter password: ")
    with open(USER_FILE, 'a') as f:
        f.write(f"{username},{password}\n")
    print("Registration successful!")

def login():
    username = input("Enter username: ")
    password = input("Enter password: ")
    with open(USER_FILE, 'r') as f:
        for line in f:
            stored_username, stored_password = line.strip().split(',')
            if stored_username == username and stored_password == password:
                print("Login successful!")
                return True
    print("Invalid username or password.")
    return False

def set_budget():
    category = input("Enter budget category: ")
    
    while True:
        try:
            limit = float(input(f"Enter budget limit for {category}: "))
            budgetcategories.append(category)
            budgetlimits.append(limit)
            break
        except ValueError:
            print("Please enter a valid number for the budget limit.")

def add_expense():
    # Check if a budget is set
    if not budgetcategories:
        print("Please set a budget first!")
        return
    
    print("\nAvailable Budget Categories:")
    for i, category in enumerate(budgetcategories):
        print(f"{i + 1}. {category}")
    
    # Select category
    category_index = int(input("Select category number: ")) - 1
    category = budgetcategories[category_index]
    
    # Input expense amount
    expense_amount = float(input(f"Enter expense amount for {category}: "))
    
    # Store the expense
    expenses.append({
        'category': category,
        'amount': expense_amount
    })
    
    # Add the transaction to history
    transaction = {
        'type': 'Expense',
        'category': category,
        'amount': expense_amount
    }
    transactions.append(transaction)
    print(f"₱{expense_amount:.2f} has been added to {category}.")

def add_transaction(transaction_type, category, amount):
    transaction = {
        'type': transaction_type,
        'category': category,
        'amount': amount
    }
    transactions.append(transaction)

def print_receipt(transaction):
    print("\n------ ATM Receipt ------")
    print(f"Transaction Type: {transaction['type']}")
    print(f"Category: {transaction['category']}")
    print(f"Amount: ₱{transaction['amount']:.2f}")
    print("-------------------------")
    print("Thank you for using our ATM!")

def print_transaction_history():
    if not transactions:
        print("No transactions to display.")
        return
    
    print("\n------ Transaction History ------")
    for i, transaction in enumerate(transactions, start=1):
        print(f"Transaction {i}: {transaction['type']} - Category: {transaction['category']} - ₱{transaction['amount']:.2f}")
    print("---------------------------------")

# Main program
def main():
    if not login():
        return
    
    while True:
        print("\n1. Set Budget")
        print("2. Add Expense")
        print("3. Print Transaction History")
        print("4. Print Receipt")
        print("5. Exit")
        
        choice = input("Enter number of your choice: ")
        
        if choice == '1':
            set_budget()
        elif choice == '2':
            add_expense()
        elif choice == '3':
            print_transaction_history()
        elif choice == '4':
            if transactions:
                print_receipt(transactions[-1])  # Print the latest transaction
            else:
                print("No transaction to print receipt for.")
        elif choice == '5':
            print("Thank you for using the ATM Simulator!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()


# Print receipt for the last transaction
atm.print_receipt()
