<h2 style="text-align:center">Pycon</h2>

### Каждый месяц в Сан-Диего организовывается встреча любителей Python, которая проходит в четвертый четверг месяца.
#### Напишите программу, которая определяет день проведения очередной встречи питонистов в Сан-Диего.


#### Формат входных данных
##### На вход программе подается два натуральных числа, представляющие год и месяц, каждое на отдельной строке.
#### Формат выходных данных
##### Программа должна определить день проведения встречи в Сан-Диего в указанных году и месяце и вывести результат в формате DD.MM.YYYY.
#### Примечание 1. Гарантируется, что подаваемые год и месяц всегда корректны.

<table align="center">
  <tbody>
    <tr>
      <th>Sample Input 1: </th>
      <th>Sample Input 2: </th>
      <th>Sample Input 3:</th>
    </tr>
    <tr>
      <td align="center">2012<br>
                        3<br></td>
      <td align="center">2015<br>
                        2<br></td>
      <td align="center">2018<br>
                        6<br></td>
    </tr>
    <tr>
      <td>Sample Output 1:</td>
      <td>Sample Output 2:</td>
      <td>Sample Output 3:</td>
    </tr>
    <tr>
      <td align="center">
      22.03.2012<br>
      </td>
      <td align="center">
      26.02.2015<br>
      </td>
      <td align="center">
      28.06.2018<br>
      </td>
    </tr>
  </tbody>
</table>

## Примеры решений:
* Первый вариант решения
```python
from datetime import datetime
import calendar

year, month = [*map(int,(input() for i in range(2)))]
list_date = []
for i in range(1, calendar.monthrange(year, month)[1]+1):
    date = datetime(year, month, i)
    if date.weekday() == 3:
        list_date.append(date.strftime('%d.%m.%Y'))
print(list_date[3])
```
* Второй вариант решения
```python
from datetime import date, timedelta

year, month = int(input()), int(input())
d = date(year, month, 1)

while d.isoweekday() != 4:
    d += timedelta(days=1)

d += timedelta(days=21)
print(d.strftime('%d.%m.%Y'))
```


