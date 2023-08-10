''' Первый вариант решения'''
class Validator:
    def __init__(self, obj: object):
        self._obj = obj

    def is_valid(self):
        return None


class NumberValidator(Validator):
    def __init__(self, obj):
        super().__init__(obj)

    def is_valid(self):
        return isinstance(self._obj, (int, float))
''' Второй вариант решения'''    
# class Validator:
#     def __init__(self, obj):
#         self._obj = obj

#     def is_valid(self):
#         pass


# class NumberValidator(Validator):
#     def is_valid(self):
#         return isinstance(self._obj, (int, float))