''' Первый вариант решения'''
class AnyClass:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)
        self.__any = ", ".join(map(lambda k: f"{k}='{kwargs[k]}'" if type(kwargs[k]) == str else f"{k}={kwargs[k]}", kwargs))
    def __str__(self) -> str:
        return f'AnyClass: {self.__any}'
    
    def __repr__(self) -> str:
        return f"{__class__.__name__}({self.__any})"
''' Второй вариант решения'''    
# class AnyClass:
#     def __init__(self, **kwargs):
#         for k, v in kwargs.items():
#             setattr(self, k, v)

#     def __str__(self):
#         return f'AnyClass: {", ".join(self._attrs())}'
        
#     def __repr__(self):
#         return f'AnyClass({", ".join(self._attrs())})'
    
#     def _attrs(self):
#         return [f'{k}={repr(v)}' for (k, v) in self.__dict__.items()]