<h2 style="text-align:center">Класс Row</h2>

### Реализуйте класс Row, описывающий объект, содержащий произвольный набор атрибутов. При создании экземпляра класс должен принимать произвольное количество именованных аргументов и устанавливать их в качестве атрибутов создаваемому экземпляру.
### Класс Row должен запрещать устанавливать новые атрибуты своим экземплярам. Помимо этого класс должен запрещать изменять значения уже имеющихся атрибутов, а также удалять их. При попытке установить новый атрибут должно возбуждаться исключение AttributeError с текстом:
> Установка нового атрибута невозможна
#### При попытке изменить значение уже имеющегося атрибута должно возбуждаться исключение AttributeError с текстом:
> Изменение значения атрибута невозможно
#### При попытке удалить атрибут должно возбуждаться исключение AttributeError с текстом:
> Удаление атрибута невозможно

#### Экземпляр класса Row должен иметь следующее формальное строковое представление:
> Row(<имя 1-го атрибута>=<значение 1-го атрибута>, <имя 2-го атрибута>=<значение 2-го атрибута>, ...)

#### Также экземпляры класса Row должны поддерживать между собой операции сравнения с помощью операторов == и!=. Два экземпляра класса Row считаются равными, если их наборы атрибутов полностью совпадают, то есть совпадает их количество, позиции, имена и соответствующие значения.
#### Наконец, при передаче экземпляра класса Row в функцию hash() должно возвращаться его хеш-значение. Алгоритм вычисления хеш-значения может быть произвольным, однако он должен учитывать все атрибуты экземпляра, их позиции, имена и соответствующие значения

##### Примечание 1. Гарантируется, что значениями атрибутов экземпляров класса Row являются хешируемые объекты.
##### Примечание 2. Обратите внимание, что в формальном строковом представлении значения атрибутов, которые принадлежат типу str, должны быть обрамлены апострофами.
##### Примечание 3. Если объект, с которым происходит сравнение, некорректен, метод, реализующий операцию сравнения, должен вернуть константу NotImplemented.
##### Примечание 4. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.
##### Примечание 5. Никаких ограничений касательно реализации класса Row нет, она может быть произвольной.

<table align="center">
  <tbody>
    <tr>
      <th>Sample Input 1: </th>
      <th>Sample Input 2: </th>
      <th>Sample Input 3: </th>
    </tr>
    <tr>
      <td align="center">row = Row(a='A', b='B', c='C')<br>
                        print(row)<br>
                        print(row.a, row.b, row.c)<br></td>
      <td align="center">row1 = Row(a=1, b=2, c=3)<br>
                        row2 = Row(a=1, b=2, c=3)<br>
                        row3 = Row(b=2, c=3, a=1)<br>
                        print(row1 == row2)<br>
                        print(hash(row1) == hash(row2))<br>
                        print(row1 == row3)<br>
                        print(hash(row1) == hash(row3))<br></td>
      <td align="center">row = Row(a=1, b=2, c=3)<br>
                        try:<br>
                            row.d = 4<br>
                        except AttributeError as e:<br>
                            print(e)<br></td>
    </tr>
    <tr>
      <td>Sample Output 1:</td>
      <td>Sample Output 2:</td>
      <td>Sample Output 3:</td>
      </tr>
    <tr>
      <td align="center">
                        Row(a='A', b='B', c='C')<br>
                          A B C<br>
      </td>
      <td align="center">
                        True<br>
                        True<br>
                        False<br>
                        False<br>
      </td>
      <td align="center">
                        Установка нового атрибута невозможна<br>
      </td>
    </tr>
  </tbody>
</table>



## Примеры решений:
* Первый вариант решения
```python
class Row:
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            object.__setattr__(self, k, v)
    
    def __setattr__(self, __name: str, __value):
            if __name in self.__dict__.keys():
                 raise AttributeError('Изменение значения атрибута невозможно')
            raise AttributeError('Установка нового атрибута невозможна')
    
    def __delattr__(self, __name: str):
        raise AttributeError('Удаление атрибута невозможно')

    def __getattribute__(self, __name: str):
        return object.__getattribute__(self, __name)
    
    @property
    def _fields(self):
        return tuple((k, v) for k,v in self.__dict__.items())

    def __eq__(self, __value: object):
        if isinstance(__value, __class__):
            return self._fields == __value._fields
        return NotImplemented
    
    def __hash__(self) -> int:
        return hash(self._fields)
    
    def __repr__(self) -> str:
        str_args =', '.join([f"{k}='{v}'" if type(v) == str else f"{k}={v}"for k,v in self.__dict__.items()])
        return f'{__class__.__name__}({str_args})'
        
```
* Второй вариант решения

```python
class Row:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)
    
    @property
    def _fields(self):
        return tuple(self.__dict__.items())
    
    def __repr__(self):
        attrs = ', '.join(f'{name}={repr(value)}' for name, value in self._fields)
        return f'Row({attrs})'
    
    def __eq__(self, other):
        if isinstance(other, Row):
            return self._fields == other._fields
        return NotImplemented
    
    def __hash__(self):
        return hash(self._fields)
    
    def __setattr__(self, name, value):
        if hasattr(self, name):
            raise AttributeError('Изменение значения атрибута невозможно')
        raise AttributeError('Установка нового атрибута невозможна')
    
    def __delattr__(self, name):
        raise AttributeError('Удаление атрибута невозможно')
```


