''' Первый вариант решения'''
def limiter(limit, unique, lookup):
    def wrapper(cls):
        cls._instances = []

        def decorator(*args, **kwargs):
            num_uniq = [getattr(i, unique) for i in cls._instances]
            if args[1] in num_uniq:
                return cls._instances[args[1]]
            elif args[0] in num_uniq:
                return cls._instances[args[0]-1]

            if len(cls._instances) < limit:
                cls._instances.append(cls(*args, **kwargs))
                return cls._instances[-1]

            if lookup == 'FIRST':
                return cls._instances[0]
            return cls._instances[-1]
        return decorator
    return wrapper
''' Второй вариант решения'''    
# def limiter(limit, unique, lookup):
#     instances = {}
#     lookups = {}

#     def wrapper(cls):
#         def get_instance(*args, **kwargs):
#             instance = cls(*args, **kwargs)
#             lookups.setdefault('FIRST', instance)
#             identifier = getattr(instance, unique)
#             if len(instances) < limit:
#                 if identifier not in instances:
#                     lookups['LAST'] = instances[identifier] = instance
#                 return instances[identifier]
#             return instances.get(identifier) or lookups.get(lookup)

#         return get_instance

#     return wrapper