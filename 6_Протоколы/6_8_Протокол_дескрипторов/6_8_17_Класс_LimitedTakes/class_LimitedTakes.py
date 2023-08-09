''' Первый вариант решения'''
class MaxCallsException(Exception):...


class LimitedTakes:
    def __init__(self, times):
        self._times = times

    def __set_name__(self, cls, attr):
        self._name = attr

    def __get__(self, obj, cls):
        if self._times > 0:
            if self._name in obj.__dict__:
                self._times -= 1
                return obj.__dict__[self._name]
            raise AttributeError('Атрибут не найден')
        raise MaxCallsException('Превышено количество доступных обращений')

    def __set__(self, obj, value):
        obj.__dict__[self._name] = value
''' Второй вариант решения'''    
# class MaxCallsException(Exception):
#     def __init__(self, message='Превышено количество доступных обращений'):
#         super().__init__(message)


# class LimitedTakes:
#     def __init__(self, times):
#         self.times = times
#         self.calls = 0

#     def __set_name__(self, owner, name):
#         self._name = name

#     def __get__(self, instance, owner):
#         if self._name in instance.__dict__:
#             if self.calls < self.times:
#                 self.calls += 1
#                 return instance.__dict__[self._name]
#             raise MaxCallsException
#         raise AttributeError('Атрибут не найден')

#     def __set__(self, instance, value):
#         instance.__dict__[self._name] = value