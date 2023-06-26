''' Первый вариант решения'''
class User:
    def __init__(self, name, age):
        self.set_name(name)
        self.set_age(age)
        self._name = self.get_name()
        self._age = self.get_age()

    def get_name(self):
        return self._name
    
    def set_name(self, new_name):
        if (not isinstance(new_name, str) or not new_name.isalpha()):
            raise ValueError('Некорректное имя')
        self._name = new_name

    def get_age(self):
        return self._age

    def set_age(self, new_age):
        if new_age not in range(0,111):
            raise ValueError('Некорректный возраст')
        self._age = new_age
```

''' Второй вариант решения'''    
# class User:
#     def __init__(self, name, age):
#         self.set_name(name)
#         self.set_age(age)

#     def set_name(self, name):
#         if isinstance(name, str) and name.isalpha():
#             self._name = name
#         else:
#             raise ValueError('Некорректное имя')
    
#     def set_age(self, age):
#         if isinstance(age, int) and 0 <= age <= 100:
#             self._age = age
#         else:
#             raise ValueError('Некорректный возраст')
   
#     def get_name(self):
#         return self._name

#     def get_age(self):
#         return self._age
