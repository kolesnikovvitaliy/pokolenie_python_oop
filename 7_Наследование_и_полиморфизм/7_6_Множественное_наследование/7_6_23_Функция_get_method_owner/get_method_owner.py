''' Первый вариант решения'''


def get_method_owner(cls, method):
    for class_ in cls.mro()[:-1]:
        if method in class_.__dict__:
            return class_
    return None


''' Второй вариант решения'''

# def get_method_owner(cls, method):
#     '''Return class location of method'''
#     for el in cls.mro():
#         if method in el.__dict__:
#             return el
