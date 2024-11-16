import datetime

class ATM:
    def __init__(self, balance=0):
        self.balance = balance

    def display_welcome(self):
        print("=" * 44)
        print(" " * 8 + "Welcome to Thom Bank ATM")
        print("=" * 44)

    def display_goodbye(self):
        print("=" * 30)
        print(" " * 8 + "Thank you for using ATM")
        print(" " * 12 + "Goodbye!")
        print("=" * 30)

    def check_balance(self):
        print("\n" + "-" * 30)
        print(f"Your current balance is: ${self.balance:.2f}")
        print("-" * 30)
        return f"Balance Inquiry: ${self.balance:.2f}"

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("\n" + "-" * 30)
            print(f"${amount:.2f} deposited successfully.")
            print("-" * 30)
        else:
            print("\nInvalid amount. Please enter a positive value.")

    def withdraw(self, amount):
        if amount <= 0:
            print("\nInvalid amount. Please enter a positive value.")
        elif amount > self.balance:
            print("\nInsufficient balance. You can only withdraw ${}".format(self.balance))
        else:
            self.balance -= amount
            print("\n" + "-" * 30)
            print(f"${amount:.2f} withdrawn successfully.")
            print("-" * 30)
            return f"Withdrawal: ${amount:.2f}"
        return None

    def print_receipt(self, transaction_detail):
        print("\n" + "=" * 30)
        print(" " * 10 + "ATM Receipt")
        print("=" * 30)
        print(f"Date: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(transaction_detail)
        print(f"Remaining Balance: ${self.balance:.2f}")
        print("=" * 30)


def main():
    atm = ATM(balance=500)  
    atm.display_welcome()

    while True:
        print("\nChoose an option:")
        print("1. Check Balance                                    2. Deposit Money")
        
        print("3. Withdraw Money                                   4. Exit")
        

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.")
            continue

        if choice == 1:
            transaction_detail = atm.check_balance()
            print_receipt = input("Would you like a receipt? (yes/no): ").strip().lower()
            if print_receipt == "yes":
                atm.print_receipt(transaction_detail)

        elif choice == 2:
            try:
                amount = float(input("Enter the amount to deposit: "))
                atm.deposit(amount)
            except ValueError:
                print("Invalid amount. Please enter a numeric value.")

        elif choice == 3:
            try:
                amount = float(input("Enter the amount to withdraw: "))
                transaction_detail = atm.withdraw(amount)
                if transaction_detail:
                    print_receipt = input("Would you like a receipt? (yes/no): ").strip().lower()
                    if print_receipt == "yes":
                        atm.print_receipt(transaction_detail)
            except ValueError:
                print("Invalid amount. Please enter a numeric value.")

        elif choice == 4:
            atm.display_goodbye()
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
