import random

class Coin:
    def __init__(self):
        self.side = "Heads"
        
    def toss(self):
        if random.randint(0, 1) == 0:
            self.side = "Heads"
        else:
            self.side = "Tails"

    def get_side(self):
        return self.side
    
# # Create a coin instance
# my_coin = Coin()

# # Display the initial side
# print("Initial side:", my_coin.get_side())

# # Toss the coin
# my_coin.toss()

# # Display the side after the toss
# print("Side after toss:", my_coin.get_side())
    
def main():
    my_coin = Coin()

    print("This side is up:", my_coin.get_side())

    print("I am tossing the coin...")
    my_coin.toss()

    print("This side is up:", my_coin.get_side())


main()