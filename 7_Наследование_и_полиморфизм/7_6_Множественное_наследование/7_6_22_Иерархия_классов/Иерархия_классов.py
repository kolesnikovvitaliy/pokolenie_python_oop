''' Первый вариант решения'''
class H:
    pass


class D(H):
    pass


class E(H):
    pass


class F(H):
    pass


class G(H):
    pass


class B(D, E):
    pass


class C(F, G):
    pass


class A(B, C):
    pass
''' Второй вариант решения'''    
# class H: ...

# class D(H): ...
# class E(H): ...
# class F(H): ...
# class G(H): ...

# class B(D, E): ...
# class C(F, G): ...

# class A(B, C): ...