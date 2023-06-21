<h2 style="text-align:center">Класс Numbers</h2>

### Реализуйте класс Numbers, описывающий изначально пустой расширяемый набор целых чисел. При создании экземпляра класс не должен принимать никаких аргументов.
#### Класс Numbers должен иметь три метода экземпляра:
* add_number() — метод, принимающий в качестве аргумента целое число и добавляющий его в набор
* get_even() — метод, возвращающий список всех четных чисел из набора
* get_odd() — метод, возвращающий список всех нечетных чисел из набора
##### Примечание 1. Числа в списках, возвращаемых методами get_even() и get_odd(), должны располагаться в том порядке, в котором они были добавлены в набор.
##### Примечание 2. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.

<table align="center">
  <tbody>
    <tr>
      <th>Sample Input 1: </th>
      <th>Sample Input 2: </th>
      <th>Sample Input 3: </th>
    </tr>
    <tr>
      <td align="center">numbers = Numbers()<br>
                        print(numbers.get_even())<br>
                        print(numbers.get_odd())<br></td>
      <td align="center">numbers = Numbers()<br>
                          numbers.add_number(3)<br>
                          numbers.add_number(2)<br>
                          numbers.add_number(1)<br>
                          numbers.add_number(4)<br>
                          print(numbers.get_even())<br>
                          print(numbers.get_odd())<br></td>
      <td align="center">numbers = Numbers()<br>
                          numbers.add_number(1)<br>
                          numbers.add_number(3)<br>
                          numbers.add_number(1)<br>
                          print(numbers.get_even())<br>
                          print(numbers.get_odd())<br></td>
    </tr>
    <tr>
      <td>Sample Output 1:</td>
      <td>Sample Output 2:</td>
      <td>Sample Output 3:</td>
      </tr>
    <tr>
      <td align="center">
      []<br>
      []<br>
      </td>
      <td align="center">
                       [2, 4]<br>
                       [3, 1]<br>
      </td>
      <td align="center">
                       []<br>
                       [1, 3, 1]<br>
      </td>
    </tr>
  </tbody>
</table>



## Примеры решений:
* Первый вариант решения
```python
class Numbers:
    def __init__(self):
        self.lst = []

    def add_number(self, n):
        self.lst.append(n)

    def get_even(self):
        return [i for i in self.lst if i % 2 == 0]

    def get_odd(self):
        return [i for i in self.lst if i % 2 != 0]
```
* Второй вариант решения
```python
class Numbers:
    def __init__(self):
        self.numbers = []
        
    def add_number(self, number):
        self.numbers.append(number)
        
    def get_even(self):
        return list(filter(lambda x: not x % 2, self.numbers))

    def get_odd(self):
        return list(filter(lambda x: x % 2, self.numbers))
```


