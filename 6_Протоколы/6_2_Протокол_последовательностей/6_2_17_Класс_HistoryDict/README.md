<h2 style="text-align:center">Класс HistoryDict</h2>

### Реализуйте класс HistoryDict, описывающий словарь, который запоминает предыдущие значения по каждому ключу. При создании экземпляра класс должен принимать один аргумент:
* data — словарь, определяющий начальный набор элементов экземпляра класса HistoryDict. Если не передан, начальный набор элементов считается пустым
#### Класс HistoryDict должен иметь пять методов экземпляра:
* keys() — метод, возвращающий итерируемый объект, элементами которого являются ключи экземпляра класса HistoryDict
* values() — метод, возвращающий итерируемый объект, элементами которого являются значения ключей экземпляра класса HistoryDict
* items() — метод, возвращающий итерируемый объект элементами которого являются элементы экземпляра класса HistoryDict в виде кортежей (<ключ>, <значение>)
* history() — метод, принимающий в качестве аргумента ключ и возвращающий список, элементами которого являются все значения, которые когда-либо содержались в экземпляре класса HistoryDict по указанному ключу. Если данный ключ не содержится в экземпляре класса HistoryDict (был удален или никогда не добавлялся), метод должен вернуть пустой список
* all_history() — метод, возвращающий словарь, ключами в котором являются ключи экземпляра класса HistoryDict, а значениями — списки, содержащие все значения, которые когда-либо содержались по этим ключам
#### При передаче экземпляра класса HistoryDict в функцию len() должно возвращаться количество элементов в нем.
#### Также экземпляр класса HistoryDict должен быть итерируемым объектом, то есть позволять перебирать свои ключи, например, с помощью цикла for.
#### Наконец, экземпляр класса HistoryDict должен позволять получать и изменять значения своих элементов по их ключам, добавлять новые пары (ключ, значение) и удалять уже имеющиеся.
##### Примечание 1. Экземпляр класса HistoryDict не должен зависеть от словаря, на основе которого он был создан. Другими словами, если исходный словарь изменится, то экземпляр класса HistoryDict измениться  не должен.
##### Примечание 2. Реализация класса HistoryDict может быть произвольной, то есть требований к наличию определенных атрибутов нет.
##### Примечание 3. Дополнительная проверка данных на корректность в методах не требуется. Гарантируется, что реализованный класс используется только с корректными данными.

<table align="center">
  <tbody>
    <tr>
      <th>Sample Input 1: </th>
      <th>Sample Input 2: </th>
      <th>Sample Input 3: </th>
      <th>Sample Input 4: </th>
      <th>Sample Input 5: </th>
    </tr>
    <tr>
      <td align="center">historydict = HistoryDict({'ducks': 99, 'cats': 1})<br>
                        print(historydict['ducks'])<br>
                        print(historydict['cats'])<br>
                        print(len(historydict))<br></td>
      <td align="center">historydict = HistoryDict({'ducks': 99, 'cats': 1})<br>
                        print(*historydict)<br>
                        print(*historydict.keys())<br>
                        print(*historydict.values())<br>
                        print(*historydict.items())<br></td>
      <td align="center">historydict = HistoryDict({'ducks': 99, 'cats': 1})<br>
                        historydict['ducks'] = 100<br>
                        print(historydict.history('ducks'))<br>
                        print(historydict.history('cats'))<br>
                        print(historydict.history('dogs'))<br></td>
      <td align="center">historydict = HistoryDict({'ducks': 99, 'cats': 1})<br>
                        print(historydict.all_history())<br>
                        historydict['ducks'] = 100<br>
                        historydict['ducks'] = 101<br>
                        historydict['cats'] = 2<br>
                        print(historydict.all_history())<br></td>
      <td align="center">historydict = HistoryDict({'ducks': 99, 'cats': 1})<br>
                          historydict['dogs'] = 1<br>
                          print(len(historydict))<br>
                          del historydict['ducks']<br>
                          del historydict['cats']<br>
                          print(len(historydict))<br></td>
    </tr>
    <tr>
      <td>Sample Output 1:</td>
      <td>Sample Output 2:</td>
      <td>Sample Output 3:</td>
      <td>Sample Output 4:</td>
      <td>Sample Output 5:</td>
      </tr>
    <tr>
      <td align="center">
                        99<br>
                        1<br>
                        2<br>
      </td>
      <td align="center">
                        ducks cats<br>
                        ducks cats<br>
                        99 1<br>
                        ('ducks', 99) ('cats', 1)<br>
      </td>
      <td align="center">
                        [99, 100]<br>
                        [1]<br>
                        []<br>
      </td>
      <td align="center">
                        {'ducks': [99], 'cats': [1]}<br>
                        {'ducks': [99, 100, 101], 'cats': [1, 2]}<br>
      </td>
      <td align="center">
                        3<br>
                        1<br>
      </td>
    </tr>
  </tbody>
</table>



## Примеры решений:
* Первый вариант решения
```python
class HistoryDict:
    def __init__(self, data=()):
        self._data = dict(data) or {}
        self._history = {k:[v] for k,v in dict(data).items()} or {}
    
    def keys(self):
        return self._data.keys()

    def values(self):
        return self._data.values()

    def items(self):
        return self._data.items()
    
    def history(self, key):
        if key in  self._history:
            return self._history[key]
        return []
    
    def all_history(self):
        return self._history
    
    def __len__(self):
        return len(self._data)

    def __iter__(self):
        yield from self._data

    def __setitem__(self, key, __value):
        self._data[key] = __value
        self._history.setdefault(key, []).append(__value)
        
    def __getitem__(self, key):
        return self._data[key]
    
    def __delitem__(self, key):
        del self._data[key]
        del self._history[key]
```
* Второй вариант решения

```python
class HistoryDict:
    def __init__(self, data=()):
        self._data = dict(data) or {}
        self._history = {key: [value] for key, value in self._data.items()}

    def keys(self):
        return self._data.keys()

    def values(self):
        return self._data.values()

    def items(self):
        return self._data.items()

    def history(self, key):
        return self._history.get(key, [])

    def all_history(self):
        return self._history

    def __len__(self):
        return len(self._data)

    def __iter__(self):
        return iter(self.keys())

    def __delitem__(self, key):
        del self._data[key]
        del self._history[key]

    def __setitem__(self, key, value):
        self._history.setdefault(key, []).append(value)
        self._data[key] = value

    def __getitem__(self, key):
        return self._data[key]
```


