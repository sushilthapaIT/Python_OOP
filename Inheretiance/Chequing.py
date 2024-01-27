from Account import Account

class Chequing(Account):
    def __init__(self, owner, fee, overdraft_limit, currency = "CAD", balance = 0.0):
        super().__init__(owner, currency, balance)
        self.fee = fee
        self.overdraft_limit = overdraft_limit

        if overdraft_limit < 0:
            print("ERROR: OverdraftLimit should be a positive value")

        if balance > overdraft_limit:
            print("ERROR: Overdraft limit has been exceeded")

    def withdraw(self, amount):
        if amount < 0:
            print("ERROR: Value for withdraw is restricted to positive values")
        else:
            if self.balance - amount - self.fee < -self.overdraft_limit:
                print("ERROR: Overdraft limit will be exceeded. Withdrawal abandoned!")
            else:
                self.balance -= (amount + self.fee)

    def set_fee(self, new_fee):
        if new_fee < 0:
            print("ERROR: Fee should be a positive value")
        else:
            self.fee = new_fee

    def get_fee(self):
        return self.fee

    def set_overdraft_limit(self, new_limit):
        if new_limit < 0 or self.balance < -new_limit:
            print("ERROR: Overdraft limit will be exceeded. Update abandoned!")
        else:
            self.overdraft_limit = new_limit

    def get_overdraft_limit(self):
        return self.overdraft_limit

    def __str__(self):
        return super().__str__() + f"\nFee: {self.conversion_rates[self.currency][1]}{self.fee:.2f}\nOverdraft Limit: {self.conversion_rates[self.currency][1]}{self.overdraft_limit:.2f}"