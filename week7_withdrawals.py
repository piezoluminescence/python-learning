balance = 1000  # Starting balance
while True:
    print("\n==== Simple ATM ====")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Exit")
    choice = input("Enter your choice (1-3): ")

    if choice == "1":
        amount = float(input("Enter amount to deposit: "))
        if amount > 0:
            balance += amount
            print(f"Deposited ${amount:.2f}. New balance: ${balance:.2f}")
        else:
            print("Invalid deposit amount.")

    elif choice == "2":
        amount = float(input("Enter amount to withdraw: "))
        if amount > balance:
            print("Insufficient funds.")
        elif amount <= 0:
            print("Invalid withdrawal amount.")
        else:
            balance -= amount
            print(f"Withdrew ${amount:.2f}. New balance: ${balance:.2f}")

    elif choice == "3":
        print("Exiting... Thank you for using the ATM!")
        break

    else:
        print("Invalid choice. Please try again.")
