''' Первый вариант решения'''
from contextlib import contextmanager


@contextmanager
def make_tag(tag):
    print(f'{tag}')
    yield
    print(f'{tag}')
''' Второй вариант решения'''    
# from contextlib import contextmanager


# @contextmanager
# def make_tag(tag):
#     print(tag)
#     yield
#     print(tag)