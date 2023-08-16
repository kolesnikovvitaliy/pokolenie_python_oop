''' Первый вариант решения'''
class EasyDict(dict):
    def __init__(self, iterables):
        super().__init__(iterables)
        for k, v in self.items():
            setattr(self, k, v)

    def __setitem__(self, key, value):
        self.__dict__[key] = value
''' Второй вариант решения'''    
# class EasyDict(dict):
#     def __getattr__(self, item):
#         print(self)
#         return self[item]