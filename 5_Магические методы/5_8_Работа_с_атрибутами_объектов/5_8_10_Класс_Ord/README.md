<h2 style="text-align:center">Класс Ord</h2>

### Реализуйте класс Ord. При создании экземпляра класс не должен принимать никаких аргументов.
#### Экземпляр класса Ord должен выступать в качестве альтернативы функции ord(). При обращении к атрибуту экземпляра, именем которого является одиночный символ, должна возвращаться его позиция в таблице символов Unicode.

##### Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.
##### Примечание 2. Никаких ограничений касательно реализации класса Ord нет, она может быть произвольной.



<table align="center">
  <tbody>
    <tr>
      <th>Sample Input 1: </th>
      <th>Sample Input 2: </th>
    </tr>
    <tr>
      <td align="center">obj = Ord()<br>
                        print(obj.a)<br>
                        print(obj.b)<br></td>
      <td align="center">obj = Ord()<br>
                        print(obj.в)<br>
                        print(obj.г)<br></td>
    </tr>
    <tr>
      <td>Sample Output 1:</td>
      <td>Sample Output 2:</td>
      </tr>
    <tr>
      <td align="center">
                        97<br>
                        98<br>
      </td>
      <td align="center">
                        1074<br>
                        1075<br>
      </td>
    </tr>
  </tbody>
</table>



## Примеры решений:
* Первый вариант решения
```python
class Ord:
    def __getattribute__(self, __name: str):
        return ord(__name)
```
* Второй вариант решения

```python
class Ord:
    def __getattribute__(self, item):
        if len(item) == 1:
            return ord(item)
        return object.__getattribute__(self, item)
```


