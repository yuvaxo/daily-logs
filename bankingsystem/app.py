import business as bus

def user_info(name, acc_no, balance=None):
    user_data = []

    if balance is not None:
        user_data.append([name, acc_no, balance])
    else:
        user_data.append([name, acc_no])

    print("\n📄 User Info:", user_data)


def main():
    name = input("Enter your name: ")
    acc_no = int(input("Enter your account Number: "))

    balance = 0
    has_balance = False

    check_balance = input("Do you want to check your balance [yes/no]: ").lower()
    if check_balance == "yes":
        balance = int(input("Enter your account Balance: "))
        has_balance = True
        user_info(name, acc_no, balance)
    else:
        user_info(name, acc_no)

    withdraw_choice = input("\nDo you want to withdraw any amount from Your account [yes/no]: ").lower()
    if withdraw_choice == "yes":
        if not has_balance:
            balance = int(input("Enter the account balance: "))
            has_balance = True

        withdrawal_amt = int(input("Enter the amount to withdraw: "))
        if withdrawal_amt > balance:
            print("❌ Insufficient balance. Withdrawal failed.")
        else:
            balance = bus.withdraw(balance, withdrawal_amt)
            print(f"✅ Amount {withdrawal_amt} withdrawn successfully.")
            print(f"💰 Total Balance: {balance}")

    deposit_choice = input("\nDo you want to deposit any amount [yes/no]: ").lower()
    if deposit_choice == "yes":
        if not has_balance:
            balance = int(input("Enter the total account balance: "))
            has_balance = True
        deposit_amt = int(input("Enter the amount to deposit: "))
        balance = bus.deposit(balance, deposit_amt)
        print(f"✅ Amount {deposit_amt} deposited successfully.")
        print(f"💰 Total Balance: {balance}")


if __name__ == "__main__":
    main()
