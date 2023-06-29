<h2 style="text-align:center">Класс Processor</h2>

### Вам доступен класс Processor. При создании экземпляра класс не принимает никаких аргументов.

#### Класс Processor имеет один статический метод:
* process() — метод, который принимает в качестве аргумента произвольный объект, преобразует его в зависимости от его типа и возвращает полученный результат. Если тип переданного объекта не поддерживается методом, возбуждается исключение TypeError с текстом:
> Аргумент переданного типа не поддерживается

#### Перепишите метод process() класса Processor с использованием декоратора @singledispatchmethod, чтобы он выполнял ту же задачу.
```python
class Processor:
    @staticmethod
    def process(data):
        if isinstance(data, (int, float)):
            return data * 2
        elif isinstance(data, str):
            return data.upper()
        elif isinstance(data, list):
            return sorted(data)
        elif isinstance(data, tuple):
            return tuple(sorted(data))
        raise TypeError('Аргумент переданного типа не поддерживается')
```
##### Примечание 1. Примеры преобразования объектов всех поддерживаемых типов показаны в методе process() класса Processor.
##### Примечание 2. Никаких ограничений касательно реализации класса Processor нет, она может быть произвольной.

<table align="center">
  <tbody>
    <tr>
      <th>Sample Input 1: </th>
      <th>Sample Input 2: </th>
    </tr>
    <tr>
      <td align="center">print(Processor.process(10))<br>
                          print(Processor.process(5.2))<br>
                          print(Processor.process('hello'))<br>
                          print(Processor.process((4, 3, 2, 1)))<br>
                          print(Processor.process([3, 2, 1]))<br></td>
      <td align="center">try:<br>
                              Processor.process({1, 2, 3})<br>
                          except TypeError as e:<br>
                              print(e)<br></td>
    </tr>
    <tr>
      <td>Sample Output 1:</td>
      <td>Sample Output 2:</td>
      </tr>
    <tr>
      <td align="center">
                        20<br>
                        10.4<br>
                        HELLO<br>
                        (1, 2, 3, 4)<br>
                        [1, 2, 3]<br>
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


class Processor:
    @singledispatchmethod
    @staticmethod
    def process(data):
        raise TypeError('Аргумент переданного типа не поддерживается')
    
    
    @process.register(tuple)
    @staticmethod
    def _tuple_process(data):
        return tuple(sorted(data))
    
    @process.register(str)
    @staticmethod
    def _str_process(data):
        return data.upper()
    
    @process.register(list)
    @staticmethod
    def _list_process(data):
        return sorted(data)
    
    @process.register(float)
    @staticmethod
    def _list_process(data):
        return data * 2
    
    @process.register(int)
    @staticmethod
    def _list_process(data):
        return data * 2
```
* Второй вариант решения

```python
from functools import singledispatchmethod

class Processor:
    @singledispatchmethod
    @staticmethod
    def process(data):
        raise TypeError('Аргумент переданного типа не поддерживается')
        
    @process.register(float)
    @process.register(int)
    @staticmethod
    def _numeric_process(data):
        return 2 * data
        
    @process.register(str)
    @staticmethod
    def _str_process(data):
        return data.upper()
        
    @process.register(list)
    @staticmethod
    def _list_process(data):
        return sorted(data)
    
    @process.register(tuple)
    @staticmethod
    def _tuple_process(data):
        return tuple(sorted(data))
```


