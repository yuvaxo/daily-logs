import business as bus

def main():
    user_info = []
    name = input("Enter your name: ")
    acc_no = int(input("Enter your account Number: "))
    check_balance = input("Do you want to check your balance [yes/no]: ").lower()
    balance = 0

    if check_balance == "yes":
        balance = int(input("Enter Your account Balace: "))

   
    if check_balance == "yes":
        user_info.append([name, acc_no, balance])
    else:
        user_info.append([name, acc_no])

    print("\nUser Info:", user_info)

    withdraw_choice = input("Do you want to withdraw any amount from Your account [yes/no]: ").lower()
    if withdraw_choice == "yes":
        withdrawal_amt = int(input("Enter the amount to withdraw : "))
        if balance == 0:
            balance = int(input("Enter the account balace: "))

        balance = bus.withdraw(balance, withdrawal_amt)
        print(f"Amount {withdrawal_amt} withdrawed Successfully")
        print(f"Total Balace: {balance}")

    deposit_choice = input("Do you want to Deposite any amount [yes/no]: ").lower()
    if deposit_choice == "yes":
        if balance == 0:
            balance = int(input("Enter the total account balace: "))
        deposit_amt = int(input("Enter the amount to Deposit: "))
        balance = bus.deposit(balance, deposit_amt)
        print(f"Amount {deposit_amt} Deposited Sucessfully")
        print(balance)

if __name__ == "__main__":
    main()
