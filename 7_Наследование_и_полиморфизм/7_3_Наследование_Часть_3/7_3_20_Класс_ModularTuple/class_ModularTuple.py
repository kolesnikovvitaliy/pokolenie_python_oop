''' Первый вариант решения'''
class ModularTuple(tuple):
    def __new__(cls, iterable=(), size=100):
        if iterable:
            return super().__new__(cls, tuple(i % size for i in iterable))
        return ()
''' Второй вариант решения'''    
# class ModularTuple(tuple):
#     def __new__(cls, iterable=(), size=100, *args, **kwargs):
#         iterable = map(lambda item: item % size, iterable)
#         instance = super().__new__(cls, iterable)
#         return instance