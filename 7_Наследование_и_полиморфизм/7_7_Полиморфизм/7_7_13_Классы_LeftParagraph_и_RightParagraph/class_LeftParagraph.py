''' Первый вариант решения'''
from abc import abstractmethod


class LeftParagraph:
    def __init__(self, length):
        self.length = length
        self.string = []

    def add(self, text):
        self.string.extend(text.split())

    def end(self):
        _lst = ['']
        while len(self.string) > 0:
            if len(_lst[-1] + self.string[0] + '\n') <= self.length:
                _lst.append(_lst[-1].strip() + ' ' + self.string[0])
                del _lst[-2]
                self.string = self.string[1:]
            else:
                _lst.append('\n')
        return self.print_text(_lst)

    @abstractmethod
    def print_text(self, data):
        for i in data:
            print(''.join(i).strip())


class RightParagraph(LeftParagraph):
    def print_text(self, data):
        for i in data:
            i = ' '*(self.length - len(i)) + i
            print(''.join(i))
''' Второй вариант решения'''    
# from abc import ABC, abstractmethod


# class Paragraph(ABC):
#     def __init__(self, length):
#         self._size = length
#         self._paragraph = ['']

#     def add(self, words):
#         words = words.split()
#         for word in words:
#             if len(self._paragraph[-1] + f' {word}') > self._size:
#                 self._paragraph.append('')
#             self._paragraph[-1] = (self._paragraph[-1] + f' {word}').lstrip()

#     @abstractmethod
#     def end(self):
#         pass


# class LeftParagraph(Paragraph):
#     def end(self):
#         for line in self._paragraph:
#             print(line)
#         self._paragraph = ['']


# class RightParagraph(Paragraph):
#     def end(self):
#         for line in self._paragraph:
#             print(line.rjust(self._size))
#         self._paragraph = ['']