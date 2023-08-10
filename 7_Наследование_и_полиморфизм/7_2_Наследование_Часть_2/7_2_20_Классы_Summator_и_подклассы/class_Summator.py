''' Первый вариант решения'''
class Summator:
    def total(self, n):
        return sum([i for i in range(n+1)])


class SquareSummator(Summator):
    def total(self, n):
        return sum([i**2 for i in range(n+1)])


class QubeSummator(Summator):
    def total(self, n):
        return sum([i**3 for i in range(n+1)])


class CustomSummator(Summator):
    def __init__(self, m):
        self.m = m

    def total(self, n):
        return sum([i**self.m for i in range(n+1)])
''' Второй вариант решения'''    
# class Summator:
#     def transform(self, n):
#         return n
    
#     def total(self, n):
#         return sum(self.transform(i) for i in range(1, n + 1))
    
# class SquareSummator(Summator):
#     def transform(self, n):
#         return n ** 2
    
# class QubeSummator(Summator):
#     def transform(self, n):
#         return n ** 3
    
# class CustomSummator(Summator):
#     def __init__(self, power):
#         self.power = power
    
#     def transform(self, n):
#         return n ** self.power