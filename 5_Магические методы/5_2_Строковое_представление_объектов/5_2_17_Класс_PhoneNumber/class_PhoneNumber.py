''' Первый вариант решения'''
class PhoneNumber:
    def __init__(self, arg):
        if ' ' in arg:
            self.phone_number = ''.join(map(lambda x: x if x != ' ' else '',arg))
        else:
            self.phone_number = arg


    def __str__(self) -> str:
        return f'({self.phone_number[:3]}) {self.phone_number[3:6]}-{self.phone_number[6:]}'
    
    def __repr__(self):
        return f"{__class__.__name__}('{self.phone_number}')"
''' Второй вариант решения'''    
# class PhoneNumber:
#     def __init__(self, phone_number):
#         self.phone_number = phone_number.replace(' ', '')

#     def __str__(self):
#         return f'({self.phone_number[:3]}) {self.phone_number[3:6]}-{self.phone_number[6:]}'

#     def __repr__(self):
#         return f"PhoneNumber('{self.phone_number}')"