''' Первый вариант решения'''
class TitledText(str):
    def __new__(cls, content, text_title):
        obj = super().__new__(cls, content)
        obj.text_title = text_title
        return obj

    def title(self):
        return self.text_title
''' Второй вариант решения'''    
# class TitledText(str):
#     def __new__(cls, value, title):
#         instance = super().__new__(cls, value)
#         instance.title = lambda: title
#         return instance