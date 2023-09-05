''' Первый вариант решения'''
from dataclasses import dataclass, field


@dataclass
class HighScoreTable:
    _len_list_score: int = field(default=0)
    scores: list = field(default_factory=list[int], repr=False)

    def update(self, res=0):
        if len(self.scores) < self._len_list_score:
            self.scores.append(res)
        else:
            if not min(self.scores) > res:
                self.scores.pop()
                self.scores.append(res)
        self.scores = sorted(self.scores, reverse=True)

    def reset(self):
        self.scores.clear()
''' Второй вариант решения'''    
# class HighScoreTable:
#     def __init__(self, limit):
#         self._limit = limit
#         self.scores = []

#     def update(self, score):
#         length = len(self.scores)
#         for index in range(length):
#             if score > self.scores[index]:
#                 if length == self._limit:
#                     self.scores.pop()
#                 self.scores.insert(index, score)
#                 break
#         else:
#             if length < self._limit:
#                 self.scores.append(score)

#     def reset(self):
#         self.scores.clear()