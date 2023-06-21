''' Первый вариант решения'''
class User:
    def __init__(self, name):
        self.name = name
        self.friends = 0

    def add_friends(self, n):
        self.friends += n

''' Второй вариант решения'''    
# @__import__('dataclasses').dataclass
# class User:
#     name: str
#     friends: int = 0

#     def add_friends(self, n):
#         self.friends += n