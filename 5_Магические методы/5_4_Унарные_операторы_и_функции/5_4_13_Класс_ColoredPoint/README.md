<h2 style="text-align:center">Класс ColoredPoint</h2>


### Реализуйте класс ColoredPoint, описывающий цветную точку на плоскости. При создании экземпляра класс должен принимать три аргумента в следующем порядке:
* x — координата точки по оси x
* y — координата точки по оси y
* color — цвет в формате RGB, представленный кортежем из трех целых чисел в диапазоне [0; 255], по умолчанию имеет значение (0, 0, 0)

#### Экземпляр класса ColoredPoint должен иметь три атрибута:
* x — координата точки по оси x
* y — координата точки по оси y
* color — цвет в формате RGB, представленный кортежем из трех целых чисел от 0 до 255
#### Также экземпляр класса ColoredPoint должен иметь следующее формальное строковое представление:
> ColoredPoint(<координата x>, <координата y>, <цвет точки в виде трехэлементного кортежа>)
#### И следующее неформальное строковое представление:
> (<координата x>, <координата y>)

#### Наконец, экземпляр класса ColoredPoint должен поддерживать унарные операторы +, - и ~:
* результатом унарного + должен являться новый экземпляр класса ColoredPoint c исходными координатами и цветом
* результатом унарного - должен являться новый экземпляр класса ColoredPoint c координатами, умноженными на минус единицу, и исходным цветом
* результатом унарного ~ должен являться новый экземпляр класса ColoredPoint c координатами, переставленными местами, и инвертированным цветом: значение каждой компоненты цвета отнимается от 255

##### Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.
##### Примечание 2. Никаких ограничений касательно реализации класса ColoredPoint нет, она может быть произвольной.

<table align="center">
  <tbody>
    <tr>
      <th>Sample Input 1: </th>
      <th>Sample Input 2: </th>
    </tr>
    <tr>
      <td align="center">point = ColoredPoint(2, -3)<br>
                        print(+point)<br>
                        print(-point)<br>
                        print(~point)<br></td>
      <td align="center">point1 = ColoredPoint(2, -3)<br>
                        point2 = ColoredPoint(10, 20, (34, 45, 67))<br>
                        print(point1.color)<br>
                        print(point2.color)<br></td>
    </tr>
    <tr>
      <td>Sample Output 1:</td>
      <td>Sample Output 2:</td>
      </tr>
    <tr>
      <td align="center">
                        (2, -3)<br>
                        (-2, 3)<br>
                        (-3, 2)<br>
      </td>
      <td align="center">
                        (0, 0, 0)<br>
                        (34, 45, 67)<br>
      </td>
    </tr>
  </tbody>
</table>



## Примеры решений:
* Первый вариант решения
```python
class ColoredPoint:
    def __init__(self, x, y, color=(0, 0, 0, )):
        self.x = x
        self.y = y
        self.color = color

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"

    def __repr__(self) -> str:
        return f"{__class__.__name__}({self.x}, {self.y}, {self.color})"
    
    def __pos__(self):
        return __class__(self.x, self.y, self.color)
    
    def __neg__(self):
        return __class__(self.x*-1, self.y*-1, self.color)
    
    def __invert__(self):
        if self.color == (0, 0, 0):
            return __class__(self.y, self.x, self.color)
        else:
            __color = tuple(255-i for i in self.color)
            return __class__(self.y, self.x, __color)
```
* Второй вариант решения

```python
class ColoredPoint:
    def __init__(self, x, y, color=(0, 0, 0)):
        self.x = x
        self.y = y
        self.color = color
        
    def __str__(self):
        return f'({self.x}, {self.y})'
        
    def __repr__(self):
        return f'ColoredPoint({self.x}, {self.y}, {self.color})'
    
    def __pos__(self):
        return ColoredPoint(self.x, self.y, self.color)
    
    def __neg__(self):
        return ColoredPoint(-self.x, -self.y, self.color)
    
    def __invert__(self):
        return ColoredPoint(self.y, self.x, tuple(255 - c for c in self.color))
```


