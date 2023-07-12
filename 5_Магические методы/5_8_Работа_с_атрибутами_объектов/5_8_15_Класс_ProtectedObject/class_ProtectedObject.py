''' Первый вариант решения'''
class ProtectedObject:
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            object.__setattr__(self, k, v)

    def __getattribute__(self, __name: str):
        if __name.startswith('_'):
            raise AttributeError('Доступ к защищенному атрибуту невозможен')
        return object.__getattribute__(self, __name)
    
    def __setattr__(self, __name: str, __value):
        if __name.startswith('_'):
            raise AttributeError('Доступ к защищенному атрибуту невозможен')
        return object.__setattr__(self, __name, __value)
    
    def __delattr__(self, __name: str):
        if __name.startswith('_'):
            raise AttributeError('Доступ к защищенному атрибуту невозможен')
        return object.__delattr__(self, __name)
''' Второй вариант решения'''    
# class ProtectedObject:    
#     def __init__(self, **kwargs):
#         for attr, value in kwargs.items():
#             object.__setattr__(self, attr, value) 
        
#     @staticmethod
#     def _check_access(attr):
#         if attr.startswith('_'):
#             msg = 'Доступ к защищенному атрибуту невозможен'
#             raise AttributeError(msg)
    
#     def __getattribute__(self, attr):
#         ProtectedObject._check_access(attr)
#         return object.__getattribute__(self, attr)
       
#     def __setattr__(self, attr, value):
#         ProtectedObject._check_access(attr)
#         object.__setattr__(self, attr, value)
        
#     def __delattr__(self, attr):
#         ProtectedObject._check_access(attr)
#         object.__delattr__(self, attr)