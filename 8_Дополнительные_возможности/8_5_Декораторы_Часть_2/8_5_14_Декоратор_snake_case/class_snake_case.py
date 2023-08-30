''' Первый вариант решения'''
def snake_case(attrs=False):
    def wrapper(cls, *args, **kwargs):
        def replase_name(cls, items, key):
            setattr(cls, items, cls.__dict__[key])
            delattr(cls, key)

        def str_snake_case(item):
            def redact_str(item):
                return ''.join(map(lambda item: item[1].lower() if
                               item[0] == 0 or
                               (item[0] > 0 and item[1].lower() == item[1])
                               else f'_{item[1].lower()}', enumerate(item)))
            if item.startswith('_'):
                item = item[1:]
                _str = '_' + redact_str(item)
                return _str
            return redact_str(item)

        not_dunder_method = [method for method in cls.__dict__.keys()
                             if not method.startswith('__')]
        if attrs:
            for i in not_dunder_method:
                str_snake = str_snake_case(i)
                replase_name(cls, str_snake, i)
            return cls
        else:
            for i in not_dunder_method:
                if 'function' in str(type(cls.__dict__[i])):
                    str_snake = str_snake_case(i)
                    replase_name(cls, str_snake, i)
            return cls
    return wrapper
''' Второй вариант решения'''    
# import re
# from typing import Callable


# def snake_case(attrs=False):
#     regex_object = re.compile(r'_?\B([A-Z])')

#     def wrapper(cls, *args, **kwargs):
#         class_attributes = list(cls.__dict__.keys())
#         for attribute in class_attributes:
#             if any((
#                     attribute.startswith('__') and attribute.endswith('__'),
#                     not isinstance(cls.__dict__[attribute], Callable) and not attrs
#             )):
#                 continue
#             setattr(cls, regex_object.sub(r'_\1', attribute).lower(), cls.__dict__[attribute])
#             delattr(cls, attribute)
#         return cls

#     return wrapper