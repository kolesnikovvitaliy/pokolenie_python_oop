''' Первый вариант решения'''
from collections import UserDict


class MultiKeyDict(UserDict):
    def __init__(self, *args, **kwargs):
        self._key = {}
        super().__init__(*args, **kwargs)
        self._key = {k: k for k in self.data.keys()}

    def alias(self, key, alias):
        if alias not in self.data:
            self._key[alias] = key

    def __getitem__(self, __key):
        if __key in self._key:
            return super().__getitem__(self._key[__key])
        return super().__getitem__(__key)

    def __setitem__(self, __key, __value):
        if __key in self._key:
            self.data[self._key[__key]] = __value
        else:
            self.data[__key] = __value

    def __delitem__(self, __key):
        new_key = [i for i in self._key.keys() if i != __key][0]
        if new_key not in self.data:
            del self._key[__key]
            self._key[new_key] = new_key
            self.data[new_key] = self.data.pop(__key)
            if __key in self._key.values():
                key_2 = [k for k, v in self._key.items() if v == __key][0]
                self._key[key_2] = new_key
        else:
            self.data[__key] = self.data.pop(self._key[__key])
            self._key[__key] = new_key
            del self._key[new_key]
            del self.data[__key]
''' Второй вариант решения'''    
# from collections import UserDict


# class MultiKeyDict(UserDict):
#     def __init__(self, *args, **kwargs):
#         self._aliases = {}
#         super().__init__(*args, **kwargs)

#     def alias(self, key, alias):
#         self._aliases[alias] = key

#     def __getitem__(self, key):
#         return self.data.get(key) or self.data.get(self._aliases[key])

#     def __setitem__(self, key, value):
#         if key in self.data or key not in self._aliases:
#             self.data[key] = value
#         else:
#             self.data[self._aliases[key]] = value

#     def __delitem__(self, del_key):
#         for alias_key, key in self._aliases.items():
#             if key == del_key:
#                 self.data[alias_key] = self.data[del_key]
#         del self.data[del_key]
