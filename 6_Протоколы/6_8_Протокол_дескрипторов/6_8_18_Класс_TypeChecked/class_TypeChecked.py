''' Первый вариант решения'''
class TypeChecked:
    def __init__(self, *args):
        self._args = args

    def __set_name__(self, cls, attr):
        self._attr = attr

    def __get__(self, obj, cls):
        if self._attr in obj.__dict__:
            return obj.__dict__[self._attr]
        raise AttributeError('Атрибут не найден')

    def __set__(self, obj, value):
        if type(value) in self._args:
            obj.__dict__[self._attr] = value
        else:
            raise TypeError('Некорректное значение')
''' Второй вариант решения'''    
# class TypeChecked:
#     def __init__(self, *types):
#         self._types = types

#     def __set_name__(self, cls, attr):
#         self._attr = attr

#     def __get__(self, obj, cls):
#         if obj is None:
#             return self
#         if self._attr in obj.__dict__:
#             return obj.__dict__[self._attr]
#         raise AttributeError('Атрибут не найден')

#     def __set__(self, obj, value):
#         if not isinstance(value, self._types):
#             raise TypeError('Некорректное значение')
#         obj.__dict__[self._attr] = value