<h2 style="text-align:center">Класс AttrsNumberObject</h2>

### Реализуйте класс AttrsNumberObject. При создании экземпляра класс должен принимать произвольное количество именованных аргументов. Все передаваемые аргументы должны устанавливаться создаваемому экземпляру в качестве атрибутов.

#### Экземпляр класса AttrsNumberObject должен иметь один атрибут:
* attrs_num — количество атрибутов, которыми обладает экземпляр класса AttrsNumberObject на данный момент, включая сам атрибут attrs_num

##### Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.
##### Примечание 2. Никаких ограничений касательно реализации класса AttrsNumberObject нет, она может быть произвольной.

<table align="center">
  <tbody>
    <tr>
      <th>Sample Input 1: </th>
      <th>Sample Input 2: </th>
      <th>Sample Input 3: </th>
      <th>Sample Input 4: </th>
    </tr>
    <tr>
      <td align="center">music_group = AttrsNumberObject(name='Silent Poets', genre='acid jazz')<br>
                          print(music_group.attrs_num)<br></td>
      <td align="center">music_group = AttrsNumberObject()<br>
                        print(music_group.attrs_num)<br></td>
      <td align="center">music_group = AttrsNumberObject(name='Woodkid', genre='pop')<br>
                          print(music_group.attrs_num)<br>
                          music_group.country = 'France'<br>
                          print(music_group.attrs_num)<br></td>
      <td align="center">music_group = AttrsNumberObject(name='Alexandra Savior', genre='dream pop')<br>
                          print(music_group.attrs_num)<br>
                          del music_group.genre<br>
                          print(music_group.attrs_num)<br></td>
    </tr>
    <tr>
      <td>Sample Output 1:</td>
      <td>Sample Output 2:</td>
      <td>Sample Output 3:</td>
      <td>Sample Output 4:</td>
      </tr>
    <tr>
      <td align="center">
                        3<br>
      </td>
      <td align="center">
                        1<br>
      </td>
      <td align="center">
                        3<br>
                        4<br>
      </td>
      <td align="center">
                        3<br>
                        2<br>
      </td>
    </tr>
  </tbody>
</table>



## Примеры решений:
* Первый вариант решения
```python
class AttrsNumberObject:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)
        self.attrs_num = 0
            
    def __setattr__(self, __name, __value):
        return object.__setattr__(self, __name, __value)

    def __getattribute__(self, __name: str):
        if __name == 'attrs_num':
            return len(self.__dict__)
        return object.__getattribute__(self, __name)
```
* Второй вариант решения

```python
class AttrsNumberObject:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)
    
    def __getattr__(self, name):
        if name == 'attrs_num':
            return len(self.__dict__) + 1
```


