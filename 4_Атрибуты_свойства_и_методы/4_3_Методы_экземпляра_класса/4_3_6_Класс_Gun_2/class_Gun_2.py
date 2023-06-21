''' Первый вариант решения'''
class Gun:
    def __init__(self):
        self.count = 0

    def shoot(self):
        a = ['pif','paf']
        if self.count % 2 == 0:
            print(a[0])
        else: print(a[1])
        self.count += 1

''' Второй вариант решения'''    
from itertools import cycle


class Gun:
    def __init__(self):
        self.shots = cycle(('pif', 'paf'))
        
    def shoot(self):
        print(next(self.shots))