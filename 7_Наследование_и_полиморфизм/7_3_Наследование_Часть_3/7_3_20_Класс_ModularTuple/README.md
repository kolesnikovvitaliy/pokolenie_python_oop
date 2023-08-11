<h2 style="text-align:center">Класс ModularTuple</h2>

### Реализуйте класс ModularTuple, наследника класса tuple, описывающий кортеж, элементы которого во время создания автоматически делятся с остатком на заданное число. При создании экземпляра класс должен принимать два аргумента в следующем порядке:
* iterable — итерируемый объект, определяющий начальный набор элементов экземпляра класса ModularTuple. Если не передан, начальный набор элементов считается пустым
* size — целое число, на которое делятся с остатком все элементы создаваемого экземпляра класса ModularTuple, по умолчанию имеет значение 100

##### Примечание 1. Экземпляр класса ModularTuple не должен зависеть от итерируемого объекта, на основе которого он был создан. Другими словами, если исходный итерируемый объект изменится, то экземпляр класса ModularTuple измениться  не должен.
##### Примечание 2. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.
##### Примечание 3. Никаких ограничений касательно реализации класса ModularTuple нет, она может быть произвольной.

<table align="center">
  <tbody>
    <tr>
      <th>Sample Input 1: </th>
      <th>Sample Input 2: </th>
    </tr>
    <tr>
      <td align="center">modulartuple = ModularTuple([101, 102, 103, 104, 105])<br>
                        print(modulartuple)<br>
                        print(type(modulartuple))<br></td>
      <td align="center">modulartuple = ModularTuple([1, 2, 3, 4, 5], 2)<br>
                        print(modulartuple)<br></td>
    </tr>
    <tr>
      <td>Sample Output 1:</td>
      <td>Sample Output 2:</td>
      </tr>
    <tr>
      <td align="center">
                        (1, 2, 3, 4, 5)<br>
                        class '__main__.ModularTuple'<br>
      </td>
      <td align="center">
                        (1, 0, 1, 0, 1)<br>
      </td>
    </tr>
  </tbody>
</table>



## Примеры решений:
* Первый вариант решения
```python
class ModularTuple(tuple):
    def __new__(cls, iterable=(), size=100):
        if iterable:
            return super().__new__(cls, tuple(i % size for i in iterable))
        return ()
```
* Второй вариант решения

```python
class ModularTuple(tuple):
    def __new__(cls, iterable=(), size=100, *args, **kwargs):
        iterable = map(lambda item: item % size, iterable)
        instance = super().__new__(cls, iterable)
        return instance
```


