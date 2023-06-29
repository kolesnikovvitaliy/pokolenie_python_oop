<h2 style="text-align:center">Класс Formatter</h2>

### Реализуйте класс Formatter. При создании экземпляра класс не должен принимать никаких аргументов.
#### Класс Formatter должен иметь один статический метод:
* format() — метод, принимающий в качестве аргумента объект типа int, float, tuple, list или dict и выводящий информацию о переданном объекте в формате, зависящем от его типа. Если переданный объект принадлежит какому-либо другому типу, должно быть возбуждено исключение TypeError с текстом:
> Аргумент переданного типа не поддерживается
#### Класс Rectangle должен иметь два свойства:
* perimeter — свойство, доступное только для чтения, возвращающее периметр прямоугольника
* area — свойство, доступное только для чтения, возвращающее площадь прямоугольника

##### Примечание 1. Примеры форматирования объектов всех типов показаны в тестовых данных.
##### Примечание 2. Обратите внимание, что метод format() должен обрамлять апострофами строковые элементы коллекций.
##### Примечание 3. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.
##### Примечание 4. Никаких ограничений касательно реализации класса Formatter нет, она может быть произвольной.


<table align="center">
  <tbody>
    <tr>
      <th>Sample Input 1: </th>
      <th>Sample Input 2: </th>
      <th>Sample Input 3: </th>
      <th>Sample Input 4: </th>
    </tr>
    <tr>
      <td align="center">Formatter.format(1337)<br>
                          Formatter.format(20.77)<br></td>
      <td align="center">Formatter.format([10, 20, 30, 40, 50])<br>
                          Formatter.format(([1, 3], [2, 4, 6]))<br></td>
      <td align="center">Formatter.format({'Cuphead': 1, 'Mugman': 3})<br>
                          Formatter.format({1: 'one', 2: 'two'})<br>
                          Formatter.format({1: True, 0: False})<br></td>
      <td align="center">try:<br>
                            Formatter.format('All them years, Dutch, for this snake?')<br>
                        except TypeError as e:<br>
                            print(e)<br></td>
    </tr>
    <tr>
      <td>Sample Output 1:</td>
      <td>Sample Output 2:</td>
      <td>Sample Output 3:</td>
      <td>Sample Output 4:</td>
      </tr>
    <tr>
      <td align="center">
                        Целое число: 1337<br>
                        Вещественное число: 20.77<br>
      </td>
      <td align="center">
                        Элементы списка: 10, 20, 30, 40, 50<br>
                        Элементы кортежа: [1, 3], [2, 4, 6]<br>
      </td>
      <td align="center">
                        Пары словаря: ('Cuphead', 1), ('Mugman', 3)<br>
                        Пары словаря: (1, 'one'), (2, 'two')<br>
                        Пары словаря: (1, True), (0, False)<br>
      </td>
      <td align="center">
                        Аргумент переданного типа не поддерживается<br>
      </td>
    </tr>
  </tbody>
</table>



## Примеры решений:
* Первый вариант решения
```python
from functools import singledispatchmethod


class Formatter:
    @singledispatchmethod
    @staticmethod
    def format(data):
        raise TypeError('Аргумент переданного типа не поддерживается')
    
    
    @format.register(int)
    @staticmethod
    def _int_format(data):
        print(f'Целое число: {data}')

    @format.register(float)
    @staticmethod
    def _int_format(data):
        print(f'Вещественное число: {data}')

    @format.register(tuple)
    @staticmethod
    def _int_format(data):
        print(f"Элементы кортежа: {', '.join(map(str,data))}")

    @format.register(list)
    @staticmethod
    def _int_format(data):
        print(f"Элементы списка: {', '.join(map(str,data))}")

    @format.register(dict)
    @staticmethod
    def _int_format(data):
        print(f"Пары словаря: {', '.join(map(str,data.items()))}")
```
* Второй вариант решения

```python
from functools import singledispatchmethod

class Formatter:
    @singledispatchmethod
    @staticmethod
    def format(data):
        raise TypeError('Аргумент переданного типа не поддерживается')
    
    @format.register(int)
    @staticmethod
    def _(data):
        print(f'Целое число: {data}')
    
    @format.register(float)
    @staticmethod
    def _(data):
        print(f'Вещественное число: {data}')
    
    @format.register(tuple)
    @staticmethod
    def _(data):
        print(f'Элементы кортежа: {", ".join([str(obj) for obj in data])}')
    
    @format.register(list)
    @staticmethod
    def _(data):
        print(f'Элементы списка: {", ".join([str(obj) for obj in data])}')
    
    @format.register(dict)
    @staticmethod
    def _(data):
        print(f'Пары словаря: {", ".join([str(pair) for pair in data.items()])}')
```


