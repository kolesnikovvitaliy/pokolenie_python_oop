''' Первый вариант решения'''
from abc import ABC, abstractmethod


class Validator(ABC):
    def __set_name__(self, cls, attr):
        self._attr = attr

    def __get__(self, obj, cls):
        if obj is None:
            return self
        if self._attr in obj.__dict__:
            return obj.__dict__[self._attr][-1]
        else:
            raise AttributeError('Атрибут не найден')

    def __set__(self, obj, value):
        if self.validate(value):
            obj.__dict__.setdefault(self._attr, []).append(value)

    @abstractmethod
    def validate(self, value):
        pass


class Number(Validator):
    def __init__(self, minvalue=None, maxvalue=None):
        self.minvalue = minvalue
        self.maxvalue = maxvalue

    def validate(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError('Устанавливаемое значение должно быть числом')
        else:
            if self.minvalue is not None:
                if value < self.minvalue:
                    raise ValueError(f'Устанавливаемое число должно быть больше или равно {self.minvalue}')

            if self.maxvalue is not None:
                if value > self.maxvalue:
                    raise ValueError(f'Устанавливаемое число должно быть меньше или равно {self.maxvalue}')
        return True


class String(Validator):
    def __init__(self, minsize=None, maxsize=None, predicate=None):
        self.minsize = minsize
        self.maxsize = maxsize
        self.predicate = predicate

    def validate(self, value):
        if not isinstance(value, str):
            raise TypeError('Устанавливаемое значение должно быть строкой')
        else:
            if self.minsize is not None:
                if len(value) < self.minsize:
                    raise ValueError(f'Длина устанавливаемой строки должна быть больше или равна {self.minsize}')
            if self.maxsize is not None:
                if len(value) > self.maxsize:
                    raise ValueError(f'Длина устанавливаемой строки должна быть меньше или равна {self.maxsize}')
            if self.predicate is not None:
                if not self.predicate(value):
                    raise ValueError('Устанавливаемая строка не удовлетворяет дополнительным условиям')
        return True
''' Второй вариант решения'''    
# from abc import ABC, abstractmethod

# class Validator(ABC):
#     def __set_name__(self, owner, attr):
#         self._attr = attr

#     def __get__(self, obj, cls):
#         if self._attr not in obj.__dict__:
#             raise AttributeError('Атрибут не найден')
#         return obj.__dict__[self._attr]
        
#     def __set__(self, obj, value):
#         self.validate(value)
#         obj.__dict__[self._attr] = value

#     @abstractmethod
#     def validate(self, value):
#         pass

# class Number(Validator):
#     def __init__(self, minvalue=None, maxvalue=None):
#         self.minvalue = minvalue
#         self.maxvalue = maxvalue

#     def validate(self, value):
#         if not isinstance(value, (int, float)):
#             raise TypeError('Устанавливаемое значение должно быть числом')
#         if self.minvalue is not None and value < self.minvalue:
#             raise ValueError(f'Устанавливаемое число должно быть больше или равно {self.minvalue}')
#         if self.maxvalue is not None and value > self.maxvalue:
#             raise ValueError(f'Устанавливаемое число должно быть меньше или равно {self.maxvalue}')

# class String(Validator):
#     def __init__(self, minsize=None, maxsize=None, predicate=None):
#         self.minsize = minsize
#         self.maxsize = maxsize
#         self.predicate = predicate

#     def validate(self, value):
#         if not isinstance(value, str):
#             raise TypeError('Устанавливаемое значение должно быть строкой')
#         if self.minsize is not None and len(value) < self.minsize:
#             raise ValueError(f'Длина устанавливаемой строки должна быть больше или равна {self.minsize}')
#         if self.maxsize is not None and len(value) > self.maxsize:
#             raise ValueError(f'Длина устанавливаемой строки должна быть меньше или равна {self.maxsize}')
#         if self.predicate is not None and not self.predicate(value):
#             raise ValueError('Устанавливаемая строка не удовлетворяет дополнительным условиям')