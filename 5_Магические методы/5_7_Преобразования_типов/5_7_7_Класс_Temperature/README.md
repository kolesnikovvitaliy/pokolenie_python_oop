<h2 style="text-align:center">Класс Temperature</h2>


### Реализуйте класс Temperature, описывающий температуру в градусах по шкале Цельсия. При создании экземпляра класс должен принимать один аргумент:
* temperature — температура в градусах по шкале Цельсия
#### Класс Temperature должен иметь один метод экземпляра:
* to_fahrenheit() — метод, возвращающий температуру по шкале Фаренгейта
#### Класс Temperature должен иметь один метод класса:
* from_fahrenheit() — метод, принимающий в качестве аргумента температуру по шкале Фаренгейта и возвращающий экземпляр класса Temperature, созданный на основе переданной температуры
#### Экземпляр класса Temperature должен иметь следующее неформальное строковое представление:
> <температура в градусах по шкале Цельсия с округлением до двух знаков после запятой>°C
#### Также экземпляр класса Temperature должен поддерживать приведение к типам bool, int и float:
* при приведении к типу bool значением экземпляра класса Temperature должно являться значение True, если его температура выше нуля, или False в противном случае
* при приведении к типу int значением экземпляра класса Temperature должна являться его температура в виде целого числа с отброшенной дробной частью
* при приведении к типу float значением экземпляра класса Temperature должна являться его температура в виде вещественного числа

<div>
<img align="center" src="https://github.com/kolesnikovvitaliy/pokolenie_python_oop/blob/main/5_Магические методы/5_7_Преобразования_типов/5_7_7_Класс_Temperature/img/task.png" title="Git" **alt="Git">
​</div>

##### Примечание 2. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.
##### Примечание 3. Никаких ограничений касательно реализации класса Temperature нет, она может быть произвольной.

<table align="center">
  <tbody>
    <tr>
      <th>Sample Input 1: </th>
      <th>Sample Input 2: </th>
      <th>Sample Input 3: </th>
    </tr>
    <tr>
      <td align="center">t = Temperature(5.5)<br>
                          print(t)<br>
                          print(int(t))<br>
                          print(float(t))<br>
                          print(t.to_fahrenheit())<br></td>
      <td align="center">t1 = Temperature(1)<br>
                          t2 = Temperature(0)<br>
                          t3 = Temperature(-1)<br>
                          print(bool(t1))<br>
                          print(bool(t2))<br>
                          print(bool(t3))<br></td>
      <td align="center">t = Temperature.from_fahrenheit(41)<br>
                            print(t)<br>
                            print(int(t))<br>
                            print(float(t))<br>
                            print(t.to_fahrenheit())<br></td>
    </tr>
    <tr>
      <td>Sample Output 1:</td>
      <td>Sample Output 2:</td>
      <td>Sample Output 3:</td>
      </tr>
    <tr>
      <td align="center">
                        5.5°C<br>
                          5<br>
                          5.5<br>
                          41.9<br>
      </td>
      <td align="center">
                        True<br>
                        False<br>
                        False<br>
      </td>
      <td align="center">
                        5.0°C<br>
                          5<br>
                          5.0<br>
                          41.0<br>
      </td>
    </tr>
  </tbody>
</table>



## Примеры решений:
* Первый вариант решения
```python
class Temperature:
    def __init__(self, temperature):
        self.temperature = temperature

    def __str__(self) -> str:
        return f"{round(self.temperature,2)}°C"

    def to_fahrenheit(self):
        return self.temperature * (9/5) + 32

    @classmethod    
    def from_fahrenheit(cls, fahrenheit):
        temperature = ((5/9) * (fahrenheit - 32))
        return cls(temperature)

    def __bool__(self):
        return self.temperature > 0

    def __int__(self):
        return int(self.temperature)
    
    def __float__(self):
        return float(self.temperature)
```
* Второй вариант решения

```python
class Temperature:
    def __init__(self, temperature):
        self.temperature = temperature

    def to_fahrenheit(self):
        return self.temperature * 1.8 + 32

    def __str__(self):
        return f'{self.temperature.__round__(2)}°C'

    def __bool__(self):
        return self.temperature > 0

    def __int__(self):
        return int(self.temperature)

    def __float__(self):
        return float(self.temperature)

    @classmethod
    def from_fahrenheit(cls, value):
        celsius = (5 / 9) * (value - 32)
        return cls(celsius)
```


