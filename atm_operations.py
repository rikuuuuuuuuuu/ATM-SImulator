balance = 3000  

while True:
    print("\nHello! Welcome to the ATM!")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Print a Receipt")
    print("5. Exit")
    
    choice = int(input("Please select a number: "))
    
    if choice == 1:

        print(f"\nYour current balance is: ₱{balance:.2f}")
    
    elif choice == 2:

        deposit = float(input("Enter the amount to deposit: "))
        if deposit > 0:
            balance += deposit
            print(f"₱{deposit:.2f} has been deposited successfully.")
        else:
            print("Invalid amount. Please enter a positive number.")
    
    elif choice == 3:
        withdraw = float(input("Enter the amount to withdraw: "))
        if withdraw > balance:
            print("Insufficient balance. Please try a smaller amount.")
        elif withdraw <= 0:
            print("Invalid amount. Please enter a positive number.")
        else:
            balance -= withdraw
            print(f"₱{withdraw:.2f} has been withdrawn successfully.")
    
    elif choice == 4:
        print("\n------ ATM Receipt ------")
        print(f"Your account Balance is: ₱{balance:.2f}")
        print("-------------------------")
        print("Thank you for using our ATM!")
    
    elif choice == 5:
        print("\nThank you for using the ATM. Have a nice day!")
        break
    
    else:
        print("\nInvalid choice. Kindly choose the (action) number you desire to use from 1 to 5.")
