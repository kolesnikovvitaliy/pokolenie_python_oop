''' Первый вариант решения'''
class DevelopmentTeam:
    def __init__(self):
        self.__lst_junior = []
        self.__lst_senior = []

    def add_junior(self, *args):
        for i in args:
            self.__lst_junior.append((i, 'junior'))
        
    def add_senior(self, *args):
        for i in args:
            self.__lst_senior.append((i, 'senior'))

    def __iter__(self):
        yield from (self.__lst_junior + self.__lst_senior)
''' Второй вариант решения'''    
# class DevelopmentTeam:
#     def __init__(self):
#         self._seniors = []
#         self._juniors = []
        
#     def add_junior(self, *juniors):
#         self._juniors.extend(juniors)
        
#     def add_senior(self, *seniors):
#         self._seniors.extend(seniors)
        
#     def __iter__(self):
#         for junior in self._juniors:
#             yield (junior, 'junior')
#         for senior in self._seniors:
#             yield (senior, 'senior')