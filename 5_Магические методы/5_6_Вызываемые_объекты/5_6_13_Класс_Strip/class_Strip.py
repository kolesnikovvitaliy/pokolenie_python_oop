''' Первый вариант решения'''
class Strip:
    def __init__(self, chars):
        self.chars = chars

    def __call__(self, string):
        return string.strip(self.chars)
''' Второй вариант решения'''    
# import re

# class Strip:
#     def __init__(self, chars):
#         self.chars = re.escape(chars)
#     def __call__(self, string):
#         return re.sub(f"^[{self.chars}]*|[{self.chars}]*$", '', string)