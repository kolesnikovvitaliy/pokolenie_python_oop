''' Первый вариант решения'''
from dataclasses import dataclass, field


@dataclass
class Testpaper:
    topic: str = field(default='')
    correct: list = field(default_factory=list)
    percent: str = field(default='')


class Student:
    def __init__(self):
        self.tests_taken = 'No tests taken'

    def take_test(self, obj, item=list):
        if isinstance(self.tests_taken, str):
            self.tests_taken = dict()
        res = self._result(item, obj)
        self.tests_taken[obj.topic] = res

    @staticmethod
    def _result(answers_student, obj):
        _result = list(set(answers_student) & set(obj.correct))
        _result = round((len(_result) / len(obj.correct)) * 100)
        result = f'{str(_result)+"%"}'
        if _result >= int(obj.percent[:-1]):
            return f'Passed! ({result})'
        return f'Failed! ({result})'
''' Второй вариант решения'''    
# class Testpaper:
#     def __init__(self, subject, markscheme, pass_mark):
#         self.subject = subject
#         self.markscheme = markscheme
#         self.pass_mark = pass_mark


# class Student:
#     def __init__(self):
#         self.tests_taken = 'No tests taken'

#     def take_test(self, paper: Testpaper, student_answers):
#         score = len(set(paper.markscheme) & set(student_answers)) / len(paper.markscheme) * 100
#         result = 'Passed!' if score >= int(paper.pass_mark[:-1]) else 'Failed'
#         percent = f'{score:.0f}%'

#         if self.tests_taken == 'No tests taken':
#             self.tests_taken = {paper.subject: f'{result} ({percent})'}
#         else:
#             self.tests_taken[paper.subject] = f'{result} ({percent})'