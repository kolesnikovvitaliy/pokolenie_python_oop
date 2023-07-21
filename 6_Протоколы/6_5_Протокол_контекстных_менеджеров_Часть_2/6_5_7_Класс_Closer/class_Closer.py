''' Первый вариант решения'''
class Closer:
    def __init__(self, obj):
        self.obj = obj

    def __enter__(self):
        return self.obj
    
    def __exit__(self, exc_type, exc_value, traceback):
        try:
            self.obj.close()
        except:
            print("Незакрываемый объект")
        return True
''' Второй вариант решения'''    
# class Closer:
#     def __init__(self, obj):
#         self.obj = obj

#     def __enter__(self):
#         return self.obj

#     def __exit__(self, *args, **kwargs):
#         try:
#             self.obj.close()
#             return False
#         except AttributeError:
#             print('Незакрываемый объект')
#             return True