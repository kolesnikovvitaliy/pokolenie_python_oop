''' Первый вариант решения'''
class Queue:
    def __init__(self, pairs=[]):
        if isinstance(pairs, dict):
            self.pairs = [(k, v) for k, v in pairs.items()]
        else:
            self.pairs = pairs[:]

    def add(self, item):
        for i, k in enumerate(self.pairs):
            if item[0] == k[0]:
                del self.pairs[i]
        self.pairs.append(item)

    def pop(self):
        if self.pairs:
            return self.pairs.pop(0)
        raise KeyError('Очередь пуста')

    def __repr__(self):
        return f'{__class__.__name__}({self.pairs})'

    def __len__(self):
        return len(self.pairs)
''' Второй вариант решения'''    
# class Queue(dict):
#     def add(self, elem):
#         key, value = elem 
#         if key in self:
#             del self[key]
#         self[key] = value
        
#     def pop(self):
#         if not self:
#             raise KeyError('Очередь пуста')
#         key, value = tuple(self.items())[0]
#         del self[key]
#         return key, value
        
#     def __repr__(self):
#         return f'{type(self).__name__}({list(self.items())})'