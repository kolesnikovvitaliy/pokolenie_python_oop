<h2 style="text-align:center">Функция quantify()</h2>

### Реализуйте функцию quantify(), которая принимает два аргумента в следующем порядке:
* iterable — итерируемый объект
* predicate — функция-предикат, то есть функция, возвращающая True или False. Если имеет значение None, то работает аналогично функции bool()

#### Функция quantify() должна считать, для скольких элементов итерируемого объекта iterable функция-предикат predicate вернула значение True, и возвращать полученный результат.
##### Примечание 1. Рассмотрим первый тест, в котором в качестве итерируемого объекта передается список чисел от 1 до 10, в качестве функции-предиката — функция, возвращающая True, если аргумент больше единицы, или False в противном случае. Переданный список чисел содержит ровно 9 чисел, больших единицы.




<table align="center">
  <tbody>
    <tr>
      <th>Sample Input 1: </th>
      <th>Sample Input 2: </th>
      <th>Sample Input 3:</th>
    </tr>
    <tr>
      <td align="center">numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]<br>
                        print(quantify(numbers, lambda x: x > 1))<br></td>
      <td align="center">numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]<br>
                        print(quantify(numbers, lambda x: x % 2 == 0))<br></td>
      <td align="center">numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]<br>
                        print(quantify(numbers, lambda x: x < 0))<br></td>
    </tr>
    <tr>
      <td>Sample Output 1:</td>
      <td>Sample Output 2:</td>
      <td>Sample Output 3:</td>
    </tr>
    <tr>
      <td align="center">
      9<br>
      </td>
      <td align="center">
      5<br>
      </td>
      <td align="center">
      0<br>
      </td>
    </tr>
  </tbody>
</table>

## Примеры решений:
* Первый вариант решения
```python
def quantify(iterable, predicate):
      if predicate == None:
          list_none = []
          for i in iterable:
              list_none.append(bool(i))
          return sum(list_none)
      else:
          return sum(map(predicate,iterable))
```
* Второй вариант решения
```python
def quantify(iterable, predicate):
    return sum(map(predicate if predicate else bool, iterable))
    #return len(list(filter(predicate, iterable)))
```


