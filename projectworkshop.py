print("By Aayus Prasai")
import json
import os

# Global variables to store user and bus information
users = {}
buses = {
    "Na 1 Kha 432": {"Service Type": "Day Service", "From": "Kathmandu", "To": "Biratnagar", "Price": 1520, "Operation": True},
    "Na 1 Kha 434": {"Service Type": "Night Service", "From": "Kathmandu", "To": "Biratnagar", "Price": 1520, "Operation": True},
    "Na 1 Kha 489": {"Service Type": "Day Service", "From": "Kathmandu", "To": "Damak", "Price": 2000, "Operation": True},
    "Na 1 Kha 586": {"Service Type": "Day Service", "From": "Kathmandu", "To": "Biratnagar", "Price": 2000, "Operation": True},
}

# Load users from a file if it exists
def load_users():
    global users
    if os.path.exists("users.json"):
        with open("users.json", "r") as f:
            users = json.load(f)

# Save users to a file
def save_users():
    with open("users.json", "w") as f:
        json.dump(users, f)

# Registration function
def register():
    username = input("Enter username: ")
    if username in users:
        print("Username already exists. Try again.")
        return
    password = input("Enter password: ")
    users[username] = password
    save_users()
    print("Registration successful!")

# Login function
def login():
    while True:
        username = input("Enter username: ")
        password = input("Enter password: ")
        if username in users and users[username] == password:
            print("Login successful!")
            return True
        else:
            print("Invalid username or password. Try again.")

# Display available routes
def display_routes():
    print("Available routes:")
    for bus, details in buses.items():
        if details["Operation"]:
            print(f"{bus} - {details['From']} to {details['To']} - Rs. {details['Price']} - {details['Service Type']}")

# Purchase ticket function
def purchase_ticket():
    display_routes()
    bus_number = input("Enter the bus number you want to book: ")
    if bus_number in buses and buses[bus_number]["Operation"]:
        print(f"Booking ticket for {buses[bus_number]['From']} to {buses[bus_number]['To']} on {bus_number}")
        name = input("Enter your name: ")
        num_tickets = int(input("Enter number of tickets: "))
        total_price = num_tickets * buses[bus_number]["Price"]
        print(f"Total price: Rs. {total_price}")
        generate_bill(name, bus_number, num_tickets, total_price)
    else:
        print("Invalid bus number or the bus is not in operation.")

# Generate bill and save to text file
def generate_bill(name, bus_number, num_tickets, total_price):
    bill_content = f"Name: {name}\nBus Number: {bus_number}\nNumber of Tickets: {num_tickets}\nTotal Price: Rs. {total_price}\n"
    with open(f"bill_{name}.txt", "w") as f:
        f.write(bill_content)
    print("Bill generated and saved to file.")

# Main loop
def main():
    load_users()
    while True:
        print("\n1. Register\n2. Login\n3. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            register()
        elif choice == "2":
            if login():
                while True:
                    print("\n1. Purchase Ticket\n2. Logout")
                    user_choice = input("Enter your choice: ")
                    if user_choice == "1":
                        try:
                            purchase_ticket()
                        except Exception as e:
                            print(f"An error occurred: {e}")
                    elif user_choice == "2":
                        break
        elif choice == "3":
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
