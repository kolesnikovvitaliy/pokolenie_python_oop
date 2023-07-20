''' Первый вариант решения'''
class MutableString:
    def __init__(self, string=''):
        self._string = string or ''

    
    def lower(self):
        self._string = self._string.lower()

    def upper(self):
        self._string = self._string.upper()

    def __str__(self):
        return f"{self._string}"
    
    def __repr__(self):
        return f"{__class__.__name__}('{self._string}')"
    
    def __len__(self):
        return len(self._string)
    
    def __iter__(self):
        yield from self._string

    def __setitem__(self, key, value):
            __str = [*self._string]
            __str[key] = value
            self._string = ''.join(__str)

    def __getitem__(self, key):
        if isinstance(key, slice):
            return __class__(self._string[key])
        return self._string[key]
    
    def __delitem__(self, key):
        __str = [*self._string]
        del __str[key]
        self._string = ''.join(__str)

    def __add__(self, other):
        return __class__(self._string + other._string)
''' Второй вариант решения'''    
# class MutableString:
#     def __init__(self, string=''):
#         self.string = string
        
#     def __str__(self):
#         return self.string
    
#     def __repr__(self):
#         return f"MutableString('{self.string}')"
    
#     def __len__(self):
#         return len(self.string)
    
#     def __iter__(self):
#         yield from self.string
        
#     def __add__(self, other):
#         return MutableString(self.string+other.string)
    
#     def lower(self):
#         self.string = self.string.lower()

#     def upper(self):
#         self.string = self.string.upper()
        
#     def __getitem__(self, key):
#         if isinstance(key, slice):
#             return MutableString(self.string[key])
#         return self.string[key]
        
#     def __setitem__(self, key, value):
#         self.string = self.string.replace(self.string[key], value)
        
#     def __delitem__(self, key):
#         self.string = self.string.replace(self.string[key], '') 