''' Первый вариант решения'''
class Reloopable:
    def __init__(self, file):
        self.file = file

    def __enter__(self):
        return [self.file.read()]
    
    def __exit__(self, exc_type, exc_value, traceback):
        self.file.close()
''' Второй вариант решения'''    
# class Reloopable:
#     def __init__(self, file):
#         self.file = file 
        
#     def __enter__(self):
#         return list(self.file)
    
#     def __exit__(self, *args, **kwargs):
#         self.file.close()