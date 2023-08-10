<h2 style="text-align:center">Классы Summator и подклассы</h2>


### 1. Реализуйте класс Summator, описывающий объект, вычисляющий сумму натуральных чисел от 1 до n:
* 1+2+3+...+n
#### При создании экземпляра класс не должен принимать никаких аргументов.
#### Класс Summator должен иметь один метод экземпляра:
* total() — метод, принимающий в качестве аргумента целое число n и возвращающий сумму целых чисел от 1 до n включительно
### 2. Помимо этого, реализуйте класс SquareSummator, наследника класса Summator, описывающий объект, вычисляющий сумму квадратов натуральных чисел от 1 до n:
* 1^2+2^2+3^2+...+n^2
#### Процесс создания экземпляра класса SquareSummator должен совпадать с процессом создания экземпляра класса Summator.
#### Класс SquareSummator должен иметь один метод экземпляра:
* total() — метод, принимающий в качестве аргумента целое число n и возвращающий сумму квадратов целых чисел от 1 до n включительно
### 3. Также реализуйте класс QubeSummator, наследника класса Summator, описывающий объект, вычисляющий сумму кубов натуральных чисел от 1 до n:
* 1^3+2^3+3^3+...+n^3
#### Процесс создания экземпляра класса QubeSummator должен совпадать с процессом создания экземпляра класса Summator.
#### Класс QubeSummator должен иметь один метод экземпляра:
* total() — метод, принимающий в качестве аргумента целое число n и возвращающий сумму кубов целых чисел от 1 до n включительно
### 4. Наконец, реализуйте класс CustomSummator, наследника класса Summator, описывающий объект, вычисляющий сумму произвольных степеней натуральных чисел от 1 до n:
* 1^m+2^m+3^m+...+n^m
#### При создании экземпляра класс должен принимать один аргумент:
* m — степень чисел в последовательности
#### Класс CustomSummator должен иметь один метод экземпляра:
* total() — метод, принимающий в качестве аргумента целое число n и возвращающий сумму целых чисел в степени m от 1 до n включительно

##### Примечание 1. Попытайтесь реализовать классы таким образом, чтобы метод total() был определен лишь в классе Summator.
##### Примечание 2. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.
##### Примечание 3. Никаких ограничений касательно реализации классов нет, она может быть произвольной.

<table align="center">
  <tbody>
    <tr>
      <th>Sample Input 1: </th>
      <th>Sample Input 2: </th>
      <th>Sample Input 3: </th>
    </tr>
    <tr>
      <td align="center">print(issubclass(SquareSummator, Summator))<br>
                        print(issubclass(QubeSummator, Summator))<br></td>
      <td align="center">summator1 = Summator()<br>
                          summator2 = SquareSummator()<br>
                          summator3 = QubeSummator()<br>
                          print(summator1.total(3))    # 1 + 2 + 3<br>
                          print(summator2.total(3))    # 1 + 4 + 9<br>
                          print(summator3.total(3))    # 1 + 8 + 27<br></td>
      <td align="center">summator1 = Summator()<br>
                        summator2 = CustomSummator(2)<br>
                        summator3 = CustomSummator(3)<br>
                        print(summator1.total(3))    # 1 + 2 + 3<br>
                        print(summator2.total(3))    # 1 + 4 + 9<br>
                        print(summator3.total(3))    # 1 + 8 + 27<br></td>
    </tr>
    <tr>
      <td>Sample Output 1:</td>
      <td>Sample Output 2:</td>
      <td>Sample Output 3:</td>
      </tr>
    <tr>
      <td align="center">
                        True<br>
                        True<br>
      </td>
      <td align="center">
                        6<br>
                        14<br>
                        36<br>
      </td>
      <td align="center">
                        6<br>
                        14<br>
                        36<br>
      </td>
    </tr>
  </tbody>
</table>



## Примеры решений:
* Первый вариант решения
```python
class Summator:
    def total(self, n):
        return sum([i for i in range(n+1)])


class SquareSummator(Summator):
    def total(self, n):
        return sum([i**2 for i in range(n+1)])


class QubeSummator(Summator):
    def total(self, n):
        return sum([i**3 for i in range(n+1)])


class CustomSummator(Summator):
    def __init__(self, m):
        self.m = m

    def total(self, n):
        return sum([i**self.m for i in range(n+1)])
```
* Второй вариант решения

```python
class Summator:
    def transform(self, n):
        return n
    
    def total(self, n):
        return sum(self.transform(i) for i in range(1, n + 1))
    
class SquareSummator(Summator):
    def transform(self, n):
        return n ** 2
    
class QubeSummator(Summator):
    def transform(self, n):
        return n ** 3
    
class CustomSummator(Summator):
    def __init__(self, power):
        self.power = power
    
    def transform(self, n):
        return n ** self.power
```


