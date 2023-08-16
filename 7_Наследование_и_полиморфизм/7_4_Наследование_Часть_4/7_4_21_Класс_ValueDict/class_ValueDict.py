''' Первый вариант решения'''
class ValueDict(dict):
    def key_of(self, value):
        if value in self.values():
            for k, v in self.items():
                if v == value:
                    return k
        else:
            return None

    def keys_of(self, value):
        if value in self.values():
            return [i[0] for i in self.items() if int(i[1]) == value]
        return iter([])
''' Второй вариант решения'''    
# class ValueDict(dict):
#     def key_of(self, value):
#         return next(self.keys_of(value), None)
    
#     def keys_of(self, value):
#         return (i for i, j in self.items() if j == value)