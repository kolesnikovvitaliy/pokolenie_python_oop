''' Первый вариант решения'''
class Counter:
    def __init__(self, start: int = 0):
        self.value = start

    def inc(self, n=None):
        if n:
            self.value += n
        else:
            self.value += 1

    def dec(self, n=None):
        if n:
            self.value -= n
        else:
            self.value -= 1
        if self.value < 0:
            self.value = 0


class NonDecCounter(Counter):
    def dec(self, n=None):
        ...


class LimitedCounter(Counter):
    def __init__(self, start: int = 0, limit: int = 10):
        super().__init__(start)
        self.__limit = limit

    def inc(self, n=None):
        if self.value < self.__limit:
            if n:
                self.value += n
            else:
                self.value += 1
            if self.value > self.__limit:
                self.value = self.__limit
''' Второй вариант решения'''    
# class Counter:
#     def __init__(self, start=0):
#         self.value = start

#     def inc(self, n=1):
#         self.value += n

#     def dec(self, n=1):
#         self.value = max(self.value - n, 0)


# class NonDecCounter(Counter):
#     def dec(self, n=1):
#         return None


# class LimitedCounter(Counter):
#     def __init__(self, start=0, limit=10):
#         Counter.__init__(self, start)
#         self.limit = limit

#     def inc(self, n=1):
#         self.value = min(self.value + n, self.limit)