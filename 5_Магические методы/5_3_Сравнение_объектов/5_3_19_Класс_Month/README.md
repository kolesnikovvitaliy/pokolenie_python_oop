<h2 style="text-align:center">Класс Month</h2>


### Реализуйте класс Month, описывающий месяц. При создании экземпляра класс должен принимать два аргумента в следующем порядке:
* year — год
* month — порядковый номер месяца
#### Экземпляр класса Month должен иметь следующее формальное строковое представление:
> Month(<год>, <порядковый номер месяца>)
#### И следующее неформальное строковое представление:
> <год>-<порядковый номер месяца>

##### Также экземпляры класса Month должны поддерживать все операции сравнения с помощью операторов ==, !=, >, <, >=, <=. Два Month объекта считаются равными, если их годы и порядковые номера месяцев совпадают. Month объект считается больше другого Month объекта, если его год больше. В случае если два Month объекта имеют равные года, большим считается тот, чей месяц больше. Методы, реализующие операции сравнения, должны уметь сравнивать как два Month объекта между собой, так и Month объект с кортежем из двух чисел, представляющих год и месяц.

##### Примечание 1. Если объект, с которым выполняется операция сравнения, некорректен, метод, реализующий эту операцию, должен вернуть константу NotImplemented.
##### Примечание 2. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.
##### Примечание 3. Никаких ограничений касательно реализации класса Month нет, она может быть произвольной.

<table align="center">
  <tbody>
    <tr>
      <th>Sample Input 1: </th>
      <th>Sample Input 2: </th>
      <th>Sample Input 3: </th>
    </tr>
    <tr>
      <td align="center">print(Month(1999, 12) == Month(1999, 12))<br>
                          print(Month(1999, 12) < Month(2000, 1))<br>
                          print(Month(1999, 12) > Month(2000, 1))<br>
                          print(Month(1999, 12) <= Month(1999, 12))<br>
                          print(Month(1999, 12) >= Month(2000, 1))<br></td>
      <td align="center">months = [Month(1998, 12), Month(2000, 1), Month(1999, 12)]<br>
                          print(sorted(months))<br></td>
      <td align="center">months = [Month(1998, 12), Month(2000, 1), Month(1999, 12)]<br>
                        print(min(months))<br>
                        print(max(months))<br></td>
    </tr>
    <tr>
      <td>Sample Output 1:</td>
      <td>Sample Output 2:</td>
      <td>Sample Output 3:</td>
      </tr>
    <tr>
      <td align="center">
                        True<br>
                        True<br>
                        False<br>
                        True<br>
                        False<br>
      </td>
      <td align="center">
                        [Month(1998, 12), Month(1999, 12), Month(2000, 1)]<br>
      </td>
      <td align="center">
                        1998-12<br>
                        2000-1<br>
      </td>
    </tr>
  </tbody>
</table>



## Примеры решений:
* Первый вариант решения
```python
from functools import total_ordering


@total_ordering
class Month:
    def __init__(self, year: int, data: int) -> None:
        self.year = year
        self.month = data

    def __str__(self) -> str:
        return f"{self.year}-{self.month}"
    
    def __repr__(self) -> str:
        return f'{__class__.__name__}({repr((self.year))}, {self.month})'

    def __eq__(self, __value: object) -> bool:
        if isinstance(__value, tuple) and len(__value) == 2:
            return self.year == __value[0] and self.month == __value[1]
        elif isinstance(__value, Month):
            return self.year == __value.year and self.month == __value.month
        return NotImplemented

    def __lt__(self, __value: object) -> bool:
        if isinstance(__value, tuple) and len(__value) == 2:
            return self.year < __value[0] or (self.year == __value[0] and self.month < __value[1])
        elif isinstance(__value, Month):
            return self.year < __value.year or (self.year == __value.year and self.month < __value.month)
        return NotImplemented
```
* Второй вариант решения

```python
from functools import total_ordering


@total_ordering
class Month:
    def __init__(self, year, month):
        self.year = year
        self.month = month

    def __str__(self):
        return f'{self.year}-{self.month}'

    def __repr__(self):
        return f"Month({self.year}, {self.month})"

    def __eq__(self, other):
        if isinstance(other, Month):
            return (self.year, self.month) == (other.year, other.month)
        elif isinstance(other, tuple):
            return (self.year, self.month) == other
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Month):
            return (self.year, self.month) < (other.year, other.month)
        elif isinstance(other, tuple):
            return (self.year, self.month) < other
        return NotImplemented
```


