''' Первый вариант решения'''
from contextlib import contextmanager


@contextmanager
def safe_write(filename):
    copy_file = f'copy_{filename}'
    try:
        tmp = open(copy_file, 'w')
        yield tmp
        tmp.close()
        tmp = open(copy_file, 'r')
        file = open(filename, 'w')
        file.write(tmp.read())
        tmp.close()
        file.close()
    except Exception as error:
        print(f"Во время записи в файл было возбуждено исключение {type(error).__name__}")
        file = open(filename, 'r')
        tmp = open(copy_file, 'w')
        tmp.write(file.read())
        file.close()
    finally:
        tmp.close()
''' Второй вариант решения'''    
# from contextlib import contextmanager

# @contextmanager
# def safe_write(filename):
#     try:
#         with open(filename + '_', 'w') as f_copy:
#             yield f_copy
#         with open(filename, 'w') as f_orig, open(filename + '_', 'r') as f_copy:
#             f_orig.write(f_copy.read())
#     except Exception as e:
#         print(f"Во время записи в файл было возбуждено исключение {type(e).__name__}")