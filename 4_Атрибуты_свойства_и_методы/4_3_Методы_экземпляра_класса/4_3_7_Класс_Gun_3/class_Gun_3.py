''' Первый вариант решения'''
class Gun:
    def __init__(self):
        self.count = 0

    def shoot(self):
        if self.count % 2:
            print('paf')
        else: print('pif')
        self.count += 1

    def shots_count(self):
        return self.count

    def shots_reset(self):
        self.count = 0
        return self.count

''' Второй вариант решения'''    
# class Gun:
#     def __init__(self):
#         self.count = 0
        
#     def shoot(self):
#         print(('pif', 'paf')[self.count%2])
#         self.count += 1
        
#     def shots_count(self):
#         return self.count
    
#     def shots_reset(self):
#         self.count = 0