''' Первый вариант решения'''
class Config:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = object.__new__(cls)
        return cls._instance

    def __init__(self):
        self.program_name = 'GenerationPy'
        self.environment = 'release'
        self.loglevel = 'verbose'
        self.version = '1.0.0'


''' Второй вариант решения'''    
# class Config:
#     _instance = None
    
#     def __new__(cls):
#         if cls._instance is None:
#             cls._instance = object.__new__(cls)
#             cls._instance.program_name = 'GenerationPy'
#             cls._instance.environment = 'release'
#             cls._instance.loglevel = 'verbose'
#             cls._instance.version = '1.0.0'
#         return cls._instance