<h2 style="text-align:center">Координаты</h2>
<div>
<img src="https://github.com/kolesnikovvitaliy/pokolenie_python_oop/blob/main/2_Повторяем_основные_конструкции_языка/2_1_Задачи/2_1_9_Координаты/img/task.png" title="Git" **alt="Git">
​</div>

### Напишите программу, которая принимает произвольное количество строк и определяет, какие из них представляют собой корректные географические координаты.

#### Формат входных данных
##### На вход программе подается произвольное количество строк, каждая из которых представляет собой пару чисел в следующем формате:
* (<координата x>, <координата y>)

#### Формат выходных данных
##### Программа должна для каждой строки вывести True, если она представляет собой корректные географические координаты, или False в противном случае.




<table align="center">
  <tbody>
    <tr>
      <th>Sample Input 1: </th>
      <th>Sample Input 2: </th>
      <th>Sample Input 3:</th>
    </tr>
    <tr>
      <td align="center">(75, 180)<br>
                        (90, -147.45)<br>
                        (77.111, 149.9999)<br>
                        (90, 180)<br>
                        (55.1, 249.9)<br>
                        (120, 150)<br></td>
      <td align="center">(-90, -180)<br>
                        (-90.0, -180.0)<br>
                        (-90, 180)<br>
                        (90, -180)<br>
                        (90.0, 180.0)<br></td>
      <td align="center">(-90.1, 1)<br>
                          (-90.2, 45)<br>
                          (10, 180.01)<br>
                          (1, 180.0004)<br></td>
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
      True<br>
      True<br>
      False<br>
      False<br>
      </td>
      <td align="center">
      True<br>
      True<br>
      True<br>
      True<br>
      True<br>
      </td>
      <td align="center">
      False<br>
      Falsev<br>
      False<br>
      False<br>
      </td>
    </tr>
  </tbody>
</table>

## Примеры решений:
* Первый вариант решения
```python
import sys

coordinates = [coordinate.strip() for coordinate in sys.stdin]

date = [[*list(map(lambda k: float(k),coordinate[1:-1].split(", ")))] for coordinate in coordinates]

for x, y in date:
    if abs(x) <= 90 and abs(y) <= 180:
        print(True)
    else:
        print(False)
```
* Второй вариант решения
```python
import sys

axis = [eval(line.strip()) for line in sys.stdin]
for x, y in axis:
    print(-90 <= x <= 90 and -180 <= y <= 180)
```


