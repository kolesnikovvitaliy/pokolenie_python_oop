''' Первый вариант решения'''
class Matrix:
    def __init__(self, rows, cols, value=0):
        self.rows = rows
        self.cols = cols
        self.__value = value
        if type(self.__value) is int:
            self.__matrix = [[value for j in range(cols)] for i in range(rows)]
        else:
            self.set_value(self.rows, self.cols, self.__value)        

    def get_value(self, rows, cols):
        return self.__matrix[rows][cols]

    def set_value(self, rows, cols, value=0):
        if type(value) is int or type(value) is float:
            self.__matrix[rows][cols] = value
        else:
            self.__matrix = [[0 for j in range(cols)] for i in range(rows)]
            for i in range(len(value)):
                for j in range(len(value[0])):
                    self.__matrix[i][j] = value[i][j]
        return self.__matrix[-1]        

    def __str__(self) -> str:
        __str = ''
        for i in self.__matrix:
            __str += ' '.join(map(str,i)) + '\n'
        return __str.strip()           
        
    def __repr__(self) -> str:
        return f"{__class__.__name__}({self.rows}, {self.cols})"
    
    def __pos__(self):
        return __class__(self.rows, self.cols, self.__value)

    def __neg__(self):
        return __class__(self.rows, self.cols, [[-i for i in v] for v in self.__matrix])
    
    def __invert__(self):
        self.__m = [[0 for j in range(len(self.__matrix))] for i in range(len(self.__matrix[0]))]
        for i in range(len(self.__matrix)):
            for j in range(len(self.__matrix[0])):
                self.__m[j][i] = self.__matrix[i][j]
                
        return __class__(len(self.__m), len(self.__m[0]), self.__m)
    
    def __round__(self, round_volue=0):
        return __class__(self.rows, self.cols, [[round(i, round_volue) for i in  v] for v in self.__matrix])


''' Второй вариант решения'''    
# class Matrix:
#     def __init__(self, rows, cols, value=0):
#         self.rows = rows
#         self.cols = cols
#         self.value = value
#         self.matrix = [[value] * cols for _ in range(rows)]

#     def get_value(self, row, col):
#         return self.matrix[row][col]

#     def set_value(self, row, col, value):
#         self.matrix[row][col] = value

#     def _create_matrix_instance(self, rows, cols, sign=1, do_transpose=False, do_round=False, n=None):
#         matrix = Matrix(rows, cols)
#         for row in range(rows):
#             for col in range(cols):
#                 r, c = (col, row) * do_transpose or (row, col)
#                 value = round(self.get_value(r, c) * sign, n) * do_round or self.get_value(r, c) * sign
#                 matrix.set_value(row, col, value)
#         return matrix

#     def __str__(self):
#         string_matrix = [' '.join(map(str, item)) for item in self.matrix]
#         return '\n'.join(string_matrix)

#     def __repr__(self):
#         return f'Matrix({self.rows}, {self.cols})'

#     def __pos__(self):
#         return self._create_matrix_instance(self.rows, self.cols)

#     def __neg__(self):
#         return self._create_matrix_instance(self.rows, self.cols, sign=-1)

#     def __invert__(self):
#         return self._create_matrix_instance(self.cols, self.rows, do_transpose=True)

#     def __round__(self, n=None):
#         return self._create_matrix_instance(self.rows, self.cols, do_round=True, n=n)