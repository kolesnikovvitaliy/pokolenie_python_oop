''' Первый вариант решения'''
def limited_hash(left, right, hash_function=hash):
    def wrapper(obj):
        res  = hash_function(obj)
        while res not in range(left, right+1):
            if res > right:
                res =  left + res-right-1
            elif res < left:
                res = right + res- left + 1
        return res
    return wrapper
''' Второй вариант решения'''    
# def limited_hash(left, right, hash_function=hash):
#     def inner_hash_function(x):
#         return left + (hash_function(x) - left) % (right - left + 1)
#     return inner_hash_function