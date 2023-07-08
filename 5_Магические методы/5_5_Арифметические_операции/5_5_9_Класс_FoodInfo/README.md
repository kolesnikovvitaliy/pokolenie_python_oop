<h2 style="text-align:center">Класс FoodInfo</h2>


### Реализуйте класс FoodInfo, описывающий пищевую ценность продуктов. При создании экземпляра класс должен принимать три аргумента в следующем порядке:
* proteins — количество белков в граммах
* fats — количество жиров в граммах
* carbohydrates — количество углеводов в граммах
#### Экземпляр класса FoodInfoдолжен иметь три атрибута:
* proteins — количество белков в граммах
* fats — количество жиров в граммах
* carbohydrates — количество углеводов в граммах
#### И следующее формальное строковое представление:
> FoodInfo(<количество белков>, <количество жиров>, <количество углеводов>)
#### Также экземпляры класса FoodInfo должны поддерживать между собой операцию сложения с помощью оператора +, результатом которой должен являться новый экземпляр класса FoodInfo с суммарным количеством белков, жиров и углеводов исходных экземпляров.
####   Наконец, экземпляр класса FoodInfo должен поддерживать операции умножения, деления и деления нацело на число n с помощью операторов *, / и // соответственно:
* результатом умножения должен являться новый экземпляр класса FoodInfo, количество белков, жиров и углеводов которого умножены на n
* результатом деления должен являться новый экземпляр класса FoodInfo, количество белков, жиров и углеводов которого поделены на n
* результатом деления нацело должен являться новый экземпляр класса FoodInfo, количество белков, жиров и углеводов которого поделены нацело на n
##### Примечание 1. Числами будем считать экземпляры классов int и float. Также будем гарантировать, что экземпляр класса FoodInfo всегда делится на ненулевое число.
##### Примечание 2. Если объект, с которым выполняется арифметическая операция, некорректен, метод, реализующий эту операцию, должен вернуть константу NotImplemented.
##### Примечание 3. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.
##### Примечание 4. Никаких ограничений касательно реализации класса FoodInfo нет, она может быть произвольной.

<table align="center">
  <tbody>
    <tr>
      <th>Sample Input 1: </th>
      <th>Sample Input 2: </th>
    </tr>
    <tr>
      <td align="center">food1 = FoodInfo(10, 20, 30)<br>
                          food2 = FoodInfo(10, 10, 20)<br>
                          print(food1 + food2)<br>
                          print(food1 * 2)<br>
                          print(food1 / 2)<br>
                          print(food1 // 2)<br></td>
      <td align="center">food1 = FoodInfo(10, 20, 30)<br>
                          try:<br>
                              food2 = (5, 10, 15) + food1<br>
                          except TypeError:<br>
                              print('Некорректный тип данных')<br></td>
    </tr>
    <tr>
      <td>Sample Output 1:</td>
      <td>Sample Output 2:</td>
      </tr>
    <tr>
      <td align="center">
                        FoodInfo(20, 30, 50)<br>
                        FoodInfo(20, 40, 60)<br>
                        FoodInfo(5.0, 10.0, 15.0)<br>
                        FoodInfo(5, 10, 15)<br>
      </td>
      <td align="center">
                        Некорректный тип данных<br>
      </td>
    </tr>
  </tbody>
</table>



## Примеры решений:
* Первый вариант решения
```python
class FoodInfo:
    def __init__(self, proteins, fats, carbohydrates):
        self.proteins = proteins
        self.fats = fats
        self.carbohydrates = carbohydrates

    def __repr__(self):
        return f"{__class__.__name__}({self.proteins}, {self.fats}, {self.carbohydrates})"
    
    def __add__(self, other):
        if isinstance(other, __class__):
            return __class__((self.proteins + other.proteins), (self.fats + other.fats), (self.carbohydrates + other.carbohydrates))
        return NotImplemented
    
    def __mul__(self, n):
        if isinstance(n, int) or isinstance(n, float):
            return __class__((self.proteins * n), (self.fats * n), (self.carbohydrates * n))
        return NotImplemented
    
    def __truediv__(self, n):
        if isinstance(n, int) or isinstance(n, float):
            return __class__((self.proteins / n), (self.fats / n), (self.carbohydrates / n))
        return NotImplemented
    
    def __floordiv__(self, n):
        if isinstance(n, int) or isinstance(n, float):
            return __class__((self.proteins // n), (self.fats // n), (self.carbohydrates // n))
        return NotImplemented

```
* Второй вариант решения

```python
class FoodInfo:
    def __init__(self, proteins, fats, carbohydrates):
        self.proteins = proteins
        self.fats = fats
        self.carbohydrates = carbohydrates
        
    def __repr__(self):
        return f'FoodInfo({", ".join(map(str, self.__dict__.values()))})'
    
    def __add__(self, other):
        if isinstance(other, self.__class__):
            return self.__class__(*map(lambda a, b: a + b, self.__dict__.values(), other.__dict__.values()))
        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return self.__class__(*(value * other for value in self.__dict__.values()))
        return NotImplemented
    
    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            return self.__class__(*(value / other for value in self.__dict__.values()))
        return NotImplemented
    
    def __floordiv__(self, other):
        if isinstance(other, (int, float)):
            return self.__class__(*(value // other for value in self.__dict__.values()))
        return NotImplemented
```


