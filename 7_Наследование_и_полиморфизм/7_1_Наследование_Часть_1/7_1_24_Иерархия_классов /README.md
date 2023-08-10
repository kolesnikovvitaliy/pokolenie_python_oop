<h2 style="text-align:center">Иерархия классов</h2>

### С помощью наследования и приведенной ниже схемы постройте иерархию пустых классов, описывающих геометрические фигуры:

<div>
<img align="center" src="https://github.com/kolesnikovvitaliy/pokolenie_python_oop/blob/main/7_Наследование_и_полиморфизм/7_1_Наследование_Часть_1/7_1_24_Иерархия_классов/img/task.png" title="Git" **alt="Git">
​</div>


<table align="center">
  <tbody>
    <tr>
      <th>Sample Input 1: </th>
      <th>Sample Input 2: </th>
    </tr>
    <tr>
      <td align="center">print(issubclass(Circle, Shape))<br>
                          print(issubclass(Polygon, Shape))<br></td>
      <td align="center">print(issubclass(Triangle, Polygon))<br>
                          print(issubclass(IsoscelesTriangle, Triangle))<br>
                          print(issubclass(EquilateralTriangle, Triangle))<br></td>
    </tr>
    <tr>
      <td>Sample Output 1:</td>
      <td>Sample Output 2:</td>
      </tr>
    <tr>
      <td align="center">
                        True<br>
                        True<br>
      </td>
      <td align="center">
                        True<br>
                        True<br>
                        True<br>
      </td>
    </tr>
  </tbody>
</table>



## Примеры решений:
* Первый вариант решения
```python
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

```
* Второй вариант решения

```python
class Shape: ...
class Circle(Shape): ...
class Polygon(Shape): ...
class Triangle(Polygon): ...
class IsoscelesTriangle(Triangle): ...
class EquilateralTriangle(Triangle): ...
class Quadrilateral(Polygon): ...
class Parallelogram(Quadrilateral): ...
class Rectangle(Parallelogram): ...
class Square(Rectangle): ...
```


