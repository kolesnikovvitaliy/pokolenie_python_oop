''' Первый вариант решения'''
class Bee:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def move_up(self, n):
        self.y += n

    def move_down(self, n):
        self.y -= n

    def move_right(self, n):
        self.x += n

    def move_left(self, n):
        self.x -= n

''' Второй вариант решения'''    
# class Bee:
#     def __init__(self, x: int = 0, y: int = 0):
#         self.x = x
#         self.y = y

#     def move_up(self, n: int):
#         self.y += n

#     def move_down(self, n: int):
#         self.y -= n

#     def move_right(self, n: int):
#         self.x += n

#     def move_left(self, n: int):
#         self.x -= n