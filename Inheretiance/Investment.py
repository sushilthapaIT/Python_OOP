from Account import Account

class Investment(Account):
    stock_list = {
        "SHOP": [994.70, "CAD"],
        "IBM": [129.87, "USD"],
        "OTEX": [58.44, "CAD"],
        "JD": [60.70, "USD"],
        "MSFT": [196.84, "USD"]
    }

    def __init__(self, owner, currency="CAD", balance=0.0):
        super().__init__(owner, currency, balance)
        self.cash = 0.0
        self.stock_holdings = {ticker: 0 for ticker in self.stock_list}

    def deposit(self, value):
        if value < 0:
            print("ERROR: Value for deposit/withdraw is restricted to positive values")
        else:
            self.balance += value
            self.cash += value
        
    def withdraw(self, value):
        if value < 0:
            print("ERROR: Value for deposit/withdraw is restricted to positive values")
        else:
            self.balance -= value
            self.cash -= value

    def update_stock_price(self, ticker_symbol, value):
        if ticker_symbol in self.stock_list and value >= 0:
            self.stock_list[ticker_symbol][0] = value
            self.balance += self.stock_holdings[ticker_symbol] * value
        else:
            print("ERROR: Stock price could not be updated!")

    def buy(self, ticker_symbol, amt):
        if ticker_symbol in self.stock_list and amt >= 0:
            stock_price = self.stock_list[ticker_symbol][0]
            stock_currency = self.stock_list[ticker_symbol][1]
            account_currency = self.currency

            if stock_currency != account_currency:
                to_conversion_value = self.conversion_rates[account_currency][0]
                if stock_currency == "CAD":
                    #need to convert stock_currency in cad to account_currency
                    stock_price = stock_price/to_conversion_value
                else:
                    from_conversion_value = self.conversion_rates[stock_currency][0]
                    #convert stock_currency to CAD
                    cad_value = stock_price * from_conversion_value
                    #convert CAD to to_currency
                    stock_price = cad_value/to_conversion_value

            if self.cash >= amt * stock_price:
                self.stock_holdings[ticker_symbol] += amt
                self.cash -= amt * stock_price
            else:
                print("ERROR: Stock purchase could not be completed!")
        else:
            print("ERROR1: Invalid stock symbol or amount")
    

    def sell(self, ticker_symbol, amt):
        if ticker_symbol in self.stock_list and amt >= 0:
            if self.stock_holdings[ticker_symbol] < amt:
                print("ERROR: Stock sale could not be completed!")
            else:
                stock_price = self.stock_list[ticker_symbol][0]
                stock_currency = self.stock_list[ticker_symbol][1]
                account_currency = self.currency

                if stock_currency != account_currency:
                    to_conversion_value = self.conversion_rates[account_currency][0]
                    if stock_currency == "CAD":
                        #need to convert stock_currency in cad to account_currency
                        stock_price = stock_price/to_conversion_value
                    else:
                        from_conversion_value = self.conversion_rates[stock_currency][0]
                        #convert stock_currency to CAD
                        cad_value = stock_price * from_conversion_value
                        #convert CAD to to_currency
                        stock_price = cad_value/to_conversion_value

                    self.stock_holdings[ticker_symbol] -= amt
                    self.cash += amt * stock_price
        else:
            print("ERROR2: Invalid stock symbol or amount")

    def __str__(self):
        stock_str = "\n".join([f"{ticker} - {amt} @ {self.conversion_rates[self.stock_list[ticker][1]][1]}{self.stock_list[ticker][0]:.2f} {self.stock_list[ticker][1]}" for ticker, amt in self.stock_holdings.items()])
        return super().__str__() + f"\nStock Holdings:\n{stock_str}"