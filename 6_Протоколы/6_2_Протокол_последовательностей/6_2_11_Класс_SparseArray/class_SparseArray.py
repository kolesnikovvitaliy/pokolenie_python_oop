''' Первый вариант решения'''
class  SparseArray:
    def __init__(self, default=None):
        self.array = []
        self.default = default
    
    def __setitem__(self, key, value):
        i = len(self.array)
        while key > len(self.array):
            self.array.insert(i, self.default)
            i += 1
        self.array.insert(key, value)

    def __getitem__(self, key):
        try:
            return self.array[key]
        except IndexError:
            return self.default
''' Второй вариант решения'''    
# class SparseArray:
#     def __init__(self, default):
#         self.array = {}
#         self.default = default

#     def __len__(self):
#         return len(self.array)

#     def __getitem__(self, key):
#         return self.array.get(key, self.default)

#     def __setitem__(self, key, value):
#         self.array[key] = value