''' Первый вариант решения'''
class Shape:
    pass


class Polygon(Shape):
    pass


class Circle(Shape):
    pass


class Quadrilateral(Polygon):
    pass


class Triangle(Polygon):
    pass


class Parallelogram(Quadrilateral):
    pass


class IsoscelesTriangle(Triangle):
    pass


class EquilateralTriangle(Triangle):
    pass


class Rectangle(Parallelogram):
    pass


class Square(Rectangle):
    pass

''' Второй вариант решения'''    
# class Shape: ...
# class Circle(Shape): ...
# class Polygon(Shape): ...
# class Triangle(Polygon): ...
# class IsoscelesTriangle(Triangle): ...
# class EquilateralTriangle(Triangle): ...
# class Quadrilateral(Polygon): ...
# class Parallelogram(Quadrilateral): ...
# class Rectangle(Parallelogram): ...
# class Square(Rectangle): ...