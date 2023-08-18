''' Первый вариант решения'''
class MROHelper:
    @staticmethod
    def len(cls):
        return len(cls.mro())

    @staticmethod
    def class_by_index(cls, n=0):
        return cls.mro()[n]

    @staticmethod
    def index_by_class(child, parent):
        return child.mro().index(parent)
''' Второй вариант решения'''    
# class MROHelper:

#     @staticmethod
#     def len(cls):
#         return len(cls.__mro__)

#     @staticmethod
#     def class_by_index(child, n=0):
#         return child.__mro__[n]

#     @staticmethod
#     def index_by_class(child, parent):
#         return child.__mro__.index(parent)