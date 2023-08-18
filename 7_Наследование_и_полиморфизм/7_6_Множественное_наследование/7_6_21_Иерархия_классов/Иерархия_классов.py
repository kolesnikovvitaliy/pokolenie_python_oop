''' Первый вариант решения'''
class A:
    pass


class B(A):
    pass


class D(A):
    pass


class C(A):
    pass


class E(B, D):
    pass
''' Второй вариант решения'''    
# class A: ...

# class B(A): ...
# class C(A): ...
# class D(A): ...

# class E(B, D): ...