''' Первый вариант решения'''
class Animal:
    def sleep(self): ...
    def eat(self): ...


class Fish(Animal):
    def swim(self): ...


class Bird(Animal):
    def lay_eggs(self): ...


class FlyingBird(Bird):
    def fly(self): ...
''' Второй вариант решения'''    
# class Animal:
#     def sleep(self):
#         pass

#     def eat(self):
#         pass


# class Fish(Animal):
#     def swim(self):
#         pass


# class Bird(Animal):
#     def lay_eggs(self):
#         pass


# class FlyingBird(Bird):
#     def fly(self):
#         pass