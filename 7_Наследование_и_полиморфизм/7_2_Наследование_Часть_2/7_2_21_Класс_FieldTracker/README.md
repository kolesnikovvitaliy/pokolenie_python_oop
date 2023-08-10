<h2 style="text-align:center">Класс FieldTracker</h2>


### Реализуйте класс FieldTracker, наследники которого получают возможность отслеживать состояние определенных атрибутов своих экземпляров класса. Дочерние классы должны наследовать четыре метода экземпляра:
* base() — метод, принимающий в качестве аргумента имя атрибута и возвращающий либо текущее значение этого атрибута, либо исходное (указанное при определении) значение этого атрибута, если оно было изменено
* has_changed() — метод, принимающий в качестве аргумента имя атрибута и возвращающий True, если значение этого атрибута было изменено хотя бы раз, или False в противном случае
* changed() — метод, возвращающий словарь, в котором ключами являются имена атрибутов, которые изменяли свои значения, а значениями — их исходные значения
* save() — метод, сбрасывающий отслеживание. После вызова метода считается, что все атрибуты ранее не изменяли свои значения, а их текущие значения считаются исходными
#### Гарантируется, что наследники класса FieldTracker:
* всегда имеют атрибут класса fields, содержащий кортеж с атрибутами, которые необходимо отслеживать
* в своем инициализаторе всегда вызывают инициализатор класса FieldTracker после установки первичных значений отслеживаемым атрибутам


##### Примечание 1. Будем считать, что атрибут изменяет свое значение только в том случае, если устанавливаемое значение отличается от текущего.
##### Примечание 2. Реализация класса FieldTracker может быть произвольной, то есть требований к наличию определенных атрибутов нет.
##### Примечание 3. Дополнительная проверка данных на корректность в методах не требуется. Гарантируется, что реализованный класс используется только с корректными данными.

<table align="center">
  <tbody>
    <tr>
      <th>Sample Input 1: </th>
      <th>Sample Input 2: </th>
      <th>Sample Input 3: </th>
    </tr>
    <tr>
      <td align="center">class Point(FieldTracker):<br>
                            fields = ('x', 'y', 'z')<br>
                            def __init__(self, x, y, z):<br>
                                self.x, self.y, self.z = x, y, z<br>
                                super().__init__()<br>
                        point = Point(1, 2, 3)<br>
                        print(point.base('x'))<br>
                        print(point.has_changed('x'))<br>
                        print(point.changed())<br></td>
      <td align="center">class Point(FieldTracker):<br>
                              fields = ('x', 'y', 'z')<br>
                              def __init__(self, x, y, z):<br>
                                  self.x, self.y, self.z = x, y, z<br>
                                  super().__init__()<br>
                          point = Point(1, 2, 3)<br>
                          point.x = 0<br>
                          point.z = 4<br>
                          point.z = 5<br>
                          print(point.base('x'))<br>
                          print(point.base('z'))<br>
                          print(point.has_changed('x'))<br>
                          print(point.has_changed('z'))<br>
                          print(point.changed())<br></td>
      <td align="center">class Point(FieldTracker):<br>
                              fields = ('x', 'y', 'z')<br>
                              def __init__(self, x, y, z):<br>
                                  self.x, self.y, self.z = x, y, z<br>
                                  super().__init__()<br>
                          point = Point(1, 2, 3)<br>
                          point.x = 0<br>
                          point.z = 4<br>
                          point.save()<br>
                          print(point.base('x'))<br>
                          print(point.base('z'))<br>
                          print(point.has_changed('x'))<br>
                          print(point.has_changed('z'))<br>
                          print(point.changed())<br></td>
    </tr>
    <tr>
      <td>Sample Output 1:</td>
      <td>Sample Output 2:</td>
      <td>Sample Output 3:</td>
      </tr>
    <tr>
      <td align="center">
                        1<br>
                        False<br>
                        {}<br>
      </td>
      <td align="center">
                        1<br>
                        3<br>
                        True<br>
                        True<br>
                        {'x': 1, 'z': 3}<br>
      </td>
      <td align="center">
                        0<br>
                        4<br>
                        False<br>
                        False<br>
                        {}6<br>
      </td>
    </tr>
  </tbody>
</table>



## Примеры решений:
* Первый вариант решения
```python
class FieldTracker:
    def __init__(self):
        self.lst = {k: v for k, v in self.__dict__.items()}

    def base(self, arg):
        return self.lst[arg]

    def has_changed(self, arg):
        return self.__dict__[arg] != self.lst[arg]

    def changed(self):
        return {k: v for k, v in self.lst.items() if self.__dict__[k] != v}

    def save(self):
        self.lst = {k: v for k, v in self.__dict__.items() if k != 'lst'}
```
* Второй вариант решения

```python
class FieldTracker:
    def __init__(self):
        self._values = {
            field: getattr(self, field)
            for field in self.fields
        }

    def base(self, field):
        return self._values[field]

    def has_changed(self, field):
        return self._values[field] != getattr(self, field)

    def changed(self):
        return {
            field: self.base(field)
            for field in self.fields
            if self.has_changed(field)
        }

    def save(self):
        for field in self.fields:
            self._values[field] = getattr(self, field)
```


