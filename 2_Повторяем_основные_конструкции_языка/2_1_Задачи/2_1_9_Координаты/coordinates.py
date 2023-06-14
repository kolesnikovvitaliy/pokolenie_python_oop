''' Первый вариант решения'''
import sys

coordinates = [coordinate.strip() for coordinate in sys.stdin]

date = [[*list(map(lambda k: float(k),coordinate[1:-1].split(", ")))] for coordinate in coordinates]

for x, y in date:
    if abs(x) <= 90 and abs(y) <= 180:
        print(True)
    else:
        print(False)
    
''' Второй вариант решения '''
# import sys

# axis = [eval(line.strip()) for line in sys.stdin]
# for x, y in axis:
#     print(-90 <= x <= 90 and -180 <= y <= 180)