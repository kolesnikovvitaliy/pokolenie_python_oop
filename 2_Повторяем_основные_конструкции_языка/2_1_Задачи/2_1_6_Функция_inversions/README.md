<h2 style="text-align:center">Функция inversions()</h2>
<div>
<img src="https://github.com/kolesnikovvitaliy/pokolenie_python_oop/blob/main/2_Повторяем_основные_конструкции_языка/2_1_Задачи/2_1_6_Функция_inversions/img/task.png" title="Git" **alt="Git">
​</div>

### Реализуйте функцию inversions(), которая принимает один аргумент:
* sequence — последовательность, элементами которой являются числа

#### Функция должна возвращать единственное число — количество инверсий в последовательности sequence.
* для каждой открывающей скобки есть закрывающая скобка 
* скобки закрываются в правильном порядке, то есть в каждой паре из открывающей и закрывающей скобок открывающая находится левее
##### Примечание 1. Последовательностью будем считать объект, имеющий длину и поддерживающий индексацию. Например, объекты типа list или range являются последовательностями.
##### Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимую функцию inversions(), но не код, вызывающий ее.





<table align="center">
  <tbody>
    <tr>
      <th>Sample Input 1: </th>
      <th>Sample Input 2: </th>
      <th>Sample Input 3:</th>
    </tr>
    <tr>
      <td align="center">sequence = [3, 1, 4, 2]<br>
            print(inversions(sequence))<br></td>
      <td align="center">sequence = [1, 2, 3, 4, 5]<br>
            print(inversions(sequence))<br></td>
      <td align="center">sequence = [4, 3, 2, 1]<br>
            print(inversions(sequence))</td>
    </tr>
    <tr>
      <td>Sample Output 1:</td>
      <td>Sample Output 2:</td>
      <td>Sample Output 3:</td>
    </tr>
    <tr>
      <td align="center">
      3<br>
      </td>
      <td align="center">
      0<br>
      </td>
      <td align="center">
      6<br>
      </td>
    </tr>
  </tbody>
</table>

## Примеры решений:
* Первый вариант решения
```python
def inversions(sequence:list):
    count = 0
    for i in range(len(sequence)):
        for j in range(len(sequence)):
            if sequence[i] > sequence[j] and i < j:
                count += 1
    return count
```
* Второй вариант решения
```python
from itertools import starmap, combinations

def inversions(sp):
    return sum(starmap(lambda x, y: x > y, combinations(sp, 2)))
```


