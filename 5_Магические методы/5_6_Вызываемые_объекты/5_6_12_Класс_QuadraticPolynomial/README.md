<h2 style="text-align:center">Класс QuadraticPolynomial</h2>

### Реализуйте класс QuadraticPolynomial, описывающий квадратный трехчлен. При создании экземпляра класс должен принимать три аргумента в следующем порядке:
* a — коэффициент a квадратного трехчлена
* b — коэффициент b квадратного трехчлена
* c — коэффициент c квадратного трехчлена
#### Экземпляр класса QuadraticPolynomial должен являться вызываемым объектом и принимать один аргумент:
* x — число

<div>
<img align="center" src="https://github.com/kolesnikovvitaliy/pokolenie_python_oop/blob/main/5_Магические методы/5_6_Вызываемые_объекты/5_6_12_Класс_QuadraticPolynomial/img/task.png" title="Git" **alt="Git">
​</div>

##### Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.
##### Примечание 2. Никаких ограничений касательно реализации класса QuadraticPolynomial нет, она может быть произвольной.

<table align="center">
  <tbody>
    <tr>
      <th>Sample Input 1: </th>
      <th>Sample Input 2: </th>
    </tr>
    <tr>
      <td align="center">func = QuadraticPolynomial(1, 2, 1)<br>
                          print(func(1))<br>
                          print(func(2))<br></td>
      <td align="center">func = QuadraticPolynomial(1, 3, 4)<br>
                          print(func(1))<br>
                          print(func(2))<br></td>
    </tr>
    <tr>
      <td>Sample Output 1:</td>
      <td>Sample Output 2:</td>
      </tr>
    <tr>
      <td align="center">
                        4<br>
                        9<br>
      </td>
      <td align="center">
                        8<br>
                        14<br>
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
    
    def __call__(self, x):
        return self.a*x**2 + self.b*x + self.c
```
* Второй вариант решения

```python
class QuadraticPolynomial:
    def __init__(self, a, b, c):
        self.a, self.b, self.c = a, b, c
        
    def __call__(self, x):
        return self.a * (x ** 2) + self.b * x + self.c
```


