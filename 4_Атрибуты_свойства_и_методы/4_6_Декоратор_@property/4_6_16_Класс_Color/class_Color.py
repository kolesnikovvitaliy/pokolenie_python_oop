''' Первый вариант решения'''
class Color:
    def __init__(self, hexcode):
        self.hexcode = hexcode
        
    @property    
    def hexcode(self):
        return self._hexcode
    
    @hexcode.setter
    def hexcode(self, hexcode):
        self._hexcode = hexcode
        self.r, self.g, self.b = int(hexcode[:2], 16),  int(hexcode[2:4], 16),  int(hexcode[4:], 16)
''' Второй вариант решения'''    
# class Color:
#     def __init__(self, hexcode: str) -> None:
#         self.hexcode = hexcode

#     @property
#     def hexcode(self) -> str:
#         return self._hexcode
    
#     @hexcode.setter
#     def hexcode(self, stroke: str) -> None:
#         self._hexcode = stroke
#         self.r, self.g, self.b = (int(stroke[i:i+2], base=16) 
#                                   for i in range(0,6,2))