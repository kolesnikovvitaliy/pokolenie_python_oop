''' Первый вариант решения'''
class SuperInt(int):
    def repeat(self, n=2):
        if self > 0:
            return SuperInt(str(self) * n)
        return -SuperInt(str(self)[1:] * n)

    def to_bin(self):
        if self > 0:
            return SuperInt(str(bin(self))[2:])
        return -SuperInt(str(bin(int(str(self)[1:])))[2:])

    def __iter__(self):
        if self > 0:
            yield from [SuperInt(i) for i in str(self)]
        else:
            yield from [SuperInt(i) for i in str(self)[1:]]

    def next(self):
        return SuperInt(self+1)

    def prev(self):
        return SuperInt(self-1)
''' Второй вариант решения'''    
# class SuperInt(int):

#     def repeat(self, n=2):
#         return SuperInt(str(self) * n)

#     def to_bin(self):
#         return format(self, 'b')

#     def next(self):
#         return SuperInt(self + 1)

#     def prev(self):
#         return SuperInt(self - 1)

#     def __iter__(self):
#         yield from map(SuperInt, str(self).lstrip('-'))