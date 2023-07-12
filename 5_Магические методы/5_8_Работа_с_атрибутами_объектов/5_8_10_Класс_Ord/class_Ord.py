''' Первый вариант решения'''
class Ord:
    def __getattribute__(self, __name: str):
        return ord(__name)
''' Второй вариант решения'''    
# class Ord:
#     def __getattribute__(self, item):
#         if len(item) == 1:
#             return ord(item)
#         return object.__getattribute__(self, item)