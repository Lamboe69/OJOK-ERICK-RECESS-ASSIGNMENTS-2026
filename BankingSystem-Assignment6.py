from datetime import datetime


class Transaction:
    def __init__(self, amount, account_holder):
        self.amount = amount
        self.account_holder = account_holder
        self.timestamp = datetime.now()

    def process(self):
        raise NotImplementedError("Subclasses must implement process()")

    def validate(self, amount=None):
        if amount is None:
            amount = self.amount
        return amount > 0

    def display(self):
        return f"Transaction of ${self.amount:.2f} for {self.account_holder}"


class Deposit(Transaction):
    def __init__(self, amount, account_holder, deposit_type="cash"):
        super().__init__(amount, account_holder)
        self.deposit_type = deposit_type

    def process(self):
        if not self.validate():
            return "Deposit failed: Invalid amount"
        return (
            f"Deposited ${self.amount:.2f} into {self.account_holder}'s"
            f" account ({self.deposit_type})"
        )

    def validate(self, amount=None, deposit_type=None):
        if amount is None:
            amount = self.amount
        if amount <= 0:
            return False
        actual_type = deposit_type if deposit_type else self.deposit_type
        if actual_type == "check":
            return amount <= 100000
        return True

    def display(self):
        return (
            f"Deposit: ${self.amount:.2f} | Holder: {self.account_holder}"
            f" | Type: {self.deposit_type}"
        )


class Withdrawal(Transaction):
    def __init__(self, amount, account_holder, balance):
        super().__init__(amount, account_holder)
        self.balance = balance

    def process(self):
        if not self.validate():
            return "Withdrawal failed: Invalid amount or insufficient funds"
        self.balance -= self.amount
        return (
            f"Withdrew ${self.amount:.2f} from {self.account_holder}'s account."
            f" Remaining balance: ${self.balance:.2f}"
        )

    def validate(self, amount=None, balance=None):
        if amount is None:
            amount = self.amount
        if balance is None:
            balance = self.balance
        return amount > 0 and balance >= amount

    def display(self):
        return (
            f"Withdrawal: ${self.amount:.2f} | Holder: {self.account_holder}"
            f" | Balance: ${self.balance:.2f}"
        )


class Transfer(Transaction):
    def __init__(self, amount, sender, recipient):
        super().__init__(amount, sender)
        self.recipient = recipient
        self.sender_balance = 0

    def process(self):
        if not self.validate():
            return "Transfer failed: Insufficient funds"
        self.sender_balance -= self.amount
        return (
            f"Transferred ${self.amount:.2f} from {self.account_holder}"
            f" to {self.recipient}"
        )

    def validate(self, amount=None, sender_balance=None):
        if amount is None:
            amount = self.amount
        if sender_balance is None:
            sender_balance = self.sender_balance
        return amount > 0 and sender_balance >= amount

    def display(self):
        return (
            f"Transfer: ${self.amount:.2f} | From: {self.account_holder}"
            f" | To: {self.recipient}"
        )


def main():
    employer_balance = 100000

    print("=" * 60)
    print("            BANKING SYSTEM - EMPLOYER DEMO")
    print("=" * 60)

    print("\n--- EMPLOYER DEPOSITS FUNDS ---")
    dep = Deposit(50000, "TechCorp Inc.", "check")
    print(dep.display())
    print(f"Result: {dep.process()}")

    print("\n--- EMPLOYER WITHDRAWS FUNDS ---")
    wd = Withdrawal(15000, "TechCorp Inc.", employer_balance)
    print(wd.display())
    print(f"Result: {wd.process()}")

    print("\n--- EMPLOYER TRANSFERS SALARY ---")
    tr = Transfer(5000, "TechCorp Inc.", "John Doe")
    tr.sender_balance = employer_balance - 15000
    print(tr.display())
    print(f"Result: {tr.process()}")

    print("\n--- METHOD OVERLOADING DEMO ---")
    print(f"Deposit.validate(50000): {dep.validate(50000)}")
    print(f"Deposit.validate(50000, 'check'): {dep.validate(50000, 'check')}")
    print(f"Deposit.validate(200000, 'check'): {dep.validate(200000, 'check')}")
    print(f"Withdrawal.validate(100, 30000): {wd.validate(100, 30000)}")
    print(f"Withdrawal.validate(-50, 30000): {wd.validate(-50, 30000)}")
    print(f"Transfer.validate(5000, 85000): {tr.validate(5000, 85000)}")
    print(f"Transfer.validate(200000, 85000): {tr.validate(200000, 85000)}")

    print("\n--- METHOD OVERRIDING DEMO ---")
    for t in [dep, wd, tr]:
        print(f"  {t.display()}")

    print("\n" + "=" * 60)
    print("       ALL TRANSACTIONS COMPLETED")
    print("=" * 60)


if __name__ == "__main__":
    main()
