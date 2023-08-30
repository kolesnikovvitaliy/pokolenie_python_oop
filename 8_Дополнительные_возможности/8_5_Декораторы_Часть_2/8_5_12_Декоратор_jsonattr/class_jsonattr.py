''' Первый вариант решения'''
import json


def jsonattr(filename):
    def decorator(cls):
        with open(filename, 'r', encoding='utf-8') as file:
            for attr, volue in json.loads(file.read()).items():
                setattr(cls, attr, volue)
        return cls
    return decorator
''' Второй вариант решения'''    
# import json


# def jsonattr(filename):
#     def wrapper(cls):
#         with open(filename) as js:
#             attrs = json.load(js)
#         for attr, value in attrs.items():
#             setattr(cls, attr, value)

#         return cls

#     return wrapper