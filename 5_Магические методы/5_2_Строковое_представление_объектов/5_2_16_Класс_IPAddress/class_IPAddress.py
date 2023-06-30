''' Первый вариант решения'''
from functools import singledispatchmethod


class IPAddress:
    @singledispatchmethod
    def __init__(self, arg):
        self.ipaddress = arg

    @__init__.register(list)
    @__init__.register(tuple)
    def _(self, arg):
        self.ipaddress = '.'.join(map(str,arg))

    def __str__(self):
        return f'{self.ipaddress}'
    
    def __repr__(self) -> str:
        return f"{__class__.__name__}('{self.ipaddress}')"
''' Второй вариант решения'''    
# class IPAddress:
#     def __init__(self, ipadress):
#         if isinstance(ipadress, str):
#             self.ipadress = ipadress
#         elif isinstance(ipadress, (list, tuple)):
#             self.ipadress = '.'.join(map(str, ipadress))
            
#     def __str__(self):
#         return self.ipadress
    
#     def __repr__(self):
#         return f"{self.__class__.__name__}('{self.ipadress}')"