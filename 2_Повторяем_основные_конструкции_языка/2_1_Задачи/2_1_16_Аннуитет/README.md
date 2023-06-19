<h2 style="text-align:center">Аннуитет</h2>

### Практически каждый человек знаком с финансовыми инвестициями, целью которых является преумножение имеющихся средств в течение некоторого времени. Наиболее простым примером является банковский вклад, который ежегодно увеличивается путем начисления на него определенного числа процентов. Составляющими такого банковского вклада являются начальная сумма вклада, процентная ставка и срок вклада.
### Чтобы понять, каким образом меняется размер вклада и происходит начисление процентов, рассмотрим следующую задачу: Вкладчик открыл счёт в банке, разместив сумму в 120000 рублей под 10% годовых. Какая сумма будет на счёте через 3 года?

#### Решение. В конце каждого года размер вклада увеличивается на 10%. Согласно условию задачи имеем:
<div>
<img style="text-align: center;" src="https://github.com/kolesnikovvitaliy/pokolenie_python_oop/blob/main/2_Повторяем_основные_конструкции_языка/2_1_Задачи/2_1_16_Аннуитет/img/task.png" title="Git" **alt="Git">
​</div>

#### Ответ: 159720 рублей.
### Реализуйте генераторную функцию annual_return(), которая принимает три аргумента в следующем порядке:
* start — целое число, начальная сумма вклада в рублях
* percent — целое число, процент, на который текущая сумма вклада будет увеличиваться каждый год
* years — целое число, количество лет, в течение которых будут начисляться проценты

##### Функция должна возвращать итератор, моделирующий банковский вклад. Возвращаемыми значениями итератора должны являться размеры вклада после очередного начисления процентов percent.






<table align="center">
  <tbody>
    <tr>
      <th>Sample Input 1: </th>
      <th>Sample Input 2: </th>
      <th>Sample Input 3:</th>
    </tr>
    <tr>
      <td align="center">for value in annual_return(120000, 10, 3):<br>
                              print(round(value))<br></td>
      <td align="center">for value in annual_return(70000, 8, 10):<br>
                                        print(round(value))<br></td>
      <td align="center">for value in annual_return(0, 0, 10):<br>
                                print(round(value))<br></td>
    </tr>
    <tr>
      <td>Sample Output 1:</td>
      <td>Sample Output 2:</td>
      <td>Sample Output 3:</td>
    </tr>
    <tr>
      <td align="center">
      132000<br>
      145200<br>
      159720<br>
      </td>
      <td align="center">
      75600<br>
      81648<br>
      88180<br>
      95234<br>
      102853<br>
      111081<br>
      119968<br>
      129565<br>
      139930<br>
      151125<br>
      </td>
      <td align="center">
      0<br>
      0<br>
      0<br>
      0<br>
      0<br>
      0<br>
      0<br>
      0<br>
      0<br>
      0<br>
      </td>
    </tr>
  </tbody>
</table>

## Примеры решений:
* Первый вариант решения
```python
def annual_return(start, percent, years):
    for i in range(years):
        start = ((start/100) * percent) + start
        yield start
```
* Второй вариант решения
```python
from typing import Iterator

def annual_return(start: int, percentage: int, years: int) -> Iterator:
    return (start := start * ((percentage + 100) / 100) for _ in range(years))
```


