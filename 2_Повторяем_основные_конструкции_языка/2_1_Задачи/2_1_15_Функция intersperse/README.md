<h2 style="text-align:center">Функция intersperse()</h2>

### Реализуйте генераторную функцию intersperse(), которая принимает два аргумента в следующем порядке:
* iterable — итерируемый объект
* delimiter — значение-разделитель
#### Функция должна возвращать генератор, порождающий последовательность из элементов итерируемого объекта iterable, между которыми располагается значение-разделитель delimiter.
##### Примечание 1. Рассмотрим первый тест, в котором в качестве итерируемого объекта передается список чисел от 1 до 3, а в качестве значения-разделителя — 0. Порождаемая генератором последовательность состоит из чисел 1, 2 и 3, между которыми располагается число 0:
* 1 0 2 0 3






<table align="center">
  <tbody>
    <tr>
      <th>Sample Input 1: </th>
      <th>Sample Input 2: </th>
      <th>Sample Input 3:</th>
    </tr>
    <tr>
      <td align="center">print(*intersperse([1, 2, 3], 0))</td>
      <td align="center">inter = intersperse('beegeek', '!')<br>
                                        print(next(inter))<br>
                                        print(next(inter))<br>
                                        print(*inter)<br></td>
      <td align="center">print(*intersperse('A', '...'))</td>
    </tr>
    <tr>
      <td>Sample Output 1:</td>
      <td>Sample Output 2:</td>
      <td>Sample Output 3:</td>
    </tr>
    <tr>
      <td align="center">
      1 0 2 0 3<br>
      </td>
      <td align="center">
      b<br>
      !<br>
      e ! e ! g ! e ! e ! k<br>
      </td>
      <td align="center">
      A<br>
      </td>
    </tr>
  </tbody>
</table>

## Примеры решений:
* Первый вариант решения
```python
def intersperse(iterable, delimiter):
    iter = list(iterable)
    a = []
    for i in range(len(iter)):
        a.append(iter[i])
        if i != iter.index(iter[-1]):
            a.append(delimiter)
    for i in a:
        yield i
```
* Второй вариант решения
```python
def intersperse(iterable, delimiter):
    first = True
    for item in iterable:
        if not first:
            yield delimiter
        first = False
        yield item
```


