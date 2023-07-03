''' Первый вариант решения'''
from functools import total_ordering

@total_ordering
class Version:
    def __init__(self, version: str) -> str or bool:
        self.version = {0: '0', 1: '0', 2: '0'}
        for i in {enumerate(version.split('.'))}:
            self.version.update(i)
        self.version = '.'.join(map(lambda x: self.version[x], self.version))
        
    def __str__(self) -> str:
        return f'{self.version}'
    
    def __repr__(self) -> str:
        return f"{__class__.__name__}({repr(self.version)})"
    
    def __eq__(self, __value: object) -> bool:
        if isinstance(__value, Version):
            return self.version == __value.version
        return NotImplemented
        
    def __lt__(self, __value: object) -> bool:
        if isinstance(__value, Version):
            return list(map(int,self.version.split('.'))) < list(map(int, __value.version.split('.')))
        return NotImplemented
''' Второй вариант решения'''    
# from functools import total_ordering

# @total_ordering
# class Version:
#     def __init__(self, version):
#         self._parts = [int(i) for i in version.split('.')]
#         self._parts += [0] * (3 - len(self._parts))

#     def __str__(self):
#         return '{}.{}.{}'.format(*self._parts)
    
#     def __repr__(self):
#         return "Version('{}.{}.{}')".format(*self._parts)
    
#     def __eq__(self, other):
#         if isinstance(other, Version):
#             return self._parts == other._parts
#         return NotImplemented
    
#     def __lt__(self, other):
#         if isinstance(other, Version):
#             return self._parts < other._parts
#         return NotImplemented