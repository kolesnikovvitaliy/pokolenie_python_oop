''' Первый вариант решения'''
def recviz(func): 
    import inspect
    def wrapper(*args,**kwargs):
        c = len(inspect.getouterframes(inspect.currentframe()))//2-1
        args_repr = [repr(a) for a in args]                      
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]  
        signature = ", ".join(args_repr + kwargs_repr)
        print(f'{"    "*c}-> {func.__name__}({signature})')
        value = func(*args,**kwargs)
        print(f'{"    "*c}<- {value!r}')    
        return value
    return wrapper

# @recviz
# def fib(n):
#     if n <= 2:
#         return 1
#     else:
#         return fib(n - 1) + fib(n - 2)
    
# fib(4)

''' Второй вариант решения'''    
# import functools


# def recviz(func):
#     level = -1

#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         nonlocal level
#         level += 1

#         pos_args = list(map(repr, args))
#         keyword_args = [f'{k}={v!r}' for k, v in kwargs.items()]

#         print('    ' * level + '->', f'{func.__name__}({", ".join(pos_args + keyword_args)})')
#         value = func(*args, **kwargs)
#         print('    ' * level + '<-', repr(value))

#         level -= 1
#         return value

#     return wrapper