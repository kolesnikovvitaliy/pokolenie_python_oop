''' Первый вариант решения'''
class Numbers:
    def __init__(self):
        self.lst = []

    def add_number(self, n):
        self.lst.append(n)

    def get_even(self):
        return [i for i in self.lst if i % 2 == 0]

    def get_odd(self):
        return [i for i in self.lst if i % 2 != 0]

''' Второй вариант решения'''    
# class Numbers:
#     def __init__(self):
#         self.numbers = []
        
#     def add_number(self, number):
#         self.numbers.append(number)
        
#     def get_even(self):
#         return list(filter(lambda x: not x % 2, self.numbers))

#     def get_odd(self):
#         return list(filter(lambda x: x % 2, self.numbers))