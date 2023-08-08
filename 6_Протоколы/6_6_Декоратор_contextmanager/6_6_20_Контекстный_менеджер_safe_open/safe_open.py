''' Первый вариант решения'''
from contextlib import contextmanager


@contextmanager
def safe_open(filename, mode='r'):
    try:
        file_ = open(filename, mode)
        result = (file_, None)
        yield result
        file_.close()
    except Exception as error:
        result = (None, error)
        yield result
''' Второй вариант решения'''    
# from contextlib import contextmanager

# @contextmanager
# def safe_open(filename, mode='r', file=None):
#     try:
#         file = open(filename, mode)
#         yield file, None
#     except Exception as e:
#         yield None, e
#     finally:
#         if file:
#             file.close()