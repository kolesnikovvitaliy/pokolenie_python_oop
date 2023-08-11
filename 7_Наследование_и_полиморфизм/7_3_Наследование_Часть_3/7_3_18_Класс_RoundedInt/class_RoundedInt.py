''' Первый вариант решения'''
class RoundedInt(int):
    def __new__(cls, num, even=True):
        if even:
            if num % 2:
                num += 1
            else:
                num = num
        else:
            if num % 2:
                num = num
            else:
                num += 1
        obj = super().__new__(cls, num)
        obj.even = even
        return obj
''' Второй вариант решения'''    
# class RoundedInt(int):
#     def __new__(cls, value, even=True, *args, **kwargs):
#         value += (value % 2 == 1) if even else (value % 2 == 0)
#         instance = super().__new__(cls, value)
#         return instance