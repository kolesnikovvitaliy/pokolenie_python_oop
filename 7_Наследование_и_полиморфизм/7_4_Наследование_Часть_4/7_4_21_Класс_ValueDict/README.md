<h2 style="text-align:center">Класс ValueDict</h2>

### Реализуйте класс ValueDict, наследника класса dict, описывающий словарь c дополнительным функционалом. Процесс создания экземпляра класса ValueDict должен совпадать с процессом создания экземпляра класса dict.
#### Класс ValueDict должен иметь два метода экземпляра:
* key_of() — метод, принимающий в качестве аргумента объект value и возвращающий первый ключ экземпляра класса ValueDict, имеющий значение value. Если такого ключа нет, метод должен вернуть None.
* keys_of() — метод, принимающий в качестве аргумента объект value и возвращающий итерируемый объект, элементами которого являются все ключи экземпляра класса ValueDict, имеющие значение value

##### Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.
##### Примечание 2. Никаких ограничений касательно реализации класса ValueDict нет, она может быть произвольной.

<table align="center">
  <tbody>
    <tr>
      <th>Sample Input 1: </th>
      <th>Sample Input 2: </th>
      <th>Sample Input 3: </th>
    </tr>
    <tr>
      <td align="center">valuedict = ValueDict({'apple': 1, 'banana': 2, 'orange': 2})<br>
                          print(valuedict.key_of(2))<br>
                          print(*valuedict.keys_of(2))<br></td>
      <td align="center">countries = {'Monaco': 'Monaco', 'Iceland': 'Reykjavik', 'Kenya': 'Nairobi',<br>
                        'Kazakhstan':  'Nur-Sultan',<br>
                              'Mali': 'Bamako', 'Colombia': 'Bogota', 'Finland': 'Helsinki', 'Costa Rica': 'San Jose',<br>
                              'Cuba': 'Havana', 'France': 'Paris', 'Gabon': 'Libreville', 'Liberia': 'Monrovia',<br>
                              'Angola': 'Luanda', 'India': 'New Delhi', 'Canada': 'Ottawa', 'Australia': 'Canberra'}<br>
                  valuedict = ValueDict(countries)<br>
                  print(valuedict.key_of('Moscow'))<br>
                  print(*valuedict.keys_of('Washington'))<br></td>
      <td align="center">valuedict = ValueDict({})<br>
                          print(valuedict.key_of(12))<br>
                          print(*valuedict.keys_of(33))<br></td>
    </tr>
    <tr>
      <td>Sample Output 1:</td>
      <td>Sample Output 2:</td>
      <td>Sample Output 3:</td>
      </tr>
    <tr>
      <td align="center">
                        banana<br>
                        banana orange<br>
      </td>
      <td align="center">
                        None<br>
      </td>
      <td align="center">
                        None<br>
      </td>
    </tr>
  </tbody>
</table>



## Примеры решений:
* Первый вариант решения
```python
class ValueDict(dict):
    def key_of(self, value):
        if value in self.values():
            for k, v in self.items():
                if v == value:
                    return k
        else:
            return None

    def keys_of(self, value):
        if value in self.values():
            return [i[0] for i in self.items() if int(i[1]) == value]
        return iter([])
```
* Второй вариант решения

```python
class ValueDict(dict):
    def key_of(self, value):
        return next(self.keys_of(value), None)
    
    def keys_of(self, value):
        return (i for i, j in self.items() if j == value)
```


