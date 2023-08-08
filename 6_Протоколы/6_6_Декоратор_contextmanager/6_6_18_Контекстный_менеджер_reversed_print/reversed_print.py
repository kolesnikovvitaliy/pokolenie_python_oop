''' Первый вариант решения'''
from contextlib import contextmanager
import sys


@contextmanager
def reversed_print():
    func = sys.stdout.write
    sys.stdout.write = lambda x: func(''.join(reversed(x)))
    yield
    sys.stdout.write = func
''' Второй вариант решения'''    
# import sys
# from contextlib import contextmanager


# @contextmanager
# def reversed_print():
#     original_write = sys.stdout.write

#     def reverse_write(text):
#         original_write(text[::-1])

#     sys.stdout.write = reverse_write
#     yield
#     sys.stdout.write = original_write