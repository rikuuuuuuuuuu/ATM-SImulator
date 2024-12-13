# budget tracker natin par
budgetcategories = []
budgetlimits = []
expenses = []

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
    # checks if may budget na naset
    if not budgetcategories:
        print("Please set a budget first!")
        return
    
    # dinidisplay yung gagawin (set budget and add exit tas exit)
    print("\nAvailable Budget Categories:")
    for i, category in enumerate(budgetcategories):
        print(f"{i + 1}. {category}")
    
    # selecting category
    category_index = int(input("Select category number: ")) - 1
    category = budgetcategories[category_index]
    
    # inputing expense
    expense_amount = float(input(f"Enter expense amount for {category}: "))
    
    # storing expense
    expenses.append({
        'category': category,
        'amount': expense_amount
    })

# start ng program

while True:
    print("\n1. Set Budget")
    print("2. Add Expense")
    print("3. Exit")
    
    choice = input("Enter number of your choice: ")
    
    if choice == '1':
        set_budget()
    elif choice == '2':
        add_expense()
    elif choice == '3':
        print("Thank you for using ATM Simulator!")
        break
    else:
        print("invalid number. please try again.")
