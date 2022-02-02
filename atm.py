def show_menu():
    print("+++++Menu+++++")
    print("1.Balance")
    print("2.Deposit")
    print("3.Withdraw")
    print("4.Exit")


balance = 0

while True:

    show_menu()

    option = int(input("Select option: "))

    if option == 1:
        print("your balance:", balance)
    elif option == 2:
        amount_deposit = int(input("Enter amount: "))
        balance = amount_deposit + balance
    elif option == 3:
        amount_withdraw = int(input("Enter amount: "))
        if amount_withdraw <= balance:
            balance = balance - amount_withdraw
        else:
            print("You have insufficient balance!")
    elif option == 4:
        print("Exiting...")
        break
    else:
        print("Invalid option!!")

    more = input("Would you like another transaction? (y/n): ")
    if more.lower() == 'n':
        print("Goodbye...")
        break
