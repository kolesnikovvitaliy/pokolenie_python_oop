''' Первый вариант решения'''
from copy import deepcopy



class SequenceZip:
    def __init__(self, *args):
        self.args = deepcopy(args)
        
    def __len__(self):
        return len(list((zip(*self.args))))
    
    def __iter__(self):
        yield from zip(*self.args)

    def __next__(self):
        yield zip(*self.args)

    def __getitem__(self, key):
        self.__lst = zip(*self.args)
        for i in range(key+1):
            if i == key:
                return next(self.__lst)
            next(self.__lst)
''' Второй вариант решения'''    
# import copy


# class SequenceZip:
#     def __init__(self, *sequences):
#         self.sequences = copy.deepcopy(sequences)

#     def __len__(self):
#         return min((len(s) for s in self.sequences), default=0)

#     def __getitem__(self, index):
#         count = -1
#         for item in self:
#             count += 1
#             if count == index:
#                 return item

#     def __iter__(self):
#         yield from zip(*self.sequences)