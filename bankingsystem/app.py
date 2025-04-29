import business as bus

def user_info(name, acc_no, balance=0):
    user_data = [] 

    if balance:
        user_data.append([name, acc_no, balance])
    else:
        user_data.append([name, acc_no])

    return user_data 

def withdraw(balance):
    withdrawal_amt = int(input("Enter the amount to withdraw: "))
    balance = bus.withdraw(balance, withdrawal_amt)
    print(f"Amount ₹{withdrawal_amt} withdrawed Successfully")
    print(f"Total Balance: ₹{balance}")
    return balance

def deposit(balance):
    deposit_amt = int(input("Enter the amount to deposit: "))
    balance = bus.deposit(balance, deposit_amt)
    print(f"Amount ₹{deposit_amt} Deposited Successfully")
    print(f"Total Balance: ₹{balance}")
    return balance

def main():
    name = input("Enter your name: ")
    acc_no = int(input("Enter your account Number: "))
    

    check_balance = input("Do you want to check your balance [yes/no]: ").lower()
    if check_balance == "yes":
        balance = int(input("Enter Your account Balance: "))
        has_balance = True
        user_data = user_info(name, acc_no, balance)
    else:
        user_data = user_info(name, acc_no)

    print("\nUser Infos:", user_data) 

    withdraw_choice = input("\nDo you want to withdraw any amount from Your account [yes/no]: ").lower()
    if withdraw_choice == "yes":
        if not has_balance:
            balance = int(input("Enter the account balance: "))
        balance = withdraw(balance)

    deposit_choice = input("\nDo you want to deposit any amount [yes/no]: ").lower()
    if deposit_choice == "yes":
        if not has_balance:
            balance = int(input("Enter the total account balance: "))
        balance = deposit(balance)

if __name__ == "__main__":
    main()
