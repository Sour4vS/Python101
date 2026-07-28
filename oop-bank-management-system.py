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


if __name__ == "__main__":
    dave = BankAccount(1000, "Dave")
    sara = BankAccount(2000, "Sara")

    jim = InterestRewardsAccount(1000, "Jim")

    tim = SavingsAccount(3000, "Tim")

    tim.deposit(500)
    tim.withdraw(500)
    tim.transfer(100, jim)
