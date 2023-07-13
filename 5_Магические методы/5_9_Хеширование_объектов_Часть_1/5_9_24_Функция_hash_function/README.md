<h2 style="text-align:center">Функция hash_function()</h2>

### Реализуйте функцию hash_function(), которая принимает один аргумент:
* obj — произвольный объект
#### Функция должна вычислять хеш-значение объекта obj согласно следующему алгоритму:
#### 1. вычисление значения выражения:
> ord(obj[0]) * ord(obj[-1]) + ord(obj[1]) * ord(obj[-2]) + ord(obj[2]) * ord(obj[-3]) + ...
#### где obj — объект, преобразованный в строку с помощью функции str(). Обратите внимание, что суммироваться должны произведения первого и последнего элементов, второго и предпоследнего, и так далее до середины. Если obj имеет нечетное количество символов, то серединный элемент должен прибавляться без перемножения
#### 2. вычисление значения выражения:
> ord(obj[0]) * 1 - ord(obj[1]) * 2 + ord(obj[2]) * 3 - ord(obj[3]) * 4 + ...
#### где obj — объект, преобразованный в строку с помощью функции str()
#### 3. вычисление значения выражения:
> (temp1 * temp2) % 123456791
#### где temp1 — значение, полученное в первом шаге, temp2 — значение, полученное во втором шаге и возвращать значение, полученное в третьем шаге.

##### Примечание 1. В тестирующую систему сдайте программу, содержащую только необходимую функцию hash_function(), но не код, вызывающий ее.

<table align="center">
  <tbody>
    <tr>
      <th>Sample Input 1: </th>
      <th>Sample Input 2: </th>
      <th>Sample Input 3: </th>
    </tr>
    <tr>
      <td align="center">print(hash_function('python'))<br></td>
      <td align="center">print(hash_function(12345))<br></td>
      <td align="center">print(hash_function(None))<br></td>
    </tr>
    <tr>
      <td>Sample Output 1:</td>
      <td>Sample Output 2:</td>
      <td>Sample Output 3:</td>
      </tr>
    <tr>
      <td align="center">
                        111998846<br>
      </td>
      <td align="center">
                        834432<br>
      </td>
      <td align="center">
                        119077607<br>
      </td>
    </tr>
  </tbody>
</table>



## Примеры решений:
* Первый вариант решения
```python
def hash_function(obj):
    a = str(obj)
    temp2 = 0
    temp1 = 0

    if len(a) % 2 == 0:
        temp1 = sum(ord(a[i]) * ord(a[-i-1]) for i in range(int(len(a)/2)))
    else:
        temp1 = sum(ord(a[i]) * ord(a[-i-1]) for i in range(int(len(a)/2))) + ord(a[int(len(a)/2)])

    for k,v in enumerate(a, 1):
        if k % 2 != 0:
            temp2 += ord(v)*k
        else:
            temp2 -= ord(v)*k
       
    return (temp1 * temp2) % 123456791
```
* Второй вариант решения

```python
def hash_function(obj):
    obj = str(obj)
    temp1 = temp2 = 0
    for i in range(len(obj) // 2):
        temp1 += ord(obj[i]) * ord(obj[-(i + 1)])
    if len(obj) % 2:
        temp1 += ord(obj[len(obj) // 2])
    for i, c in enumerate(obj, 1):
        temp2 += ord(c) * i * ((-1) ** (i + 1))
    return temp1 * temp2 % 123456791
```


