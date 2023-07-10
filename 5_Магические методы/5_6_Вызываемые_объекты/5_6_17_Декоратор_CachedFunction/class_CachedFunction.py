''' Первый вариант решения'''
class CachedFunction:
    cache = {}
    def __init__(self, func):
        self.func = func
    def __call__(self, *args):
        result = self.cache.get(args)
        if result is None:
            result = self.func(*args)
            self.cache[args] = result
        return result
''' Второй вариант решения'''    
# class CachedFunction:
#     def __init__(self, func):
#         self.func = func
#         self.cache = {}
        
#     def __call__(self, *args):
#         if args not in self.cache:
#             self.cache[args] = self.func(*args)
#         return self.cache[args]