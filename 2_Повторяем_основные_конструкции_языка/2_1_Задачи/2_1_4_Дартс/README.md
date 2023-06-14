<h2 style="text-align:center">Дартс</h2>

#### Будем считать, что игровое поле для игры в дартс представляет собой квадратную матрицу, заполненную натуральными числами, расположенными в порядке возрастания от краев к центру. Стороной игрового поля будем называть сторону квадратной матрицы, которую представляет это поле.

#### Напишите программу, которая создает поле для игры в дартс определенного размера.

### Формат входных данных
#### На вход программе подается единственное натуральное число — сторона игрового поля.

### Формат выходных данных
#### Программа должна создать и вывести игровое поле с заданной стороной.

#### Примечание 1. Гарантируется, что сторона игрового поля не превышает 18.

<table align="center">
  <tbody>
    <tr>
      <th>Sample Input 3: </th>
      <th>Sample Input 4: </th>
      <th>Sample Input 5:</th>
    </tr>
    <tr>
      <td align="center">3</td>
      <td align="center">4</td>
      <td align="center">5</td>
    </tr>
    <tr>
      <td>Sample Output 3:</td>
      <td>Sample Output 4:</td>
      <td>Sample Output 5:</td>
    </tr>
    <tr>
      <td align="center">
      111<br>
      121<br>
      111<br>
      </td>
      <td align="center">
      1 1 1 1<br>
      1 2 2 1<br>
      1 2 2 1<br>
      1 1 1 1<br>
      </td>
      <td align="center">
      1 1 1 1 1<br>
      1 2 2 2 1<br>
      1 2 3 2 1<br>
      1 2 2 2 1<br>
      1 1 1 1 1<br>
      </td>
    </tr>
  </tbody>
</table>

## Примеры решений:
* Первый вариант решения
```python
def make_dartboard_1(n):
    dartboard = []
    for i in range(n):
        result =[]
        for j in range(n):            
            if (i == j and i <= n - 1 - j) or (i <= j and i <= n - 1 - j):
                result.append(i+1)
            elif (i >= j and i <= n - 1 - j):
                result.append(j+1)
            elif (i <= j and i >= n - 1 - j):
                result.append(n - j)
            elif (i >= j and i >= n - 1 - j):
                result.append(n-i)
            else:
                result.append(1)
        dartboard.append(result)
    return dartboard

dartboard_1 = make_dartboard_1(int(input()))

for line in dartboard_1:
    print(*line)
```
* Второй вариант решения
```python
def make_dartboard_2(n):
    mat = [[1] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            mat[i][j] = min(i + 1, j + 1, n - i, n - j)
    return mat

dartboard_2 = make_dartboard_2(int(input()))

for line in dartboard_2:
    print(*line)
```


