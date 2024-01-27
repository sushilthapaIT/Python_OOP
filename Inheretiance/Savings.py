from Account import Account

class Savings(Account):
    def __init__(self, owner, interest_rate, currency = "CAD", balance = 0.0):
        super().__init__(owner, currency, balance)
        self.interest_rate = interest_rate

        if interest_rate < 0:
            print("ERROR: InterestRate should be a non-negative value")

    def apply_interest(self):
        monthly_interest = (self.balance * self.interest_rate / 100) / 12
        self.balance += monthly_interest

    def set_interest_rate(self, new_rate):
        if new_rate < 0:
            print("ERROR: InterestRate should be a non-negative value")
        else:
            self.interest_rate = new_rate

    def get_interest_rate(self):
        return self.interest_rate