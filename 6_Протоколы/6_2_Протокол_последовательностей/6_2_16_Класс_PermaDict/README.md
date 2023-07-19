<h2 style="text-align:center">Класс PermaDict</h2>


### Реализуйте класс PermaDict, описывающий словарь, который позволяет добавлять и удалять пары (<ключ>, <значение>), но не позволяет изменять значения по уже имеющимся ключам. При создании экземпляра класс должен принимать один аргумент:
* data — словарь, определяющий начальный набор элементов экземпляра класса PermaDict. Если не передан, начальный набор элементов считается пустым
#### Класс PermaDict должен иметь три метода экземпляра:
* keys() — метод, возвращающий итерируемый объект, элементами которого являются ключи экземпляра класса PermaDict
* values() — метод, возвращающий итерируемый объект, элементами которого являются значения ключей экземпляра класса PermaDict
* items() — метод, возвращающий итерируемый объект элементами которого являются элементы экземпляра класса PermaDict в виде кортежей (<ключ>, <значение>)
#### При передаче экземпляра класса PermaDict в функцию len() должно возвращаться количество элементов в нем.
#### Также экземпляр класса PermaDict должен быть итерируемым объектом, то есть позволять перебирать свои ключи, например, с помощью цикла for
#### Наконец, экземпляр класса PermaDict должен позволять получать значения своих элементов по их ключам, добавлять новые пары (ключ, значение) и удалять уже имеющиеся с помощью оператора del. При этом изменение значений по уже имеющимся ключам должно быть недоступно, и при попытке выполнения такой операции должно возбуждаться исключение KeyError с текстом:
> Изменение значения по ключу невозможно
##### Примечание 1. Экземпляр класса PermaDict не должен зависеть от словаря, на основе которого он был создан. Другими словами, если исходный словарь изменится, то экземпляр класса PermaDict измениться  не должен.
##### Примечание 2. Реализация класса PermaDict может быть произвольной, то есть требований к наличию определенных атрибутов нет.
##### Примечание 3. Дополнительная проверка данных на корректность в методах не требуется. Гарантируется, что реализованный класс используется только с корректными данными.

<table align="center">
  <tbody>
    <tr>
      <th>Sample Input 1: </th>
      <th>Sample Input 2: </th>
      <th>Sample Input 3: </th>
      <th>Sample Input 4: </th>
    </tr>
    <tr>
      <td align="center">permadict = PermaDict({'name': 'Timur', 'city': 'Moscow'})<br>
                        print(permadict['name'])<br>
                        print(len(permadict))<br></td>
      <td align="center">permadict = PermaDict({'name': 'Timur', 'city': 'Moscow', 'age': 30})<br>
                        print(*permadict)<br>
                        print(*permadict.keys())<br>
                        print(*permadict.values())<br>
                        print(*permadict.items())<br></td>
      <td align="center">permadict = PermaDict()<br>
                        permadict['name'] = 'Timur'<br>
                        permadict['age'] = 30<br>
                        del permadict['name']<br>
                        print(permadict['age'])<br>
                        print(len(permadict))<br></td>
      <td align="center">permadict = PermaDict({'name': 'Timur', 'city': 'Moscow'})<br>
                        try:<br>
                            permadict['name'] = 'Arthur'<br>
                        except KeyError as e:<br>
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
                       Timur<br>
                        2<br>
      </td>
      <td align="center">
                        name city age<br>
                        name city age<br>
                        Timur Moscow 30<br>
                        ('name', 'Timur') ('city', 'Moscow') ('age', 30)<br>
      </td>
      <td align="center">
                        30<br>
                        1<br>
      </td>
      <td align="center">
                        'Изменение значения по ключу невозможно'<br>
      </td>
    </tr>
  </tbody>
</table>



## Примеры решений:
* Первый вариант решения
```python
from copy import deepcopy


class PermaDict:
    def __init__(self, data={}):
        self.data = deepcopy(data or {})
    
    def keys(self):
        return self.data.keys()

    def values(self):
        return self.data.values()

    def items(self):
        return self.data.items()

    def __len__(self):
        return len(self.data)

    def __iter__(self):
        yield from self.data

    def __setitem__(self, key, __value):
        if key in self.data:
            raise KeyError('Изменение значения по ключу невозможно')
        self.data[key] = __value

    def __getitem__(self, __value):
        return self.data[__value]
    
    def __delitem__(self, key):
        del self.data[key]

```
* Второй вариант решения

```python
class PermaDict:
    def __init__(self, data=()):
        self._data = dict(data) or {}

    def keys(self):
        return self._data.keys()

    def values(self):
        return self._data.values()

    def items(self):
        return self._data.items()

    def __len__(self):
        return len(self._data)

    def __iter__(self):
        return iter(self.keys())

    def __delitem__(self, key):
        del self._data[key]

    def __setitem__(self, key, value):
        if key in self.keys():
            raise KeyError('Изменение значения по ключу невозможно')
        self._data[key] = value

    def __getitem__(self, key):
        return self._data[key]
```


