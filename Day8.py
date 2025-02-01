users = {}

def register_user(firstName, lastName, phoneNumber, userName, password):
    if userName in users:
        print("Username already exists. Please choose a different username.")
    else:
        users[userName] = {
            'firstName': firstName,
            'lastName': lastName,
            'phoneNumber': phoneNumber,
            'password': password
        }
        print(f"User {userName} registered successfully!")

def login_user(userName, password):
    if userName in users:
        if users[userName]['password'] == password:
            print(f"Welcome, {users[userName]['firstName']} {users[userName]['lastName']}!")
        else:
            print("Incorrect password. Please try again.")
    else:
        print("Username not found. Please register first.")
# Dictionary to store user details
users = {}

def register_user(firstName, lastName, phoneNumber, userName, password):
    if userName in users:
        print("Username already exists. Please choose a different username.")
    else:
        users[userName] = {
            'firstName': firstName,
            'lastName': lastName,
            'phoneNumber': phoneNumber,
            'password': password
        }
        print(f"User {userName} registered successfully!")

def login_user(userName, password):
    if userName in users:
        if users[userName]['password'] == password:
            print(f"Welcome, {users[userName]['firstName']} {users[userName]['lastName']}!")
        else:
            print("Incorrect password. Please try again.")
    else:
        print("Username not found. Please register first.")

def main():
    while True:
        # Register new user
        firstName = input("Enter first name: ")
        lastName = input("Enter last name: ")
        phoneNumber = input("Enter phone number: ")
        userName = input("Enter username: ")
        password = input("Enter password: ")
        
        register_user(firstName, lastName, phoneNumber, userName, password)
        
        # Ask if the user wants to register another account
        another = input("Do you want to register another account? (yes/no): ").strip().lower()
        if another != 'yes':
            break
    
    # Proceed to login
    while True:
        userName = input("Enter username to login: ")
        password = input("Enter password to login: ")
        
        login_user(userName, password)
        
        # Ask if the user wants to try logging in again
        try_again = input("Do you want to try logging in again? (yes/no): ").strip().lower()
        if try_again != 'yes':
            break

if __name__ == "__main__":
    main()
# Dictionary to store user details
users = {}

def register_user(firstName, lastName, phoneNumber, userName, password):
    if userName in users:
        print("Username already exists. Please choose a different username.")
    else:
        users[userName] = {
            'firstName': firstName,
            'lastName': lastName,
            'phoneNumber': phoneNumber,
            'password': password
        }
        print(f"User {userName} registered successfully!")

def login_user(userName, password):
    if userName in users:
        if users[userName]['password'] == password:
            print(f"Welcome, {users[userName]['firstName']} {users[userName]['lastName']}!")
        else:
            print("Incorrect password. Please try again.")
    else:
        print("Username not found. Please register first.")

def modify_username(oldUserName, newUserName):
    if oldUserName in users:
        if newUserName in users:
            print("The new username already exists. Please choose a different username.")
        else:
            users[newUserName] = users.pop(oldUserName)
            print(f"Username changed from {oldUserName} to {newUserName} successfully!")
    else:
        print("Old username not found. Please check the username and try again.")

def main():
    while True:
        print("\nSelect an option:")
        print("1. Register")
        print("2. Login")
        print("3. Modify Username")
        print("4. Exit")
        
        choice = input("Enter your choice: ").strip()
        
        if choice == '1':
            firstName = input("Enter first name: ")
            lastName = input("Enter last name: ")
            phoneNumber = input("Enter phone number: ")
            userName = input("Enter username: ")
            password = input("Enter password: ")
            register_user(firstName, lastName, phoneNumber, userName, password)
        
        elif choice == '2':
            userName = input("Enter username to login: ")
            password = input("Enter password to login: ")
            login_user(userName, password)
        
        elif choice == '3':
            oldUserName = input("Enter your current username: ")
            newUserName = input("Enter your new username: ")
            modify_username(oldUserName, newUserName)
        
        elif choice == '4':
            print("Exiting the program. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()

