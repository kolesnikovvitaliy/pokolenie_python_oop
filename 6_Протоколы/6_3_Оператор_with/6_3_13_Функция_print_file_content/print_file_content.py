''' Первый вариант решения'''
def print_file_content(filename):
    try:
        with open(filename, mode='r', encoding='utf-8') as file:
            print(file.read())
    except:
        print('Файл не найден')
''' Второй вариант решения'''    
# class HandlerFileNotFoundError:
#     def __init__(self, func):
#         self.func = func

#     def __call__(self, *args, **kwargs):
#         try:
#             return self.func(*args, **kwargs)
#         except:
#             print("Файл не найден")


# @HandlerFileNotFoundError
# def print_file_content(filename):
#     with open(filename, encoding="utf-8") as f1:
#         print(f1.read())
