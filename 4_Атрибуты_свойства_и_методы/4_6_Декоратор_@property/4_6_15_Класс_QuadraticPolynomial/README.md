<h2 style="text-align:center">Класс QuadraticPolynomial</h2>

<div>
<img align="center" src="https://github.com/kolesnikovvitaliy/pokolenie_python_oop/blob/main/4_Атрибуты_свойства_и_методы/4_6_Декоратор_@property/4_6_15_Класс_QuadraticPolynomial/img/task_1.png" title="Git" **alt="Git">
​</div>

### Реализуйте класс QuadraticPolynomial, описывающий квадратный трехчлен. При создании экземпляра класс должен принимать три аргумента в следующем порядке:
* a — коэффициент a квадратного трехчлена
* b — коэффициент b квадратного трехчлена
* c — коэффициент c квадратного трехчлена

#### Экземпляр класса QuadraticPolynomial должен иметь три атрибута:
* a — коэффициент a квадратного трехчлена
* b — коэффициент b квадратного трехчлена
* c — коэффициент c квадратного трехчлена
#### Класс QuadraticPolynomial должен иметь четыре свойства:
* x1 — свойство, доступное только для чтения, возвращающее корень квадратного трехчлена, вычисленный по формуле:

<div>
<img align="center" src="https://github.com/kolesnikovvitaliy/pokolenie_python_oop/blob/main/4_Атрибуты_свойства_и_методы/4_6_Декоратор_@property/4_6_15_Класс_QuadraticPolynomial/img/task_2.png" title="Git" **alt="Git">
​</div>

* x2 — свойство, доступное только для чтения, возвращающее корень квадратного трехчлена, вычисленный по формуле:

<div>
<img align="center" src="https://github.com/kolesnikovvitaliy/pokolenie_python_oop/blob/main/4_Атрибуты_свойства_и_методы/4_6_Декоратор_@property/4_6_15_Класс_QuadraticPolynomial/img/task_3.png" title="Git" **alt="Git">
​</div>

* view — свойство, доступное только для чтения, возвращающее строку вида:
> ax^2 + bx + c 
> 
> где a, b и с представляют коэффициенты квадратного трехчлена

* coefficients — свойство, доступное для чтения и записи, возвращающее кортеж вида:
> (a, b, c)
>
> где a, b и с представляют коэффициенты квадратного трехчлена

##### Примечание 1. Если квадратный трехчлен имеет лишь один корень, значения свойств x1 и x2 должны совпадать.
##### Примечание 2. При изменении коэффициентов квадратного трехчлена через соответствующие атрибуты или свойство coefficients значения свойств x1, x2, view и coefficients также должны изменяться.
##### Примечание 3. Если какие-либо коэффициенты квадратного трехчлена равны нулю, они по-прежнему должны присутствовать в строке, возвращаемой свойством view, дополнительно их убирать не нужно.
##### Примечание 4. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.
##### Примечание 5. Никаких ограничений касательно реализации класса QuadraticPolynomial нет, она может быть произвольной.

<table align="center">
  <tbody>
    <tr>
      <th>Sample Input 1: </th>
      <th>Sample Input 2: </th>
      <th>Sample Input 3: </th>
    </tr>
    <tr>
      <td align="center">polynom = QuadraticPolynomial(1, 2, -3)<br>
                        print(polynom.a)<br>
                        print(polynom.b)<br>
                        print(polynom.c)<br></td>
      <td align="center">polynom = QuadraticPolynomial(1, 2, -3)<br>
                          print(polynom.x1)<br>
                          print(polynom.x2)<br></td>
      <td align="center">polynom = QuadraticPolynomial(1, 2, -3)<br>
                          print(polynom.view)<br>
                          print(polynom.coefficients)<br></td>
    </tr>
    <tr>
      <td>Sample Output 1:</td>
      <td>Sample Output 2:</td>
      <td>Sample Output 3:</td>
      </tr>
    <tr>
      <td align="center">
                        1<br>
                        2<br>
                        -3<br>
      </td>
      <td align="center">
                        -3.0<br>
                        1.0<br>
      </td>
      <td align="center">
                        1x^2 + 2x - 3<br>
                        (1, 2, -3)<br>
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
        self.__d = (self.b ** 2) - (4 * self.a * self.c)
        

    @property
    def x1(self):
        if self.__d >= 0:
            return (-self.b - pow(((self.b**2) - (4 * self.a * self.c)), 0.5)) / (2 * self.a)
    
    @property
    def x2(self):
        if self.__d >= 0:
            return (-self.b + pow(((self.b**2) - (4 * self.a * self.c)), 0.5)) / (2 * self.a)
        else:
            return None
        
    @property    
    def view(self):
        return str(self.a) + 'x^2' +  str(*[' + ' if self.b >= 0 else ' - ']) + str(abs(self.b)) + 'x' + str(*[' + ' if self.c >= 0 else ' - ']) + str(abs(self.c))
    
    @property
    def coefficients(self):
        return (self.a, self.b, self.c)
    
    @coefficients.setter
    def coefficients(self, coefficients):
        self.a, self.b, self.c = coefficients
        self.__d = (self.b ** 2) - (4 * self.a * self.c)
```
* Второй вариант решения

```python
class QuadraticPolynomial:
    def __init__(self, a, b, c):
        self.a, self.b, self.c = a, b, c

    @property
    def d(self):
        return self.b ** 2 - 4 * self.a * self.c

    @property
    def x1(self):
        return (-self.b - self.d ** 0.5) / (2 * self.a) if self.d >= 0 else None

    @property
    def x2(self):
        return (-self.b + self.d ** 0.5) / (2 * self.a) if self.d >= 0 else None

    @property
    def view(self):
        b, sign_b = abs(self.b), '-' if self.b < 0 else '+'
        c, sign_c = abs(self.c), '-' if self.c < 0 else '+'
        return f'{self.a}x^2 {sign_b} {b}x {sign_c} {c}'

    @property
    def coefficients(self):
        return self.a, self.b, self.c

    @coefficients.setter
    def coefficients(self, coeff):
        a, b, c = coeff
        self.a, self.b, self.c = a, b, c
```


