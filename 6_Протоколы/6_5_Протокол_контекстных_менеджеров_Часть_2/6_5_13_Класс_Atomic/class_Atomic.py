''' Первый вариант решения'''
from copy import deepcopy


class Atomic:
    def __init__(self, data, deep=False):
        self.data = data
        self._copy = deepcopy(data)
        self.deep = deep

    def __enter__(self):
        return self.data
    
    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type == None:
            return self.data
        else:
            if self.deep:
                if isinstance(self.data, list):
                    self.data[:] = self._copy[:]
                elif isinstance(self.data, dict):
                    for k, v in self._copy.items():
                        self.data[k] = v
                elif isinstance(self.data, set):
                    self.data.clear()
                    self.data.update(self._copy)
            else: 
                if isinstance(self.data, list):
                    if isinstance(self.data[0], list):
                        self.data[:] = self.data[:len(self._copy)]
                    else:
                        self.data[:] = self._copy[:]
                elif isinstance(self.data, dict):
                    for k, v in self.data.items():
                        self.data[k] = v
                elif isinstance(self.data, set):
                    self.data.clear()
                    self.data.update(self._copy)                
        return True
''' Второй вариант решения'''    
# import copy


# class Atomic:
#     def __init__(self, data, deep=False):
#         self.original = data
#         self.copy = copy.deepcopy if deep else copy.copy
        
#         if isinstance(data, list):
#             self.original_update = self.original.extend
#         elif isinstance(data, (set, dict)):
#             self.original_update = self.original.update

#     def __enter__(self):
#         self.data = self.copy(self.original)
#         return self.data

#     def __exit__(self, exc_type, exc_val, exc_tb):
#         if exc_type is None:
#             self.original.clear()
#             self.original_update(self.data)
#         return True