<h2 style="text-align:center">Класс Peekable</h2>


### Реализуйте класс Peekable. При создании экземпляра класс должен принимать один аргумент:
* iterable — итерируемый объект
#### Экземпляр класса Peekable должен являться итератором, который генерирует элементы итерируемого объекта iterable в исходном порядке, а затем возбуждает исключение StopIteration.

#### Класс Peekable должен иметь один метод экземпляра:
* peek() — метод, возвращающий следующий элемент итератора аналогично функции next(), но при этом не сдвигающий итератор. Если итератор пуст, должно быть возбуждено исключение StopIteration. Также метод должен уметь принимать один необязательный аргумент default — объект, который будет возвращен вместо возбуждения исключения StopIteration, если итератор пуст
##### Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.
##### Примечание 2. Класс Peekable должен удовлетворять протоколу итератора, то есть иметь методы __iter__() и __next__(). Реализация же протокола может быть произвольной.

<table align="center">
  <tbody>
    <tr>
      <th>Sample Input 1: </th>
      <th>Sample Input 2: </th>
      <th>Sample Input 3: </th>
    </tr>
    <tr>
      <td align="center">iterator = Peekable('beegeek')<br>
                          print(next(iterator))<br>
                          print(next(iterator))<br>
                          print(*iterator)<br></td>
      <td align="center">iterator = Peekable('Python')<br>
                        print(next(iterator))<br>
                        print(iterator.peek())<br>
                        print(iterator.peek())<br>
                        print(next(iterator))<br>
                        print(iterator.peek())<br>
                        print(iterator.peek())<br></td>
      <td align="center">iterator = Peekable('Python')<br>
                          print(*iterator)<br>
                          print(iterator.peek(None))<br></td>
    </tr>
    <tr>
      <td>Sample Output 1:</td>
      <td>Sample Output 2:</td>
      <td>Sample Output 3:</td>
      </tr>
    <tr>
      <td align="center">
                        b<br>
                        e<br>
                        e g e e k<br>
      </td>
      <td align="center">
                        P<br>
                        y<br>
                        y<br>
                        y<br>
                        t<br>
                        t<br>
      </td>
      <td align="center">
                        P y t h o n<br>
                        None<br>
      </td>
    </tr>
  </tbody>
</table>



## Примеры решений:
* Первый вариант решения
```python
class Peekable:
    def __init__(self, iterables):
        self.iterables = list(iterables)
        self.__i = 0

    def peek(self, default=StopIteration):
        if self.__i >= len(self.iterables):
            if default == StopIteration:
                raise default
            else:
                return default
        return self.iterables[self.__i]

    def __iter__(self):
        return self

    def __next__(self):
        if self.__i >= len(self.iterables):
            raise StopIteration
        self.__i += 1
        return self.iterables[self.__i-1]
```
* Второй вариант решения

```python
class Peekable:
    def __init__(self, iterable):
        self.iterable = list(iterable)
        self.index = -1 
    
    def peek(self, default=StopIteration):
        try:
            return self.iterable[self.index + 1]
        except:
            if default == StopIteration:
                raise default
            else:
                return default
    
    def __iter__(self):
        return self
    
    def __next__(self):
        self.index += 1
        if self.index == len(self.iterable):
            raise StopIteration
        return self.iterable[self.index]
```


