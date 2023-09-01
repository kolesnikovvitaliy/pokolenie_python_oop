''' Первый вариант решения'''
class CaesarCipher:
    def __init__(self, shift):
        self.shift = shift

    def encode(self, letter, code=1):
        _text = ''
        __ex = self.shift * code
        for i in letter:
            a, b = (97, 122) if i.isalpha() and i.lower() == i else (65, 90)
            if ord(i) in range(a, b+1):
                if (ord(i) + __ex) > b:
                    i = chr(((ord(i) + __ex) - b) + a - 1)
                    _text += i
                elif (ord(i) + __ex) < a:
                    i = chr(b - (a - (ord(i) + __ex + 1)))
                    _text += i
                else:
                    i = chr(ord(i) + __ex)
                    _text += i
            else:
                _text += i
        return _text

    def decode(self, letter):
        return self.encode(letter, -1)
''' Второй вариант решения'''    
# from re import search, I

# class CaesarCipher:
#     def __init__(self: object, n: int) -> None:
#         self.n = n
        
#     def encode(self: object, string: str, code: int|bool = True) -> str:
#         new_str, n = '', code * self.n
#         for i in string:
#             if search(r'[a-z]', i, I):
#                 x = [65, 97][i.lower() == i]
#                 i = chr((ord(i) + n - x) % 26 + x)
#             new_str += i
#         return new_str
    
#     def decode(self: object, string: str) -> str:
#         return self.encode(string, -1)