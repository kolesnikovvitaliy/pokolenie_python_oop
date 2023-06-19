<h2 style="text-align:center">Функция pluck()</h2>

### ПРеализуйте функцию pluck(), которая принимает три аргумента в следующем порядке:
* data — словарь произвольной вложенности
* path — строка, представляющая собой ключ или последовательность ключей, перечисленных через точку .
* default — произвольный объект, значение по умолчанию; имеет значение None, если не передан явно

#### Функция должна возвращать значение по ключу path из словаря data. Если path представляет собой последовательность ключей, например, key1.key2, то возвращаемым значением функции должно быть значение по ключу key2 из словаря data[key1]. Если указанного ключа или хотя бы одного ключа из последовательности ключей в словаре нет, функция должна вернуть значение default.

<table align="center">
  <tbody>
    <tr>
      <th>Sample Input 1: </th>
      <th>Sample Input 2: </th>
      <th>Sample Input 3:</th>
    </tr>
    <tr>
      <td align="center">d = {'a': {'b': 5, 'z': 20}, 'c': {'d': 3}, 'x': 40}<br>
                              print(pluck(d, 'x'))<br></td>
      <td align="center">d = {'a': {'b': 5, 'z': 20}, 'c': {'d': 3}, 'x': 40}<br>
                                        print(pluck(d, 'a.b'))<br></td>
      <td align="center">d = {'a': {'b': {'c': {'d': {'e': 4}}}}}<br>
                                print(pluck(d, 'a.b.c'))<br></td>
    </tr>
    <tr>
      <td>Sample Output 1:</td>
      <td>Sample Output 2:</td>
      <td>Sample Output 3:</td>
    </tr>
    <tr>
      <td align="center">
      40<br>
      </td>
      <td align="center">
      5<br>
      </td>
      <td align="center">
      {'d': {'e': 4}}<br>
      </td>
    </tr>
  </tbody>
</table>

## Примеры решений:
* Первый вариант решения
```python
def pluck(data, path, default=None):
    list_key = path.split('.')
    try:
        for key in range(len(list_key)):
            data = data[list_key[key]]
        return data
    except:
        return default
```
* Второй вариант решения
```python
def pluck(data, path, default=None):
    for key in path.split('.'):
        data = data.get(key, default)
    return data
```


