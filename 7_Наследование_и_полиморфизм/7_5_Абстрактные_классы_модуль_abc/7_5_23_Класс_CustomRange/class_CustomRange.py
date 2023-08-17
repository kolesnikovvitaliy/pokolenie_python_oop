''' Первый вариант решения'''
from collections.abc import Sequence


class CustomRange(Sequence):
    def __init__(self, *args):
        self.args = self.set_items(args)

    def set_items(self, args):
        __result = []
        for i in args:
            if isinstance(i, str):
                __tmp = [int(j) for j in i.split('-')]
                __tmp[1] += 1
                __tmp = range(*__tmp)
                __result.extend([j for j in __tmp])
            else:
                __result.append(i)
        return __result

    def __getitem__(self, index):
        return self.args[index]

    def __len__(self):
        return len(self.args)
''' Второй вариант решения'''    
# from collections.abc import Sequence


# class CustomRange(Sequence):
#     def __init__(self, *args):
#         self._data = []
#         for arg in args:
#             start, stop = (arg, arg) if isinstance(arg, int) else map(int, arg.split('-'))
#             self._data.extend(range(start, stop + 1))

#     def __getitem__(self, item):
#         if isinstance(item, (int, slice)):
#             return self._data[item]
#         return NotImplemented

#     def __len__(self):
#         return len(self._data)