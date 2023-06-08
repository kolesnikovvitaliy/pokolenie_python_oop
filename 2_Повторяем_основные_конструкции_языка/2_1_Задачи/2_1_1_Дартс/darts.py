'''
Sample Input 3:           Sample Input :               Sample Input 5:
3                         4                            5
Sample Input 3:           Sample Input 4:              Sample Input 5:

1 1 1                     1 1 1 1                      1 1 1 1 1
1 2 1                     1 2 2 1                      1 2 2 2 1
1 1 1                     1 2 2 1                      1 2 3 2 1
                          1 1 1 1                      1 2 2 2 1             
                                                       1 1 1 1 1
'''

def make_dartboard_1(n):
    dartboard = []
    for i in range(n):
        result =[]
        for j in range(n):            
            if (i == j and i <= n - 1 - j) or (i <= j and i <= n - 1 - j):
                result.append(i+1)
            elif (i >= j and i <= n - 1 - j):
                result.append(j+1)
            elif (i <= j and i >= n - 1 - j):
                result.append(n - j)
            elif (i >= j and i >= n - 1 - j):
                result.append(n-i)
            else:
                result.append(1)
        dartboard.append(result)
    return dartboard

dartboard_1 = make_dartboard_1(int(input()))

for line in dartboard_1:
    print(*line)

# Второй вариант решения:
# def make_dartboard_2(n):
#     mat = [[1] * n for _ in range(n)]
#     for i in range(n):
#         for j in range(n):
#             mat[i][j] = min(i + 1, j + 1, n - i, n - j)
#     return mat

# dartboard_2 = make_dartboard_2(int(input()))

# for line in dartboard_2:
#     print(*line)
