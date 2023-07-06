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


matrix = Matrix(2, 3, 1)

print(matrix)
print()
print(-matrix)
print()
print(~matrix)

