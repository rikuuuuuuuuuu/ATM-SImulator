import datetime

class ATM:
    def __init__(self):
        # Initialize an empty list to store transaction history
        self.transaction_history = []

    def record_transaction(self, transaction_type, amount, balance):
        """
        Record a transaction in the transaction history.

        Args:
            transaction_type (str): Type of the transaction (e.g., 'Deposit', 'Withdrawal').
            amount (float): Amount involved in the transaction.
            balance (float): Balance after the transaction.
        """
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        transaction = {
            "timestamp": timestamp,
            "type": transaction_type,
            "amount": amount,
            "balance": balance
        }
        self.transaction_history.append(transaction)

    def display_transaction_history(self):
        """
        Display the transaction history in a readable format.
        """
        print("\nTransaction History:")
        if not self.transaction_history:
            print("No transactions available.")
            return

        for i, transaction in enumerate(self.transaction_history, start=1):
            print(f"{i}. [{transaction['timestamp']}] {transaction['type']}: {transaction['amount']:.2f} | Balance: {transaction['balance']:.2f}")

    def print_receipt(self):
        """
        Print the receipt for the most recent transaction.
        """
        if not self.transaction_history:
            print("No transactions available for receipt printing.")
            return

        last_transaction = self.transaction_history[-1]
        print("\nReceipt:")
        print("--------------------------------")
        print(f"Date: {last_transaction['timestamp']}")
        print(f"Transaction Type: {last_transaction['type']}")
        print(f"Amount: {last_transaction['amount']:.2f}")
        print(f"Remaining Balance: {last_transaction['balance']:.2f}")
        print("--------------------------------")

# Example Usage
atm = ATM()

# Simulate some transactions
atm.record_transaction("Deposit", 500.00, 1500.00)
atm.record_transaction("Withdrawal", 200.00, 1300.00)

# Display transaction history
atm.display_transaction_history()

# Print receipt for the last transaction
atm.print_receipt()
