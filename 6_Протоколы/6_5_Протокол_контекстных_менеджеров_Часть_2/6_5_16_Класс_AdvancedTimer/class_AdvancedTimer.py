''' Первый вариант решения'''
from time import perf_counter


class AdvancedTimer:
    def __init__(self):
        self.hisory_run = []
        self.runs = self.hisory_run
        self.last_run = None
        self.max = None
        self.min = None

    def __enter__(self):
        self._start = perf_counter()
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        self.result = perf_counter() - self._start
        self.hisory_run.append(self.result)
        self.last_run = self.hisory_run[-1]
        self.runs = self.hisory_run
        self.max = max(self.hisory_run)
        self.min = min(self.hisory_run)
        return True
''' Второй вариант решения'''    
# import time

# class AdvancedTimer:
#     def __init__(self):
#         self.runs = []
#         self.last_run = self.min = self.max = None

#     def __enter__(self):
#         self.start = time.perf_counter()
#         return self

#     def __exit__(self, *args, **kwargs):
#         self.last_run = time.perf_counter() - self.start
#         self.runs.append(self.last_run)
#         self.min = min(self.runs)
#         self.max = max(self.runs)