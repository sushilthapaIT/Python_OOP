from Account import Account
from Chequing import Chequing
from Savings import Savings
from Investment import Investment

# Create accounts
account1 = Account("Aaron Sarson")
chequing1 = Chequing("Jim Cooper", fee=5, overdraft_limit=1000)
savings1 = Savings("Anushka Sharma", interest_rate=2)
investment1 = Investment("Apurba Pokharel")

# Print initial account information
print("Initial Account Information:")
print(account1)
print("\nInitial Chequing Account Information:")
print(chequing1)
print("\nInitial Savings Account Information:")
print(savings1)
print("\nInitial Investment Account Information:")
print(investment1)

# Deposit and withdraw operations
account1.deposit(500)
account1.withdraw(200)

chequing1.deposit(1000)
chequing1.withdraw(300)

savings1.deposit(2000)
savings1.withdraw(500)
savings1.apply_interest()

investment1.deposit(1500)
investment1.buy("IBM", 3)
investment1.sell("IBM", 2)
investment1.update_stock_price("SHOP", 1000)

# Print updated account information
print("\nUpdated Account Information:")
print(account1)
print("\nUpdated Chequing Account Information:")
print(chequing1)
print("\nUpdated Savings Account Information:")
print(savings1)
print("\nUpdated Investment Account Information:")
print(investment1)