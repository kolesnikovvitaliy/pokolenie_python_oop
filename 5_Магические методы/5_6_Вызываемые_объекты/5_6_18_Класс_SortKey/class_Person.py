''' Первый вариант решения'''
class SortKey:
    def __init__(self, *args):
       self.arg = args

    def __call__(self, obj):
        __result = []
        for key in self.arg:
            __result.append(obj.__dict__[key])
        return __result
''' Второй вариант решения'''    
# class SortKey:
#     def __init__(self, *attributes):
#         self.attributes = attributes

#     def __call__(self, instance):
#         return [getattr(instance, attribute) for attribute in self.attributes]