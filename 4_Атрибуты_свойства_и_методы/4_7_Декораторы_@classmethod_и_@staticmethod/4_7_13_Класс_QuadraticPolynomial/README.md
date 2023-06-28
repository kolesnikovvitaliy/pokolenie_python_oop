<h2 style="text-align:center">Класс QuadraticPolynomial</h2>

<div>
<img align="center" src="https://github.com/kolesnikovvitaliy/pokolenie_python_oop/blob/main/4_Атрибуты_свойства_и_методы/4_7_Декораторы_@classmethod_и_@staticmethod/4_7_13_Класс_QuadraticPolynomial/img/task.png" title="Git" **alt="Git">
​</div>


### Реализуйте класс QuadraticPolynomial, описывающий квадратный трехчлен. При создании экземпляра класс должен принимать три аргумента в следующем порядке:
* a — коэффициент a квадратного трехчлена
* b — коэффициент b квадратного трехчлена
* c — коэффициент c квадратного трехчлена
#### Экземпляр класса QuadraticPolynomial должен иметь три атрибута:
* a — коэффициент a квадратного трехчлена
* b — коэффициент b квадратного трехчлена
* c — коэффициент c квадратного трехчлена
#### Класс QuadraticPolynomial должен иметь два метода класса:
* from_iterable() — метод, принимающий в качестве аргумента итерируемый объект из трех элементов a, b и c, которые представляют коэффициенты квадратного трехчлена, и возвращающий экземпляр класса QuadraticPolynomial, созданный на основе переданных коэффициентов
* from_str() — метод, принимающий в качестве аргумента строку, которая содержит коэффициенты a, b и c квадратного трехчлена, записанные через пробел. Метод должен возвращать экземпляр класса QuadraticPolynomial, созданный на основе переданных коэффициентов, предварительно преобразованных в экземпляры класса float 

##### Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.

<table align="center">
  <tbody>
    <tr>
      <th>Sample Input 1: </th>
      <th>Sample Input 2: </th>
      <th>Sample Input 3: </th>
    </tr>
    <tr>
      <td align="center">polynom = QuadraticPolynomial(1, -5, 6)<br>
                          print(polynom.a)<br>
                          print(polynom.b)<br>
                          print(polynom.c)<br></td>
      <td align="center">polynom = QuadraticPolynomial.from_iterable([2, 13, -1])<br>
                          print(polynom.a)<br>
                          print(polynom.b)<br>
                          print(polynom.c)<br></td>
      <td align="center">polynom = QuadraticPolynomial.from_str('-1.5 4 14.8')<br>
                        print(polynom.a)<br>
                        print(polynom.b)<br>
                        print(polynom.c)<br>
                        print(polynom.a + polynom.b + polynom.c)<br></td>
    </tr>
    <tr>
      <td>Sample Output 1:</td>
      <td>Sample Output 2:</td>
      <td>Sample Output 3:</td>
      </tr>
    <tr>
      <td align="center">
                        1<br>
                        -5<br>
                        6<br>
      </td>
      <td align="center">
                        2<br>
                        13<br>
                        -1<br>
      </td>
      <td align="center">
                        -1.5<br>
                        4.0<br>
                        14.8<br>
                        17.3<br>
      </td>
    </tr>
  </tbody>
</table>



## Примеры решений:
* Первый вариант решения
```python
class QuadraticPolynomial:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    @classmethod
    def from_iterable(cls, iterable):
        cls.a, cls.b, cls.c = iterable
        return cls

    @classmethod
    def from_str(cls, text):
        cls.a, cls.b, cls.c = map(float, text.split())
        return cls
```
* Второй вариант решения

```python
class QuadraticPolynomial:
    def __init__(self, a, b, c):
        self.a, self.b, self.c = a, b, c

    @classmethod
    def from_iterable(cls, iterable):
        return cls(*iterable)

    @classmethod
    def from_str(cls, string):
        iterable = (float(digit) for digit in string.split())
        return cls.from_iterable(iterable)
```


