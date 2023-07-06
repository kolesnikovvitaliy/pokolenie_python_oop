''' Первый вариант решения'''
class ReversibleString:
    def __init__(self, string: str) -> str:
        self.string = string

    def __str__(self) -> str:
        return f"{self.string}"

    def __neg__(self):
        return ReversibleString(''.join(reversed(self.string)))
''' Второй вариант решения'''    
# class ReversibleString:
#     def __init__(self, string):
#         self.string = string

#     def __str__(self):
#         return self.string

#     def __neg__(self):
#         return ReversibleString(self.string[::-1])