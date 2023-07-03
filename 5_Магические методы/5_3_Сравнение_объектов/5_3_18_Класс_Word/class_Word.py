''' Первый вариант решения'''
from functools import total_ordering

@total_ordering
class Word:
    def __init__(self, text: str) -> None:
        self.words = text

    def __str__(self) -> str:
        return f'{self.words.capitalize()}'

    def __repr__(self) -> str:
        return f"{__class__.__name__}('{self.words}')"
    
    def __eq__(self, __value: object) -> bool:
        if isinstance(__value, Word):
            return len(self.words) == len(__value.words)
        return NotImplemented

    def __gt__(self, __value: object) -> bool:
        if isinstance(__value, Word):
            return len(self.words) > len(__value.words)
        return NotImplemented
''' Второй вариант решения'''    
# from functools import total_ordering
# @total_ordering
# class Word:
#     def __init__(self, word: str):
#         self.word = word

#     def __repr__(self):
#         return f"{type(self).__name__}('{self.word}')"

#     def __str__(self):
#         return self.word.title()

#     def __eq__(self, other):
#         if isinstance(other, Word):
#             return len(self.word) == len(other.word)
#         return NotImplemented

#     def __lt__(self, other):
#         if isinstance(other, Word):
#             return len(self.word) < len(other.word)
#         return NotImplemented