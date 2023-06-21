''' Первый вариант решения'''
from collections import Counter


class Postman:
    def __init__(self):
        self.delivery_data = []

    def add_delivery(self, st, h, ap):
        self.delivery_data.append((st, h, ap))

    def get_houses_for_street(self, st):
        return list(map(lambda j: j[0], Counter(map(lambda y: y[1], filter(lambda x: st in x , self.delivery_data ))).items()))
    def get_flats_for_house(self, st, h):
        return list(map(lambda j: j[0], Counter(map(lambda y: y[2], filter(lambda x: st in x and h in x, self.delivery_data ))).items()))


''' Второй вариант решения'''    
# class Postman:
#     def __init__(self):
#         self.delivery_data = []

#     def add_delivery(self, street, house, apartment):
#         self.delivery_data.append((street, house, apartment))

#     def get_houses_for_street(self, street):
#         return list({h: None for s, h, _ in self.delivery_data if s == street})

#     def get_flats_for_house(self, street, house):
#         return list({a: None for s, h, a in self.delivery_data if s == street and h == house})