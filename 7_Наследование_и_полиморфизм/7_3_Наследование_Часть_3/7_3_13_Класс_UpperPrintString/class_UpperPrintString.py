''' Первый вариант решения'''
class UpperPrintString(str):
    def __str__(self):
        return f'{super().__str__().upper()}'
''' Второй вариант решения'''    
# class UpperPrintString(str):
#     def __str__(self):
#         return self.upper()