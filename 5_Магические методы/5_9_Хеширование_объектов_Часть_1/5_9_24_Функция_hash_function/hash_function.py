''' Первый вариант решения'''
def hash_function(obj):
    a = str(obj)
    temp2 = 0
    temp1 = 0

    if len(a) % 2 == 0:
        temp1 = sum(ord(a[i]) * ord(a[-i-1]) for i in range(int(len(a)/2)))
    else:
        temp1 = sum(ord(a[i]) * ord(a[-i-1]) for i in range(int(len(a)/2))) + ord(a[int(len(a)/2)])

    for k,v in enumerate(a, 1):
        if k % 2 != 0:
            temp2 += ord(v)*k
        else:
            temp2 -= ord(v)*k
       
    return (temp1 * temp2) % 123456791
''' Второй вариант решения'''    
# def hash_function(obj):
#     obj = str(obj)
#     temp1 = temp2 = 0
#     for i in range(len(obj) // 2):
#         temp1 += ord(obj[i]) * ord(obj[-(i + 1)])
#     if len(obj) % 2:
#         temp1 += ord(obj[len(obj) // 2])
#     for i, c in enumerate(obj, 1):
#         temp2 += ord(c) * i * ((-1) ** (i + 1))
#     return temp1 * temp2 % 123456791