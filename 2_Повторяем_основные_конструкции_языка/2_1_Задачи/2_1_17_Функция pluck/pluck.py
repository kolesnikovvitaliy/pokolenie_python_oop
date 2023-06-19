''' Первый вариант решения'''
def pluck(data, path, default=None):
    list_key = path.split('.')
    try:
        for key in range(len(list_key)):
            data = data[list_key[key]]
        return data
    except:
        return default

# d = {'a': {'b': {'c': {'d': {'e': 4}}}}}
# print(pluck(d, 'a.b.c'))

''' Второй вариант решения'''    
# def pluck(data, path, default=None):
#     for key in path.split('.'):
#         data = data.get(key, default)
#     return data