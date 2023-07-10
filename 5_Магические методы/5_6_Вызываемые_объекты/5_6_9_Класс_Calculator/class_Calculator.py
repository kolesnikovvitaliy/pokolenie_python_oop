''' Первый вариант решения'''
class Calculator:
   def __call__(self, a: int, b: int, operation: str):
        if operation == '/' and b == 0:
            raise ValueError('Деление на ноль невозможно')
        return eval(f'{a}{operation}{b}')
''' Второй вариант решения'''    
# class Calculator:

#     def __call__(self, a, b, operation):
#         match operation:
#             case '+': return a + b
#             case '-': return a - b
#             case '*': return a * b
#             case '/':
#                 try:
#                     return a / b
#                 except:
#                     raise ValueError('Деление на ноль невозможно')