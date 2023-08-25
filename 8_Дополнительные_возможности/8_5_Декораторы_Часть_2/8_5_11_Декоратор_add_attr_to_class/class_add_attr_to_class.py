''' Первый вариант решения'''
def add_attr_to_class(**attrs):
    def decorator(cls):
        for k, v in attrs.items():
            setattr(cls, k, v)
        return cls
    return decorator
''' Второй вариант решения'''    
# class add_attr_to_class:
#     def __init__(self, **kwargs):
#         self.attrs = kwargs

#     def __call__(self, cls):
#         for attr_name, attr_value in self.attrs.items():
#             setattr(cls, attr_name, attr_value)
#         return cls