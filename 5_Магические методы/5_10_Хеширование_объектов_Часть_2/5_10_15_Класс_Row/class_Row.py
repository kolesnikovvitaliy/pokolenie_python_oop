''' Первый вариант решения'''
class Row:
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            object.__setattr__(self, k, v)
    
    def __setattr__(self, __name: str, __value):
            if __name in self.__dict__.keys():
                 raise AttributeError('Изменение значения атрибута невозможно')
            raise AttributeError('Установка нового атрибута невозможна')
    
    def __delattr__(self, __name: str):
        raise AttributeError('Удаление атрибута невозможно')

    def __getattribute__(self, __name: str):
        return object.__getattribute__(self, __name)
    
    @property
    def _fields(self):
        return tuple((k, v) for k,v in self.__dict__.items())

    def __eq__(self, __value: object):
        if isinstance(__value, __class__):
            return self._fields == __value._fields
        return NotImplemented
    
    def __hash__(self) -> int:
        return hash(self._fields)
    
    def __repr__(self) -> str:
        str_args =', '.join([f"{k}='{v}'" if type(v) == str else f"{k}={v}"for k,v in self.__dict__.items()])
        return f'{__class__.__name__}({str_args})'
        
''' Второй вариант решения'''    
# class Row:
#     def __init__(self, **kwargs):
#         self.__dict__.update(kwargs)
    
#     @property
#     def _fields(self):
#         return tuple(self.__dict__.items())
    
#     def __repr__(self):
#         attrs = ', '.join(f'{name}={repr(value)}' for name, value in self._fields)
#         return f'Row({attrs})'
    
#     def __eq__(self, other):
#         if isinstance(other, Row):
#             return self._fields == other._fields
#         return NotImplemented
    
#     def __hash__(self):
#         return hash(self._fields)
    
#     def __setattr__(self, name, value):
#         if hasattr(self, name):
#             raise AttributeError('Изменение значения атрибута невозможно')
#         raise AttributeError('Установка нового атрибута невозможна')
    
#     def __delattr__(self, name):
#         raise AttributeError('Удаление атрибута невозможно')