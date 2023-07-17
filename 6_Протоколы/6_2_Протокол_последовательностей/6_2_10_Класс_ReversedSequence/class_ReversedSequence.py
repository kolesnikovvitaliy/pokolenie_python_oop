''' Первый вариант решения'''
class ReversedSequence:
    def __init__(self, sequence):
        self.sequence = sequence

    def __getitem__(self, key):
        return list(reversed(self.sequence))[key]     

    def __iter__(self):
        yield from reversed(self.sequence)

    def __len__(self):
        return len(self.sequence)
    
    def __reversed__(self):
        return self.sequence
''' Второй вариант решения'''    
# class ReversedSequence:
#     def __init__(self, sequence):
#         self.sequence = sequence

#     def __len__(self):
#         return len(self.sequence)

#     def __getitem__(self, key):
#         return self.sequence[~key]

#     def __iter__(self):
#         yield from reversed(self.sequence)