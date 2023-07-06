''' Первый вариант решения'''
class Money:
    def __init__(self, amount: int) -> str:
        self.amount = amount

    def __str__(self) -> str:
        return f"{self.amount} руб."
    
    def __pos__(self) -> int:
        if self.amount >= 0:
            return __class__(self.amount)
        return __class__(~self.amount+1)
    
    def __neg__(self) -> int:
        if self.amount >= 0:
            return __class__(-self.amount)
        return __class__(self.amount)
''' Второй вариант решения'''    
# class Money:
#     def __init__(self, amount):
#         self.amount = amount

#     def __str__(self):
#         return f'{self.amount} руб.'

#     def __pos__(self):
#         return Money(abs(self.amount))

#     def __neg__(self):
#         return Money(-abs(self.amount))