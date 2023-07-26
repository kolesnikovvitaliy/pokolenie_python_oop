''' Первый вариант решения'''
class WriteSpy:
    def __init__(self, file_1, file_2, to_close=False):
        self.file_1 = file_1
        self.file_2 = file_2
        self.to_close = to_close
    
    def write(self, text):
        if self.writable():
            self.file_1.write(text)
            self.file_2.write(text)
        else:
            raise ValueError('Файл закрыт или недоступен для записи')
    
    def close(self):
        self.file_1.close()
        self.file_2.close()

    def writable(self):
        if self.file_1.closed or self.file_2.closed:
            return False
        else:
            if self.file_1.__dict__['mode'] == 'w' and self.file_2.__dict__['mode'] == 'w':
                return True
            return False
        
    def closed(self):
        if self.file_1.closed and self.file_2.closed:
            return True
        return False

    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        if self.to_close:
            self.close()
''' Второй вариант решения'''    
# class WriteSpy:
#     def __init__(self, file1, file2, to_close=False):
#         self.file1 = file1
#         self.file2 = file2
#         self.to_close = to_close

#     def __enter__(self):
#         return self

#     def __exit__(self, *args, **kwargs):
#         if self.to_close:
#             self.close()

#     def write(self, text):
#         try:
#             self.file1.write(text)
#             self.file2.write(text)
#         except:
#             raise ValueError("Файл закрыт или недоступен для записи")

#     def writable(self):
#         if self.file1.closed or self.file2.closed:
#             return False
#         return self.file1.writable() and self.file2.writable()

#     def close(self):
#         self.file1.close()
#         self.file2.close()

#     def closed(self):
#         return self.file1.closed and self.file2.closed