''' Первый вариант решения'''
class AttrsNumberObject:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)
        self.attrs_num = 0
            
    def __setattr__(self, __name, __value):
        return object.__setattr__(self, __name, __value)

    def __getattribute__(self, __name: str):
        if __name == 'attrs_num':
            return len(self.__dict__)
        return object.__getattribute__(self, __name)
''' Второй вариант решения'''    
# class AttrsNumberObject:
#     def __init__(self, **kwargs):
#         self.__dict__.update(kwargs)
    
#     def __getattr__(self, name):
#         if name == 'attrs_num':
#             return len(self.__dict__) + 1