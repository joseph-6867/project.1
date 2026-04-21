class Bank:
    def __init__(self, balance):
        self.__balance = balance  

    def get_balance(self):
        return self.__balance

b = Bank(1000)
print(b.get_balance())
