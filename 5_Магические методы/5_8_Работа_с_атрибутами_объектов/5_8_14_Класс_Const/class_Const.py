''' Первый вариант решения'''
class Const:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def __setattr__(self, __name: str, __value):
        if __name in self.__dict__:
            raise AttributeError('Изменение значения атрибута невозможно')
        return object.__setattr__(self, __name, __value)
    
    def __getattribute__(self, __name: str):
        return object.__getattribute__(self, __name)
    
    def __delattr__(self, __name: str):
        raise AttributeError('Удаление атрибута невозможно')
''' Второй вариант решения'''    
# class Const:
#     def __init__(self, **kwargs): 
#         self.__dict__.update(kwargs)
        
#     def __setattr__(self, name, value):
#         if hasattr(self, name):
#             raise AttributeError('Изменение значения атрибута невозможно')
#         super().__setattr__(name, value)
        
#     def __delattr__(self, name): 
#         raise AttributeError('Удаление атрибута невозможно')       