<h2 style="text-align:center">Класс AttrDict</h2>

### Реализуйте класс AttrDict, описывающий упрощенный словарь, значения элементов которого можно получать как по ключам ([key]), так и по одноименным атрибутам (.key). При создании экземпляра класс должен принимать один аргумент:
* data — словарь, определяющий начальный набор элементов упрощенного словаря. Если не передан, начальный набор элементов считается пустым
#### При передаче экземпляра класса AttrDict в функцию len() должно возвращаться количество элементов в нем.
#### Также экземпляр класса AttrDict должен быть итерируемым объектом, то есть позволять перебирать свои ключи, например, с помощью цикла for.
#### Наконец, экземпляр класса AttrDict должен позволять получать значения своих элементов как по их ключам, так и по одноименным атрибутам. Реализовывать добавление элементов и изменение их значений по одноименным атрибутам не нужно.

##### Примечание 1. Экземпляр класса AttrDict не должен зависеть от словаря, на основе которого он был создан. Другими словами, если исходный словарь изменится, то экземпляр класса AttrDict измениться  не должен.
##### Примечание 2. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.
##### Примечание 3. Никаких ограничений касательно реализации класса AttrDict нет, она может быть произвольной.

<table align="center">
  <tbody>
    <tr>
      <th>Sample Input 1: </th>
      <th>Sample Input 2: </th>
      <th>Sample Input 3: </th>
    </tr>
    <tr>
      <td align="center">attrdict = AttrDict({'name': 'X Æ A-12', 'father': 'Elon Musk'})<br>
                          print(attrdict['name'])<br>
                          print(attrdict.father)<br>
                          print(len(attrdict))<br></td>
      <td align="center">attrdict = AttrDict({'name': 'Timur', 'city': 'Moscow'})<br>
                          attrdict['city'] = 'Dubai'<br>
                          attrdict['age'] = 31<br>
                          print(attrdict.city)<br>
                          print(attrdict.age)<br>
<br></td>
      <td align="center">attrdict = AttrDict()<br>
                          attrdict['school_name'] = 'BEEGEEK'<br>
                          print(attrdict['school_name'])<br>
                          print(attrdict.school_name)<br></td>
    </tr>
    <tr>
      <td>Sample Output 1:</td>
      <td>Sample Output 2:</td>
      <td>Sample Output 3:</td>
      </tr>
    <tr>
      <td align="center">
                        X Æ A-12<br>
                        Elon Musk<br>
                        2<br>
      </td>
      <td align="center">
                        Dubai<br>
                        31<br>
      </td>
      <td align="center">
                        BEEGEEK<br>
                        BEEGEEK<br>
      </td>
    </tr>
  </tbody>
</table>



## Примеры решений:
* Первый вариант решения
```python
class AttrDict:
    def __init__(self, data=()):   
        self.__dict__.update(data)
    
    def __setitem__(self, key, value):
        self.__dict__[key]= value
    
    def __getitem__(self, key):
        return self.__dict__[key]
    
    def __setattr__(self, __name, __value):
        return self.__dict__

    def __len__(self):
        return len(self.__dict__)
    
    def __iter__(self):
        yield from self.__dict__
```
* Второй вариант решения

```python
class AttrDict:
    def __init__(self, data=()):
        self._data = dict(data) or {}

    def __len__(self):
        return len(self._data)

    def __getitem__(self, key):
        return self._data[key]

    def __setitem__(self, key, value):
        self._data[key] = value

    def __getattr__(self, key):
        return self._data[key]

    def __iter__(self):
        yield from self._data
```


