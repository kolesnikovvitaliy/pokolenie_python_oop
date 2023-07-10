''' Первый вариант решения'''
class CountCalls: 
    calls = 0

    def __init__(self, func):
        self.func = func
        
    def __call__(self, *args, **kwargs):
            self.calls +=1
            return self.func(*args, **kwargs)
''' Второй вариант решения'''    
# def CountCalls(func):
#     def wrapper(*args, **kwargs):
#         wrapper.calls += 1
#         value = func(*args, **kwargs)
#         return value
#     wrapper.calls = 0
#     return wrapper