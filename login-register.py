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
                return
    print("Invalid username or password.")

def main():
    while True:
        choice = input("\n1. Register\n2. Login\n3. Exit\nEnter choice: ")
        if choice == '1':
            register()
        elif choice == '2':
            login()
        elif choice == '3':
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
