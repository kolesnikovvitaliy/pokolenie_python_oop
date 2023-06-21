''' Первый вариант решения'''
class Todo:
    def __init__(self):
        self.things = []
        self.low_priority = 0
        self.high_priority = 0

    def add(self, name, n):
        self.things.append((name, n))
        self.low_priority = min(map(lambda y: y[1], self.things))
        self.high_priority = max(map(lambda y: y[1], self.things))


    def get_by_priority(self, n):
        return list(map(lambda y: y[0], filter(lambda x: x if n in x else [], self.things)))

    def get_low_priority(self):
        return list(map(lambda y: y[0], filter(lambda x: self.low_priority in x, self.things)))

    def get_high_priority(self):
        return list(map(lambda y: y[0], filter(lambda x: self.high_priority in x, self.things)))


''' Второй вариант решения'''    
# class Todo:
#     def __init__(self):
#         self.things = []

#     def add(self, thing, priority):
#         self.things.append((thing, priority))

#     def get_by_priority(self, priority):
#         return [t for t, p in self.things if p == priority]

#     def get_low_priority(self):
#         priority = min(map(lambda t: t[1], self.things)) if self.things else None
#         return self.get_by_priority(priority)

#     def get_high_priority(self):
#         priority = max(map(lambda t: t[1], self.things)) if self.things else None
#         return self.get_by_priority(priority)