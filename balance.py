class BankAccount:
    def __init__(self):
        self.__balance = 0

    def deposit(self, amt):
        self.__balance += amt

    def withdraw(self):
        self.__balance 