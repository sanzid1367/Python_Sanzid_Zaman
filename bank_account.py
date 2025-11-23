class BankAccount:
    def __init__(self, account_number, holder_name, balance):
        # Private fields using double underscore
        self.__account_number = account_number
        self.__holder_name = holder_name
        self.__balance = balance
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Success! New Balance: ${self.__balance}")
        else:
            print("Error: Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Error: Insufficient funds (Cannot go below zero).")
        else:
            self.__balance -= amount
            print(f"Success! New Balance: ${self.__balance}")

    def display_account(self):
        print(f"Account {self.__account_number} - Holder: {self.__holder_name} - Balance: ${self.__balance}")

    @staticmethod
    def validate_account_number(account_number):

        if len(account_number) == 10 and account_number.isdigit():
            return True
        return False


print("--- Create New Account ---")
acc_num = input("Enter Account Number (10 digits): ")

if BankAccount.validate_account_number(acc_num):
    
    name = input("Enter Holder Name: ")
    initial_balance = float(input("Enter Initial Balance: "))

    my_account = BankAccount(acc_num, name, initial_balance)

    while True:
        print("\n--- Menu ---")
        print("1. Deposit Money")
        print("2. Withdraw Money")
        print("3. Display Details")
        print("4. Exit")
        
        choice = input("Choose an option: ")

        if choice == '1':
            amt = float(input("Amount to deposit: "))
            my_account.deposit(amt)
        elif choice == '2':
            amt = float(input("Amount to withdraw: "))
            my_account.withdraw(amt)
        elif choice == '3':
            my_account.display_account()
        elif choice == '4':
            print("Exiting system. Goodbye!")
            break
        else:
            print("Invalid option. Try again.")

else:
    print("Invalid Account Number! It must be exactly 10 digits.")