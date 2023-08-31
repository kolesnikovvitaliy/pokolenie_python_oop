''' Первый вариант решения'''
class CaesarCipher:
    def __init__(self, shift):
        self.shift = shift

    def encode(self, letter):
        _text = ''
        for i in letter:
            number = ord(i)
            if 65 <= number <= 90:
                number = number + self.shift
                if number > 90:
                    number = number - 26
                    _text += chr(number)
                else:
                    _text += chr(number)
            elif 97 <= number <= 122:
                number = number + self.shift
                if number > 122:
                    number = number - 26
                    _text += chr(number)
                else:
                    _text += chr(number)
            else:
                _text += chr(number)
        return _text

    def decode(self, letter):
        _text = ''
        for i in letter:
            number = ord(i)
            if 65 <= number <= 90:
                number = number - self.shift
                if number < 65:
                    number = number + 26
                    _text += chr(number)
                else:
                    _text += chr(number)
            elif 97 <= number <= 122:
                number = number - self.shift
                if number < 97:
                    number = number + 26
                    _text += chr(number)
                else:
                    _text += chr(number)
            else:
                _text += chr(number)
        return _text
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