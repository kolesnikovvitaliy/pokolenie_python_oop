''' Первый вариант решения'''
def quantify(iterable, predicate):
        if predicate == None:
            list_none = []
            for i in iterable:
                list_none.append(bool(i))
            return sum(list_none)
        else:
            return sum(map(predicate,iterable))
    
''' Второй вариант решения'''    
# def quantify(iterable, predicate):
#     if predicate is None:
#         predicate = bool
#     return sum(map(predicate, iterable))
#     return sum(map(predicate if predicate else bool, iterable))
#     return len(list(filter(predicate, iterable)))