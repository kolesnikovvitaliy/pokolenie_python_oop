''' Первый вариант решения'''
from collections import UserDict


class BirthdayDict(UserDict):
    def __setitem__(self, key, item):
        if item in self.values():
            print(f'Хей, {key}, не только ты празднуешь день рождения в ' +
                  'этот день!')
        return super().__setitem__(key, item)
''' Второй вариант решения'''    
# from collections import UserDict

# class BirthdayDict(UserDict):

#     def __setitem__(self, key, value):
#         if value in self.data.values():
#             print(f'Хей, {key}, не только ты празднуешь день рождения в этот день!')
#         self.data[key] = value