''' Первый вариант решения'''
class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def get_fullname(self):
        return f'{self.name} {self.surname}'

    def set_fullname(self, fullname):
        self.name, self.surname = fullname.split()

    fullname = property(get_fullname, set_fullname)
''' Второй вариант решения'''    
# class Person:
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname

#     @property
#     def fullname(self):
#         return self.name, self.surname

#     @fullname.setter
#     def fullname(self, fullname):
#         self.name, self.surname = fullname.split()

#     @fullname.getter
#     def fullname(self):
#         return f'{self.name} {self.surname}'