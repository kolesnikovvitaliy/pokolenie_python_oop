''' Первый вариант решения'''
class Father:
    def __init__(self, mood='neutral'):
        self.mood = mood

    def greet(self):
        return 'Hello!'

    def be_strict(self):
        self.mood = 'strict'


class Mother(Father):
    def greet(self):
        return 'Hi, honey!'

    def be_kind(self):
        self.mood = 'kind'


class Daughter(Mother):
    pass


class Son(Mother, Father):
    def greet(self):
        return Father.greet(self)
''' Второй вариант решения'''    
# from abc import ABC, abstractmethod


# class Family(ABC):
#     def __init__(self, mood='neutral'):
#         self.mood = mood

#     @abstractmethod
#     def greet(self):
#         pass


# class Father(Family):
#     def greet(self):
#         return 'Hello!'

#     def be_strict(self):
#         self.mood = 'strict'


# class Mother(Family):
#     def greet(self):
#         return 'Hi, honey!'

#     def be_kind(self):
#         self.mood = 'kind'


# class Daughter(Mother, Father):
#     pass


# class Son(Father, Mother):
#     pass