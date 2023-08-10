''' Первый вариант решения'''
class FieldTracker:
    def __init__(self):
        self.lst = {k: v for k, v in self.__dict__.items()}

    def base(self, arg):
        return self.lst[arg]

    def has_changed(self, arg):
        return self.__dict__[arg] != self.lst[arg]

    def changed(self):
        return {k: v for k, v in self.lst.items() if self.__dict__[k] != v}

    def save(self):
        self.lst = {k: v for k, v in self.__dict__.items() if k != 'lst'}
''' Второй вариант решения'''    
# class FieldTracker:
#     def __init__(self):
#         self._values = {
#             field: getattr(self, field)
#             for field in self.fields
#         }

#     def base(self, field):
#         return self._values[field]

#     def has_changed(self, field):
#         return self._values[field] != getattr(self, field)

#     def changed(self):
#         return {
#             field: self.base(field)
#             for field in self.fields
#             if self.has_changed(field)
#         }

#     def save(self):
#         for field in self.fields:
#             self._values[field] = getattr(self, field)