conversion_rate = {
        "USD": [1.34607, "$"],
        "EUR": [1.51746, "€"],
        "GBP": [1.70233, "£"],
        "CNY": [0.0189917, "¥"],
        "INR": [0.0178035, "₹"],
        "CAD": [1, "$"]
    }
class Account:
    def __init__(self, owner, currency = "CAD", balance = 0.0):
        self.owner = owner
        self.balance = balance
        self.conversion_rates = conversion_rate
        if currency in self.conversion_rates:
            self.currency = currency
        else:
            print("ERROR: Unsupported currency type")
        
    def deposit(self, value):
        if value < 0:
            print("ERROR: Value for deposit/withdraw is restricted to positive values")
        else:
            self.balance += value
        
    def withdraw(self, value):
        if value < 0:
            print("ERROR: Value for deposit/withdraw is restricted to positive values")
        else:
            self.balance -= value

    def getCurrencty(self):
        return self.currency

    def setCurrency(self, to_currency):
        if to_currency in self.conversion_rates:
            balance = self.balance
            from_currency = self.currency
            from_conversion_value = self.conversion_rates[from_currency][0]
            to_conversion_value = self.conversion_rates[to_currency][0]
            if from_currency == "CAD":
                #need to convert CAD to to_currency
                new_value = balance/to_conversion_value
                self.balance = new_value
                self.currency = to_currency
            else:
                #convert from_currency to CAD
                cad_value = balance * from_conversion_value
                #convert CAD to to_currency
                new_value = cad_value/to_conversion_value
                self.balance = new_value
                self.currency = to_currency

        else:
            print("ERROR: Unsupported currency type")

    def __str__(self):
        return f"Owner: {self.owner}\nBalance: {self.conversion_rates[self.currency][1]}{self.balance:.2f}"
    
    def __eq__(self, other):
        obj1_currency = self.currency
        obj2_currency = other.currency
        obj1_cad = 0
        obj2_cad = 0
        if obj1_currency == "CAD":
            obj1_cad = self.balance
        else:
            obj1_value = self.balance
            obj1_cad = obj1_value * self.conversion_rates[obj1_currency][0]
            
        if obj2_currency == "CAD":
            obj2_cad = other.balance
        else:
            obj2_value = other.balance
            obj2_cad = obj2_value * self.conversion_rates[obj2_currency][0]

        obj1_cad = round(obj1_cad,2)
        obj2_cad = round(obj2_cad,2)
        return obj1_cad == obj2_cad
    
    def __add__(self, other):
        to_currency = self.currency
        from_currency = other.currency
        if to_currency == from_currency:
            new_balance = self.balance + other.balance
            return Account(self.owner, self.currency, new_balance)
        else:
            balance = other.balance
            from_conversion_value = self.conversion_rates[from_currency][0]
            to_conversion_value = self.conversion_rates[to_currency][0]
            if from_currency == "CAD":
                #need to convert CAD to to_currency
                new_value = balance/to_conversion_value
                new_balance = self.balance + new_value
                return Account(self.owner, self.currency, new_balance)
            else:
                #convert from_currency to CAD
                cad_value = balance * from_conversion_value
                #convert CAD to to_currency
                new_value = cad_value/to_conversion_value
                new_balance = self.balance + new_value
                return Account(self.owner, self.currency, new_balance)
            
if __name__ == "__main__":
    a = Account("apurba")
    a.deposit(10)
    print(a.balance)