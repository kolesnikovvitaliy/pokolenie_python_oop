''' Первый вариант решения'''
def singleton(cls):
    cls._instance = None

    def decorator(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = object.__new__(cls)
        return cls._instance
    cls.__new__ = decorator
    return cls
''' Второй вариант решения'''    
# def singleton(cls):
#     _instance = object.__new__(cls)
    
#     def new_new(cls, *args, **kwargs):
#         return _instance
    
#     cls.__new__ = new_new
#     return cls