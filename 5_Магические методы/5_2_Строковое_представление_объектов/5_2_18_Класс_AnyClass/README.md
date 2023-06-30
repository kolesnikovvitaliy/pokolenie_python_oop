<h2 style="text-align:center">Класс AnyClass</h2>

### Реализуйте класс AnyClass. При создании экземпляра класс должен принимать произвольное количество именованных аргументов и устанавливать их в качестве атрибутов создаваемому экземпляру.
#### Экземпляр класса AnyClass должен иметь следующее формальное строковое представление:
> AnyClass(<имя 1-го атрибута>=<значение 1-го атрибута>, <имя 2-го атрибута>=<значение 2-го атрибута>, ...)
#### И следующее неформальное строковое представление:
> AnyClass: <имя 1-го атрибута>=<значение 1-го атрибута>, <имя 2-го атрибута>=<значение 2-го атрибута>, ...
##### Примечание 1. Обратите внимание, что в формальном строковом представлении значения атрибутов, которые принадлежат типу str, должны быть обрамлены апострофами.
##### Примечание 2. Никаких ограничений касательно реализации класса AnyClass нет, она может быть произвольной.

<table align="center">
  <tbody>
    <tr>
      <th>Sample Input 1: </th>
      <th>Sample Input 2: </th>
      <th>Sample Input 3: </th>
    </tr>
    <tr>
      <td align="center">any = AnyClass()<br>
                          print(str(any))<br>
                          print(repr(any))<br></td>
      <td align="center">cowboy = AnyClass(name='John', surname='Marston')<br>
                        print(str(cowboy))<br>
                        print(repr(cowboy))<br></td>
      <td align="center">obj = AnyClass(attr1=10, attr2='beegeek', attr3=True, attr4=[1, 2, 3], attr5=('one', 'two'), attr6=None)<br>
                        print(str(obj))<br>
                        print(repr(obj))<br></td>
    </tr>
    <tr>
      <td>Sample Output 1:</td>
      <td>Sample Output 2:</td>
      <td>Sample Output 3:</td>
      </tr>
    <tr>
      <td align="center">
                        AnyClass: <br>
                        AnyClass()<br>
      </td>
      <td align="center">
                        obj = AnyClass(attr1=10, attr2='beegeek', attr3=True, attr4=[1, 2, 3], attr5=('one', 'two'), attr6=None)<br>
      </td>
      <td align="center">
                        AnyClass: attr1=10, attr2='beegeek', attr3=True, attr4=[1, 2, 3], attr5=('one', 'two'), attr6=None<br>
                        AnyClass(attr1=10, attr2='beegeek', attr3=True, attr4=[1, 2, 3], attr5=('one', 'two'), attr6=None)<br>
      </td>
    </tr>
  </tbody>
</table>



## Примеры решений:
* Первый вариант решения
```python
class AnyClass:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)
        self.__any = ", ".join(map(lambda k: f"{k}='{kwargs[k]}'" if type(kwargs[k]) == str else f"{k}={kwargs[k]}", kwargs))
    def __str__(self) -> str:
        return f'AnyClass: {self.__any}'
    
    def __repr__(self) -> str:
        return f"{__class__.__name__}({self.__any})"
```
* Второй вариант решения

```python
class AnyClass:
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

    def __str__(self):
        return f'AnyClass: {", ".join(self._attrs())}'
        
    def __repr__(self):
        return f'AnyClass({", ".join(self._attrs())})'
    
    def _attrs(self):
        return [f'{k}={repr(v)}' for (k, v) in self.__dict__.items()]
```


