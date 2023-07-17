<h2 style="text-align:center">Класс SparseArray</h2>


### Разреженный массив (список) — абстрактное представление обычного массива (списка), в котором данные представлены не непрерывно, а фрагментарно: большинство его элементов принимает одно и то же значение по умолчанию, обычно 0 или None. В разреженном массиве возможен доступ к неопределенным элементам, в этом случае массив вернет некоторое значение по умолчанию.
### Реализуйте класс SparseArray, описывающий разреженный массив. При создании экземпляра класс должен принимать один аргумент:
* default — значение по умолчанию для неопределенных элементов разреженного массива
#### Экземпляр класса SparseArray должен позволять получать и изменять значения своих элементов с помощью индексов. При попытке получить значение элемента по несуществующему индексу должно быть возвращено значение по умолчанию.
##### Примечание 1. Гарантируется, что при доступе к элементам используются только неотрицательные индексы.
##### Примечание 2. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.
#### Примечание 3. Никаких ограничений касательно реализации класса SparseArray нет, она может быть произвольной.

<table align="center">
  <tbody>
    <tr>
      <th>Sample Input 1: </th>
      <th>Sample Input 2: </th>
    </tr>
    <tr>
      <td align="center">array = SparseArray(0)<br>
                          array[5] = 1000<br>
                          array[12] = 1001<br>
                          print(array[5])<br>
                          print(array[12])<br>
                          print(array[13])<br></td>
      <td align="center">array = SparseArray(None)<br>
                        array[0] = 'Timur'<br>
                        array[1] = 'Arthur'<br>
                        print(array[0])<br>
                        print(array[1])<br>
                        print(array[2])<br></td>
    </tr>
    <tr>
      <td>Sample Output 1:</td>
      <td>Sample Output 2:</td>
      </tr>
    <tr>
      <td align="center">
                        1000<br>
                        1001<br>
                        0<br>
      </td>
      <td align="center">
                        Timur<br>
                        Arthur<br>
                        None<br>
      </td>
    </tr>
  </tbody>
</table>



## Примеры решений:
* Первый вариант решения
```python
class  SparseArray:
    def __init__(self, default=None):
        self.array = []
        self.default = default
    
    def __setitem__(self, key, value):
        i = len(self.array)
        while key > len(self.array):
            self.array.insert(i, self.default)
            i += 1
        self.array.insert(key, value)

    def __getitem__(self, key):
        try:
            return self.array[key]
        except IndexError:
            return self.default
```
* Второй вариант решения

```python
class SparseArray:
    def __init__(self, default):
        self.array = {}
        self.default = default

    def __len__(self):
        return len(self.array)

    def __getitem__(self, key):
        return self.array.get(key, self.default)

    def __setitem__(self, key, value):
        self.array[key] = value
```


