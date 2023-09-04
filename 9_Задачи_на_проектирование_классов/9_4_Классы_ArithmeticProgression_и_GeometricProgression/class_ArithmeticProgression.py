''' Первый вариант решения'''
class ArithmeticProgression:
    def __init__(self, first, d):
        self.first = first
        self.d = d
        self.flag = True

    def __iter__(self):
        return self

    def __next__(self):
        res = self.first
        self.first += self.d
        return res


class GeometricProgression(ArithmeticProgression):
    def __next__(self):
        res = self.first
        self.first *= self.d
        return res
''' Второй вариант решения'''    
from abc import ABC, abstractmethod


class Progression(ABC):
    def __init__(self, start, step):
        self._current = start
        self._step = step

    def __iter__(self):
        return self

    @abstractmethod
    def __next__(self):
        pass


class ArithmeticProgression(Progression):
    def __next__(self):
        answer = self._current
        self._current += self._step
        return answer


class GeometricProgression(Progression):
    def __next__(self):
        answer = self._current
        self._current *= self._step
        return answer