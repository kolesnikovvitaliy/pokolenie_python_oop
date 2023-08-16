<h2 style="text-align:center">Класс EasyDict</h2>

### Реализуйте класс EasyDict, наследника класса dict, описывающий словарь, значения элементов которого можно получать как по ключам ([key]), так и по одноименным атрибутам (.key). Процесс создания экземпляра класса EasyDict должен совпадать с процессом создания экземпляра класса dict.

##### Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.
##### Примечание 2. Никаких ограничений касательно реализации класса EasyDict нет, она может быть произвольной.

<table align="center">
  <tbody>
    <tr>
      <th>Sample Input 1: </th>
      <th>Sample Input 2: </th>
      <th>Sample Input 3: </th>
    </tr>
    <tr>
      <td align="center">easydict = EasyDict({'name': 'Timur', 'city': 'Moscow'})<br>
                        print(easydict['name'])<br>
                        print(easydict.city)<br></td>
      <td align="center">easydict = EasyDict({'name': 'Timur', 'city': 'Moscow'})<br>
                          easydict['city'] = 'Dubai'<br>
                          easydict['age'] = 30<br>
                          print(easydict.city)<br>
                          print(easydict.age)<br></td>
      <td align="center">easydict = EasyDict({'name': 'Artur', 'city': 'Almetevsk'})<br>
                          easydict.age = 21<br>
                          print(easydict)<br></td>
    </tr>
    <tr>
      <td>Sample Output 1:</td>
      <td>Sample Output 2:</td>
      <td>Sample Output 3:</td>
      </tr>
    <tr>
      <td align="center">
                        Timur<br>
                        Moscow<br>
      </td>
      <td align="center">
                        Dubai<br>
                        30<br>
      </td>
      <td align="center">
                        {'name': 'Artur', 'city': 'Almetevsk'}<br>
      </td>
    </tr>
  </tbody>
</table>



## Примеры решений:
* Первый вариант решения
```python
class EasyDict(dict):
    def __init__(self, iterables):
        super().__init__(iterables)
        for k, v in self.items():
            setattr(self, k, v)

    def __setitem__(self, key, value):
        self.__dict__[key] = value
```
* Второй вариант решения

```python
class EasyDict(dict):
    def __getattr__(self, item):
        print(self)
        return self[item]
```


