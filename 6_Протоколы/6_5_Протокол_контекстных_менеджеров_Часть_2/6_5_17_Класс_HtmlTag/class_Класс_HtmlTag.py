''' Первый вариант решения'''
class HtmlTag:
    level = -1
    def __init__(self, tag, inline=False):
        self.tag = tag
        self.inline = inline
    
    def __enter__(self):
        __class__.level += 1
        if self.inline:
            print('  ' * __class__.level + f'<{self.tag}>', end='')
        else:
            print('  ' * __class__.level + f'<{self.tag}>')
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        if self.inline:
            __class__.level -= 1
            print(f'</{self.tag}>')
        else:
            print('  ' * __class__.level + f'</{self.tag}>')
        __class__.level -= 1

    def print(self, text):
        __class__.level += 1
        if self.inline:
            print(text, end='')
        else:
            print('  ' * __class__.level + text)
            __class__.level -= 1
''' Второй вариант решения'''    
# class HtmlTag:
#     '''Creating the right html body'''
    
#     counter = 0
    
#     def __init__(self, tag, inline=False):
#         self.tag = tag
#         self.inline = '' if inline else '\n'
        
#     def __enter__(self):
#         print(f'{"  " * HtmlTag.counter}<{self.tag}>', end = self.inline)
#         HtmlTag.counter += 1
#         return self
    
#     def print(self, text):
#         print(f'{"  " * HtmlTag.counter if self.inline else ""}{text}', end=self.inline)
        
#     def __exit__(self, exc_type, exc_value, exc_traceback):
#         HtmlTag.counter -= 1
#         print(f'{"  " * HtmlTag.counter if self.inline else ""}</{self.tag}>')