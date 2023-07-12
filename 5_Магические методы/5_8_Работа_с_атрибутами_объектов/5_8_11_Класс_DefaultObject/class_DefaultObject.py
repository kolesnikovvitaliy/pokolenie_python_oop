''' Первый вариант решения'''
class DefaultObject:
    def __init__(self, default=None, **kwargs):
        self.default = default
        for args in kwargs.items():
            setattr(self, *args)

    def __getattribute__(self, __name: str):
            return object.__getattribute__(self, __name)
    
    def __getattr__(self, __name: str):
        return self.default
        
''' Второй вариант решения'''    
# class DefaultObject:
#     def __init__(self, default=None, **kwargs):
#         self.default = default
#         self.__dict__.update(kwargs)
        
#     def __getattr__(self, name):
#         return self.default