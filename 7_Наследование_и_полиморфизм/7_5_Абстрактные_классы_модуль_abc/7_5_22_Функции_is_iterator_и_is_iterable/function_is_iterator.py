''' Первый вариант решения'''
from collections.abc import Iterable, Iterator


def is_iterable(obj):
    return isinstance(obj, Iterable)


def is_iterator(obj):
    return isinstance(obj, Iterator)
''' Второй вариант решения'''    
# from collections.abc import Iterable, Iterator

# is_iterable = lambda obj: isinstance(obj, Iterable)
# is_iterator = lambda obj: isinstance(obj, Iterator)