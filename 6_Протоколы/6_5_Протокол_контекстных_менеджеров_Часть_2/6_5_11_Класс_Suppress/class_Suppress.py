''' Первый вариант решения'''
class Suppress:
    def __init__(self, *args):
        self.args = args
        self.exception = None
    
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_value and exc_type  in self.args:
            self.exception = exc_value
        return True
''' Второй вариант решения'''    
# class Suppress:
#     def __init__(self, *exceptions):
#         self.exceptions = exceptions

#     def __enter__(self):
#         return self

#     def __exit__(self, exc_type, exc_val, exc_tb):
#         if exc_type in self.exceptions:
#             self.exception = exc_val
#             return True
#         self.exception = None
#         return False