''' Первый вариант решения'''
class AllTrue:
    def __eq__(self, __value): return True
    def __ne__(self, __value): return True
    def __lt__(self, __value): return True
    def __gt__(self, __value): return True
    def __le__(self, __value): return True
    def __ge__(self, __value): return True


def anything():
    return AllTrue()
''' Второй вариант решения'''    
# class AlwaysTrue:
#     def __eq__(self, other):
#         return True

#     __ne__ = __lt__ = __le__ = __gt__ = __ge__ = __eq__


# def anything():
#     return AlwaysTrue()