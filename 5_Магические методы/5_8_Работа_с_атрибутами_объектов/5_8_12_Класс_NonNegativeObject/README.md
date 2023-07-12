<h2 style="text-align:center">Класс NonNegativeObject</h2>


### Реализуйте класс NonNegativeObject. При создании экземпляра класс должен принимать произвольное количество именованных аргументов. Все передаваемые аргументы должны устанавливаться создаваемому экземпляру в качестве атрибутов, причем если значением атрибута является отрицательное число, оно должно быть взято с противоположным знаком.

##### Примечание 1. Числами будем считать экземпляры классов int и float.
##### Примечание 2. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.
##### Примечание 3. Никаких ограничений касательно реализации класса NonNegativeObject нет, она может быть произвольной.

<table align="center">
  <tbody>
    <tr>
      <th>Sample Input 1: </th>
      <th>Sample Input 2: </th>
    </tr>
    <tr>
      <td align="center">point = NonNegativeObject(x=1, y=-2, z=0, color='black')<br>
                          print(point.x)<br>
                          print(point.y)<br>
                          print(point.z)<br>
                          print(point.color)<br></td>
      <td align="center">point = NonNegativeObject(x=1.5, y=-2.3, z=0.0, color='yellow')<br>
                          print(point.x)<br>
                          print(point.y)<br>
                          print(point.z)<br>
                          print(point.color)<br></td>
    </tr>
    <tr>
      <td>Sample Output 1:</td>
      <td>Sample Output 2:</td>
      </tr>
    <tr>
      <td align="center">
                        1<br>
                        2<br>
                        0<br>
                        black<br>
      </td>
      <td align="center">
                        1.5<br>
                        2.3<br>
                        0.0<br>
                        yellow<br>
      </td>
    </tr>
  </tbody>
</table>



## Примеры решений:
* Первый вариант решения
```python
class NonNegativeObject:
    def __init__(self, **kwargs) -> None:
        self.__dict__.update(kwargs)
    
    def __getattribute__(self, __name: str):
        if isinstance(object.__getattribute__(self, __name), (int, float)):
            return abs(object.__getattribute__(self, __name))
        return object.__getattribute__(self, __name)
```
* Второй вариант решения

```python
class NonNegativeObject:
    def __init__(self, **kwargs):
        for name, value in kwargs.items():
            setattr(self, name, value)
        
    def __setattr__(self, name, value):
        if isinstance(value, (int, float)):
            value = abs(value)
        object.__setattr__(self, name, value)
```


