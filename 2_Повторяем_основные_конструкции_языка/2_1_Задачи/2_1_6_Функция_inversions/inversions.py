''' Превый вариан решения'''
def inversions(sequence:list):
    count = 0
    for i in range(len(sequence)):
        for j in range(len(sequence)):
            if sequence[i] > sequence[j] and i < j:
                count += 1
    return count

''' Второй вариан решения'''

from itertools import starmap, combinations

def inversions(sp):
    return sum(starmap(lambda x, y: x > y, combinations(sp, 2)))



# sequence = [3, 1, 4, 2]
# sequence = [1, 2, 3, 4, 5]
sequence = [4, 3, 2, 1]
print(inversions(sequence))