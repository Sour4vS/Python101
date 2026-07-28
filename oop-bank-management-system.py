import json


class BalanceException(Exception):
    pass


class BankAccount:
    def __init__(self, initial_amount, account_name):
        self.balance = initial_amount
        self.name = account_name
        print(f"\n'{self.name}' account created.")
        self.get_balance()

    def get_balance(self):
        print(f"Balance: ${self.balance:.2f}")

    def deposit(self, amount):
        self.balance += amount
        print("\nDeposit completed successfully.")
        self.get_balance()

    def viable_transaction(self, amount):
        if self.balance >= amount:
            return
        raise BalanceException(
            f"Account '{self.name}' has only ${self.balance:.2f} available."
        )

    def withdraw(self, amount):
        try:
            self.viable_transaction(amount)
            self.balance -= amount
            print("\nWithdrawal completed successfully.")
            self.get_balance()
        except BalanceException as error:
            print(f"\nWithdrawal interrupted: {error}")

    def transfer(self, amount, account):
        try:
            print("\nBeginning transfer...")
            self.viable_transaction(amount)
            self.withdraw(amount)
            account.deposit(amount)
            print("Transfer completed successfully.")
        except BalanceException as error:
            print(f"\nTransfer interrupted: {error}")


class InterestRewardsAccount(BankAccount):
    def deposit(self, amount):
        self.balance += amount * 1.05
        print("\nDeposit completed with 5% interest reward.")
        self.get_balance()


class SavingsAccount(InterestRewardsAccount):
    def __init__(self, initial_amount, account_name):
        super().__init__(initial_amount, account_name)
        self.fee = 5

    def withdraw(self, amount):
        try:
            self.viable_transaction(amount + self.fee)
            self.balance -= amount + self.fee
            print("\nWithdrawal completed successfully.")
            self.get_balance()
        except BalanceException as error:
            print(f"\nWithdrawal interrupted: {error}")


class BankManager:
    def __init__(self):
        self.accounts = []

    def add_account(self, account):
        self.accounts.append(account)

    def display_accounts(self):
        print("\n------ Accounts ------")
        for account in self.accounts:
            account.get_balance()

    def save_data(self):
        with open("accounts.json", "w") as file:

            data = []

            for account in self.accounts:
                data.append(account.__dict__)

            json.dump(data, file, indent=4)

        print("\nAccounts saved successfully.")

    def load_data(self):
        try:
            with open("accounts.json", "r") as file:

                data = json.load(file)

                self.accounts = []

                for account_data in data:
                    account = BankAccount(
                        account_data["balance"],
                        account_data["name"]
                    )
                    self.accounts.append(account)

            print("\nAccounts loaded successfully.")

        except FileNotFoundError:
            print("\nNo account file found. Starting with empty database.")


if __name__ == "__main__":

    manager = BankManager()

    manager.load_data()

    if len(manager.accounts) == 0:

        dave = BankAccount(1000, "Dave")
        sara = BankAccount(2000, "Sara")
        jim = InterestRewardsAccount(1000, "Jim")
        tim = SavingsAccount(3000, "Tim")

        manager.add_account(dave)
        manager.add_account(sara)
        manager.add_account(jim)
        manager.add_account(tim)

    else:
        dave = manager.accounts[0]
        sara = manager.accounts[1]
        jim = manager.accounts[2]
        tim = manager.accounts[3]

    tim.deposit(500)
    tim.withdraw(500)
    tim.transfer(100, jim)

    manager.display_accounts()

    manager.save_data()
