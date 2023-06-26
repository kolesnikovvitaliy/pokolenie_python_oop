''' Первый вариант решения'''
class BankAccount:
    def __init__(self, balance=0):
        self._balance = balance
    
    def get_balance(self):
        return self._balance
    
    def deposit(self, amount):
            self._balance += amount
            return self._balance
    
    def withdraw(self, amount):
        if (self._balance - amount) >= 0:
            self._balance -= amount
            return self._balance
        raise ValueError('На счете недостаточно средств')
    
    def transfer(self, account, amount):
        self.withdraw(amount)
        account.deposit(amount) 

''' Второй вариант решения'''    
# class BankAccount:
#     def __init__(self, balance=0):
#         self._balance = balance
    
#     def get_balance(self):
#         return self._balance
    
#     def deposit(self, amount):
#         self._balance += amount
    
#     def withdraw(self, amount):
#         if self._balance < amount:
#             raise ValueError('На счете недостаточно средств')
#         self._balance -= amount

#     def transfer(self, account, amount):
#         self.withdraw(amount)
#         account.deposit(amount)
    