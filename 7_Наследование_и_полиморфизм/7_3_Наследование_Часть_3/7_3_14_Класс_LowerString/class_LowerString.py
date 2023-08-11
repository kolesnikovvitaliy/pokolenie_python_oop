''' Первый вариант решения'''
class LowerString(str):
    def __new__(cls, obj=''):
        obj = super().__new__(cls, str(obj).lower())
        return obj
''' Второй вариант решения'''    
# class LowerString(str):
#     def __new__(cls, obj=''):
#         return super().__new__(cls, str(obj).lower())