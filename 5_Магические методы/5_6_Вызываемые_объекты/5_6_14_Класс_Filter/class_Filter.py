''' Первый вариант решения'''
class Filter:
    def __init__(self, predicate=None):
        self.predicate = predicate

    def __call__(self, iterable):
        if self.predicate is not None:
            return list(filter(self.predicate, iterable))
        return list(filter(bool, iterable))
''' Второй вариант решения'''    
# class Filter:
#     def __init__(self, func):
#         self.func = func or bool
        
#     def __call__(self, itrbl):
#         return [x for x in itrbl if self.func(x)]