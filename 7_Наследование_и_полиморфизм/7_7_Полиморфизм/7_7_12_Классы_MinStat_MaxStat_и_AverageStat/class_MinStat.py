''' Первый вариант решения'''
class MinStat:
    def __init__(self, iterable=[]):
        self.iterable = iterable

    def add(self, item):
        self.iterable.append(item)

    def result(self):
        if self.iterable:
            return min(self.iterable)
        return None

    def clear(self):
        self.iterable.clear()


class MaxStat(MinStat):
    def result(self):
        if self.iterable:
            return max(self.iterable)
        return None


class AverageStat(MinStat):
    def result(self):
        if self.iterable:
            return sum(self.iterable) / len(self.iterable)
        return None
''' Второй вариант решения'''    
# import statistics
# from abc import ABC, abstractmethod


# class Stat(ABC):
#     def __init__(self, iterable=()):
#         self.data = list(iterable)

#     def add(self, n):
#         self.data.append(n)

#     def clear(self):
#         self.data.clear()

#     @abstractmethod
#     def result(self):
#         pass


# class MinStat(Stat):
#     def result(self):
#         return min(self.data, default=None)


# class MaxStat(Stat):
#     def result(self):
#         return max(self.data, default=None)


# class AverageStat(Stat):
#     def result(self):
#         return statistics.fmean(self.data) if self.data else None