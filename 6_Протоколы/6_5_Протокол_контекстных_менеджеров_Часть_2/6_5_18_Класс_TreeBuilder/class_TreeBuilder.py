''' Первый вариант решения'''
class TreeBuilder:
    def __init__(self):
        ''' '''
        self.index = 0
        self._structure = {0: []}

    def __enter__(self):
        self.index += 1
        self._structure[self.index] = []
        return self

    def add(self, obj):
        self._structure.setdefault(self.index, []).append(obj)

    def __exit__(self, exc_type, exc_val, exc_tb):
        last = max(self._structure.keys())
        if last:
            if self._structure[last]:
                self._structure[last-1].append(self._structure.pop(last))
            else:
                self._structure.pop(last)
        self.index -= 1

    def structure(self):
        return self._structure[0]
''' Второй вариант решения'''    
# class TreeBuilder:
#     def __init__(self):
#         self.knots = [[]]
        
#     def __enter__(self):
#         self.knots.append([])
        
#     def __exit__(self, *args, **kwargs):
#         if self.knots[-1]:
#             self.knots[-2].append(self.knots[-1])
#         self.knots.pop()
    
#     def add(self, value):
#         self.knots[-1].append(value)
        
#     def structure(self):
#         return self.knots[-1]