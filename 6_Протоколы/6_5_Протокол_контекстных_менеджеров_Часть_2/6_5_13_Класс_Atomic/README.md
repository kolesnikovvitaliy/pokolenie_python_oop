<h2 style="text-align:center">Класс Atomic</h2>

### Реализуйте класс Atomic. При создании экземпляра класс должен принимать два аргумента в следующем порядке:
* data — произвольный список, множество или словарь
* deep — булево значение, по умолчанию равняется False
#### Экземпляр класса Atomic должен являться контекстным менеджером, который позволяет выполнять операции над коллекцией data внутри блока with в атомарном режиме, то есть либо все операции должны быть выполнены, либо ни одна из них. Если все операции корректны (не приводят к возбуждению исключения), они должны быть применены к коллекции data. Если какая-либо операция некорректна, все ранее выполненные операции должны быть отменены, а коллекция data должна быть возвращена в исходное состояние.
#### Параметр deep должен определять состояние вложенных структур коллекции data после завершения блока with. Если он имеет значение False, контекстный менеджер должен возвращать в исходное состояние только саму коллекцию data, не затрагивая ее вложенные структуры. Например, если data является двумерным списком и внутри блока with произошло изменение одного из его вложенных списков, то этот вложенный список должен сохранить свое новое состояние, даже если последующие операции внутри блока with приведут к возбуждению исключения и возврату коллекции data в исходное состояние. Если же параметр deep имеет значение True, контекстный менеджер должен возвращать в исходное состояние не только саму коллекцию data, но и ее вложенные структуры.



##### Примечание 1. Наглядные примеры использования класса Atomic продемонстрированы в тестовых данных.
##### Примечание 2. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.
##### Примечание 3. Класс Atomic должен удовлетворять протоколу контекстного менеджера, то есть иметь методы __enter__() и __exit__(). Реализация же протокола может быть произвольной.



<table align="center">
  <tbody>
    <tr>
      <th>Sample Input 1: </th>
      <th>Sample Input 2: </th>
      <th>Sample Input 3: </th>
      <th>Sample Input 4: </th>
    </tr>
    <tr>
      <td align="center">numbers = [1, 2, 3, 4, 5]<br>
                        with Atomic(numbers) as atomic:<br>
                            atomic.append(6)<br>
                            atomic[2] = 0<br>
                            del atomic[1]<br>
                        print(numbers)<br></td>
      <td align="center">numbers = [1, 2, 3, 4, 5]<br>
                          with Atomic(numbers) as atomic:<br>
                              atomic.append(6)<br>
                              atomic[2] = 0<br>
                              del atomic[100]           # обращение по несуществующему индексу<br>
                          print(numbers)<br></td>
      <td align="center">matrix = [[1, 2], [3, 4]]<br>
                        with Atomic(matrix) as atomic:<br>
                            atomic[1].append(0)       # изменение вложенной структуры<br>
                            atomic.append([5, 6])<br>
                            del atomic[100]           # обращение по несуществующему индексу<br>
                        print(matrix)<br></td>
      <td align="center">matrix = [[1, 2], [3, 4]]<br>
                        with Atomic(matrix, True) as atomic:<br>
                            atomic[1].append(0)       # изменение вложенной структуры<br>
                            atomic.append([5, 6])<br>
                            del atomic[100]           # обращение по несуществующему индексу<br>
                        print(matrix)<br></td>
    </tr>
    <tr>
      <td>Sample Output 1:</td>
      <td>Sample Output 2:</td>
      <td>Sample Output 3:</td>
      <td>Sample Output 4:</td>
      </tr>
    <tr>
      <td align="center">
                        [1, 0, 4, 5, 6]<br>
      </td>
      <td align="center">
                        [1, 2, 3, 4, 5]<br>
      </td>
      <td align="center">
                        [[1, 2], [3, 4, 0]]<br>
      </td>
      <td align="center">
                        [[1, 2], [3, 4]]<br>
      </td>
    </tr>
  </tbody>
</table>



## Примеры решений:
* Первый вариант решения
```python
from copy import deepcopy


class Atomic:
    def __init__(self, data, deep=False):
        self.data = data
        self._copy = deepcopy(data)
        self.deep = deep

    def __enter__(self):
        return self.data
    
    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type == None:
            return self.data
        else:
            if self.deep:
                if isinstance(self.data, list):
                    self.data[:] = self._copy[:]
                elif isinstance(self.data, dict):
                    for k, v in self._copy.items():
                        self.data[k] = v
                elif isinstance(self.data, set):
                    self.data.clear()
                    self.data.update(self._copy)
            else: 
                if isinstance(self.data, list):
                    if isinstance(self.data[0], list):
                        self.data[:] = self.data[:len(self._copy)]
                    else:
                        self.data[:] = self._copy[:]
                elif isinstance(self.data, dict):
                    for k, v in self.data.items():
                        self.data[k] = v
                elif isinstance(self.data, set):
                    self.data.clear()
                    self.data.update(self._copy)                
        return True
```
* Второй вариант решения

```python
import copy


class Atomic:
    def __init__(self, data, deep=False):
        self.original = data
        self.copy = copy.deepcopy if deep else copy.copy
        
        if isinstance(data, list):
            self.original_update = self.original.extend
        elif isinstance(data, (set, dict)):
            self.original_update = self.original.update

    def __enter__(self):
        self.data = self.copy(self.original)
        return self.data

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            self.original.clear()
            self.original_update(self.data)
        return True
```


