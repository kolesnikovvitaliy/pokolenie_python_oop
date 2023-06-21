''' Первый вариант решения'''
class Scales:
    def __init__(self):
        self.right = 0
        self.left = 0
    
    def add_right(self, n):
        self.right += n

    def add_left(self, n):
        self.left += n
    
    def get_result(self):
        if self.right > self.left:
            return 'Правая чаша тяжелее'
        elif self.right < self.left:
            return 'Левая чаша тяжелее'
        else: 
            return 'Весы в равновесии'


''' Второй вариант решения'''    
# class Scales:
#     def __init__(self):
#         self.left = 0
#         self.right = 0

#     def add_left(self, w):
#         self.left += w

#     def add_right(self, w):
#         self.right += w

#     def get_result(self):
#         if self.left == self.right:
#             return 'Весы в равновесии'
#         return ('Левая чаша тяжелее', 'Правая чаша тяжелее')[self.right > self.left]