''' Первый вариант решения'''
from copy import deepcopy


class Selfie:
    def __init__(self):
        self._history = []

    def save_state(self):
        self._history.append(deepcopy(self))

    def recover_state(self, n):
        if len(self._history) > n:
            return self._history[n]
        return self

    def n_states(self):
        return len(self._history)
''' Второй вариант решения'''    
# from copy import deepcopy


# class Selfie:
#     def __init__(self):
#         self.states = {}

#     def save_state(self):
#         self.states[len(self.states)] = deepcopy(self)

#     def recover_state(self, n):
#         return self.states[n] if n in self.states else self

#     def n_states(self):
#         return len(self.states)