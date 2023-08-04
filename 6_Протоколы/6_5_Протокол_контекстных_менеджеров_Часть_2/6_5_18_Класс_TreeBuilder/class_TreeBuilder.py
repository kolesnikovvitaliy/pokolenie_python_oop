''' Первый вариант решения'''
class TreeBuilder:

    def __init__(self):
        self._structure = []
        self._list_stack = [self._structure]

    def __enter__(self):
        self._list_stack[-1].append([])
        self._list_stack.append(self._list_stack[-1][-1])
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if not self._list_stack[-1]:
            self._list_stack[-2].pop()
        self._list_stack.pop()

    def add(self, item):
        self._list_stack[-1].append(item)

    def structure(self):
        return self._structure
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