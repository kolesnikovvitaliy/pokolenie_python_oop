''' Первый вариант решения'''
def intersperse(iterable, delimiter):
    iter = list(iterable)
    a = []
    for i in range(len(iter)):
        a.append(iter[i])
        if i != iter.index(iter[-1]):
            a.append(delimiter)
    for i in a:
        yield i

# iterable = iter('Beegeek')
# print(*intersperse(iterable, '+'))

''' Второй вариант решения'''    
# def intersperse(iterable, delimiter):
#     first = True
#     for item in iterable:
#         if not first:
#             yield delimiter
#         first = False
#         yield item