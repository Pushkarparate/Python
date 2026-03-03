def display_balance(balance):
    print("Current Balance =", balance)

def deposit(balance, amount):
    balance = balance + amount
    return balance

def withdraw(balance, amount):
    balance = balance - amount
    return balance


balance = 0   # initial balance

while True:
    print("\n--- BANK MENU ---")
    print("1. Display Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        display_balance(balance)

    elif choice == 2:
        amt = int(input("Enter deposit amount: "))
        balance = deposit(balance, amt)

    elif choice == 3:
        amt = int(input("Enter withdraw amount: "))
        balance = withdraw(balance, amt)

    elif choice == 4:
        print("Thank you!")
        break

    else:
        print("Invalid choice")
