<h2 style="text-align:center">Класс MultiKeyDict</h2>

### Реализуйте класс MultiKeyDict, который практически во всем повторяет класс dict. Создание экземпляра класса MultiKeyDict должно происходить аналогично созданию экземпляра класса dict:

```python 
multikeydict1 = MultiKeyDict(x=1, y=2, z=3)
multikeydict2 = MultiKeyDict([('x', 1), ('y', 2), ('z', 3)])

print(multikeydict1['x'])        # 1
print(multikeydict2['z'])        # 3
```
#### Особенностью класса MultiKeyDict должен являться метод alias(), который должен позволять давать имеющимся ключам псевдонимы. Обращение по созданному псевдониму не должно ничем отличаться от обращения по оригинальному ключу, то есть с момента создания псевдонима у значения становится два ключа (или больше, если псевдонимов несколько):
```python 
multikeydict = MultiKeyDict(x=100, y=[10, 20])

multikeydict.alias('x', 'z')     # добавление ключу 'x' псевдонима 'z'
multikeydict.alias('x', 't')     # добавление ключу 'x' псевдонима 't'
print(multikeydict['z'])         # 100
multikeydict['t'] += 1
print(multikeydict['x'])         # 101

multikeydict.alias('y', 'z')     # теперь 'z' становится псевдонимом ключа 'y'
multikeydict['z'] += [30]
print(multikeydict['y'])         # [10, 20, 30]
```
#### Значение должно оставаться доступным по псевдониму даже в том случае, если оригинальный ключ был удален:
```python 
multikeydict = MultiKeyDict(x=100)

multikeydict.alias('x', 'z')
del multikeydict['x']
print(multikeydict['z'])         # 100
```
#### Ключи должны иметь приоритет над псевдонимами. Если некоторые ключ и псевдоним совпадают, то все операции при обращении к ним должны выполняться именно с ключом:
```python 
multikeydict = MultiKeyDict(x=100, y=[10, 20])

multikeydict.alias('x', 'y')
print(multikeydict['y'])         # [10, 20]
```

<table align="center">
  <tbody>
    <tr>
      <th>Sample Input 1: </th>
      <th>Sample Input 2: </th>
      <th>Sample Input 3: </th>
      <th>Sample Input 4: </th>
    </tr>
    <tr>
      <td align="center">multikeydict = MultiKeyDict(x=100, y=[10, 20])<br>
                        multikeydict.alias('x', 'z')<br>
                        multikeydict.alias('x', 't')<br>
                        print(multikeydict['z'])<br>
                        multikeydict['t'] += 1<br>
                        print(multikeydict['x'])<br>
                        multikeydict.alias('y', 'z')<br>
                        multikeydict['z'] += [30]<br>
                        print(multikeydict['y'])<br></td>
      <td align="center">multikeydict = MultiKeyDict(x=100)<br>
                        multikeydict.alias('x', 'z')<br>
                        del multikeydict['x']<br>
                        print(multikeydict['z'])<br>
                        try:<br>
                            print(multikeydict['x'])<br>
                        except KeyError:<br>
                            print('Ключ отстутствует')<br></td>
      <td align="center">multikeydict = MultiKeyDict(x=100, y=[10, 20])<br>
                          multikeydict.alias('x', 'y')<br>
                          print(multikeydict['y'])<br>
                          multikeydict['y'] += [30]<br>
                          print(multikeydict['y'])<br></td>
      <td align="center">multikeydict = MultiKeyDict(lecture='python', lesson='object oriented programming')<br>
                          multikeydict.alias('lecture', 'lesson')<br>
                          print(multikeydict['lesson'])<br>
                          multikeydict.alias('lecture', 'lesson')<br>
                          print(multikeydict['lesson'])<br>
                          del multikeydict['lesson']<br>
                          print(multikeydict['lesson'])<br></td>
    </tr>
    <tr>
      <td>Sample Output 1:</td>
      <td>Sample Output 2:</td>
      <td>Sample Output 3:</td>
      <td>Sample Output 4:</td>
      </tr>
    <tr>
      <td align="center">
                        100<br>
                        101<br>
                        [10, 20, 30]<br>
      </td>
      <td align="center">
                        100<br>
                        Ключ отстутствует<br>
      </td>
      <td align="center">
                        [10, 20]<br>
                        [10, 20, 30]<br>
      </td>
      <td align="center">
                        object oriented programming<br>
                        object oriented programming<br>
                        python<br>
      </td>
    </tr>
  </tbody>
</table>



## Примеры решений:
* Первый вариант решения
```python
from collections import UserDict


class MultiKeyDict(UserDict):
    def __init__(self, *args, **kwargs):
        self._key = {}
        super().__init__(*args, **kwargs)
        self._key = {k: k for k in self.data.keys()}

    def alias(self, key, alias):
        if alias not in self.data:
            self._key[alias] = key

    def __getitem__(self, __key):
        if __key in self._key:
            return super().__getitem__(self._key[__key])
        return super().__getitem__(__key)

    def __setitem__(self, __key, __value):
        if __key in self._key:
            self.data[self._key[__key]] = __value
        else:
            self.data[__key] = __value

    def __delitem__(self, __key):
        new_key = [i for i in self._key.keys() if i != __key][0]
        if new_key not in self.data:
            del self._key[__key]
            self._key[new_key] = new_key
            self.data[new_key] = self.data.pop(__key)
            if __key in self._key.values():
                key_2 = [k for k, v in self._key.items() if v == __key][0]
                self._key[key_2] = new_key
        else:
            self.data[__key] = self.data.pop(self._key[__key])
            self._key[__key] = new_key
            del self._key[new_key]
            del self.data[__key]
```
* Второй вариант решения

```python
from collections import UserDict


class MultiKeyDict(UserDict):
    def __init__(self, *args, **kwargs):
        self._aliases = {}
        super().__init__(*args, **kwargs)

    def alias(self, key, alias):
        self._aliases[alias] = key

    def __getitem__(self, key):
        return self.data.get(key) or self.data.get(self._aliases[key])

    def __setitem__(self, key, value):
        if key in self.data or key not in self._aliases:
            self.data[key] = value
        else:
            self.data[self._aliases[key]] = value

    def __delitem__(self, del_key):
        for alias_key, key in self._aliases.items():
            if key == del_key:
                self.data[alias_key] = self.data[del_key]
        del self.data[del_key]

```


