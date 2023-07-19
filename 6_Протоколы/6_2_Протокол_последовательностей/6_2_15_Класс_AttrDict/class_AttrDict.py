''' Первый вариант решения'''
class AttrDict:
    def __init__(self, data=()):   
        self.__dict__.update(data)
    
    def __setitem__(self, key, value):
        self.__dict__[key]= value
    
    def __getitem__(self, key):
        return self.__dict__[key]
    
    def __setattr__(self, __name, __value):
        return self.__dict__

    def __len__(self):
        return len(self.__dict__)
    
    def __iter__(self):
        yield from self.__dict__
''' Второй вариант решения'''    
# class AttrDict:
#     def __init__(self, data=()):
#         self._data = dict(data) or {}

#     def __len__(self):
#         return len(self._data)

#     def __getitem__(self, key):
#         return self._data[key]

#     def __setitem__(self, key, value):
#         self._data[key] = value

#     def __getattr__(self, key):
#         return self._data[key]

#     def __iter__(self):
#         yield from self._data