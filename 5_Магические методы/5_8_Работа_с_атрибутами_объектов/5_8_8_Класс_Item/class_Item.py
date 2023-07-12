''' Первый вариант решения'''
class Item:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __getattribute__(self, name):
        if name == 'total': 
            return self.price * self.quantity
        elif name == 'name':
            return object.__getattribute__(self, name).title()
        return object.__getattribute__(self, name)
''' Второй вариант решения'''    
# class Item:
#     def __init__(self, name, price, quantity):
#         self.name = name
#         self.price = price
#         self.quantity = quantity

#     def __getattribute__(self, attr):
#         if attr == 'name':
#             return object.__getattribute__(self, attr).title()
#         return object.__getattribute__(self, attr)
    
#     def __getattr__(self, attr):
#         if attr == 'total':
#             return self.price * self.quantity
#         raise AttributeError