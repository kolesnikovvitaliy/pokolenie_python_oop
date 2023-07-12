''' Первый вариант решения'''
class NonNegativeObject:
    def __init__(self, **kwargs) -> None:
        self.__dict__.update(kwargs)
    
    def __getattribute__(self, __name: str):
        if isinstance(object.__getattribute__(self, __name), (int, float)):
            return abs(object.__getattribute__(self, __name))
        return object.__getattribute__(self, __name)
''' Второй вариант решения'''    
# class NonNegativeObject:
#     def __init__(self, **kwargs):
#         for name, value in kwargs.items():
#             setattr(self, name, value)
        
#     def __setattr__(self, name, value):
#         if isinstance(value, (int, float)):
#             value = abs(value)
#         object.__setattr__(self, name, value)