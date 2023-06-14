''' Первый вариант решения '''

def jsonify(func):
    import functools, json    
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return json.dumps(func(*args, **kwargs))
    return wrapper

''' Второй вариант решения '''
# import json

# def jsonify(func):
#     def wrapper(*args):
#         wrapper.__name__ = func.__name__
#         wrapper.__doc__ = func.__doc__
#         return json.dumps(func(*args))
#     return wrapper
