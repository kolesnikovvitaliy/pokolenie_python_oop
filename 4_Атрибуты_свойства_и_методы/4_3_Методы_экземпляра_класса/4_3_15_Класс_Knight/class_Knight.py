''' Первый вариант решения'''
class Knight:
    def __init__(self, horizontal: str, vertical: int, color: str):
        self.horizontal = horizontal
        self.vertical = vertical
        self.color = color

    def get_char(self):
        return 'N'
    
    def can_move(self, x: str, y: int):
        import re
        if re.findall('[a-h]', x) and y in range(0,9):
            if (self.vertical - y == 2) or (y - self.vertical  == 2):
               if chr(ord(self.horizontal)+1) == x or chr(ord(self.horizontal)-1) == x:
                   return True
            elif chr(ord(self.horizontal)+2) == x or chr(ord(self.horizontal)-2) == x:
                if (self.vertical - y == 1) or (y - self.vertical  == 1):
                    return True
        return False
            
    def move_to(self, x: str, y: int):
        if self.can_move(x, y):
            self.horizontal = x
            self.vertical = y
            
    def draw_board(self):
        col = {v: k for k,v in enumerate([chr(i) for i in range(ord('a'), ord('i'))])}
        row = {k:v for k,v in list(zip(range(1,9),range(7,-1,-1)))}
        arr = [["N" if [i, j] == [row[self.vertical], col[self.horizontal]] else '.' for j in range(8)] for i in range(8)]
        for i in range(8):
            for j in range(8):
                if (row[self.vertical] - i) * (col[self.horizontal] - j) in [-2, 2]: arr[i][j] = "*" 
        for line in arr:
            print(*line, sep = '')

''' Второй вариант решения'''    
# class Knight:
#     def __init__(self, col, row, color):
#         self.col = col
#         self.row = row
#         self.color = color
        
#     def get_char(self):
#         return 'N'
    
#     def can_move(self, col, row):
#         return (ord(self.col) - ord(col))**2 + (self.row - row)**2 == 5
    
#     def move_to(self, col, row):
#         if self.can_move(col, row):
#             self.col = col
#             self.row = row
            
#     def draw_board(self):
#         for row in range(8, 0, -1):
#             for col in 'abcdefgh':
#                 if self.col == col and self.row == row:
#                     print(self.get_char(), end='')
#                 elif self.can_move(col, row):
#                     print('*', end='')
#                 else:
#                     print('.', end='')
#             print()