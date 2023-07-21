''' Первый вариант решения'''
class ReadableTextFile:
    def __init__(self, filename):
        self.filename = filename
    
    def __enter__(self):
        self.file = open(self.filename, mode='r', encoding='utf-8')
        yield self.file.read().strip()
    
    def __exit__(self, exc_type, exc_value, traceback):
        self.file.close()
        return True
''' Второй вариант решения'''    
# class ReadableTextFile:
#     def __init__(self, filename):
#         self.file = open(filename, encoding='UTF-8')

#     def __enter__(self):
#         return map(str.strip, self.file)

#     def __exit__(self, *args, **kwargs):
#         self.file.close()