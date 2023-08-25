''' Первый вариант решения'''
import functools


def track_instances(cls):
    old_init = cls.__init__
    cls.instances = []

    @functools.wraps(old_init)
    def decorator(self, *args, **kwargs):
        old_init(self, *args, **kwargs)
        cls.instances.append(self)
    cls.__init__ = decorator
    return cls
''' Второй вариант решения'''    
# import functools


# def track_instances(cls):
#     cls_init = cls.__init__
#     cls.instances = []

#     @functools.wraps(cls_init)
#     def new_init(self, *args, **kwargs):
#         cls_init(self, *args, **kwargs)
#         self.instances.append(self)

#     cls.__init__ = new_init
#     return cls