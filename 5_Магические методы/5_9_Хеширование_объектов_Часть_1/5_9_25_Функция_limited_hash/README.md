<h2 style="text-align:center">Функция limited_hash()</h2>

### Реализуйте функцию limited_hash(), которая принимает три аргумента в следующем порядке:
* left — целое число
* right — целое число
* hash_function — хеш-функция, по умолчанию равняется встроенной функции hash()
#### Функция должна возвращать новую функцию, которая принимает в качестве аргумента произвольный объект, вычисляет его хеш-значение с помощью функции hash_function(), преобразует его в число, принадлежащее диапазону [left; right], и возвращает полученный результат.

#### Если вычисленное хеш-значение уже принадлежит диапазону [left; right], то функция должна возвращать его без преобразования. Если вычисленное хеш-значение равняется right + 1, то функция перед возвратом должна преобразовать его в left, если right + 2 — в left + 1, если right + 3 — в left + 2, и так далее. Аналогичные преобразования, но в другую сторону, должны выполняться для хеш-значений, которые меньше left. Преобразования должны выполняться циклично при очередном выходе из диапазона.

##### Примечание 1. В тестирующую систему сдайте программу, содержащую только необходимую функцию limited_hash(), но не код, вызывающий ее.

<table align="center">
  <tbody>
    <tr>
      <th>Sample Input 1: </th>
      <th>Sample Input 2: </th>
      <th>Sample Input 3: </th>
    </tr>
    <tr>
      <td align="center">hash_function = limited_hash(10, 15)<br>
                          print(hash_function(10))<br>
                          print(hash_function(11))<br>
                          print(hash_function(15))<br></td>
      <td align="center">hash_function = limited_hash(10, 15)<br>
                          print(hash_function(16))<br>
                          print(hash_function(17))<br>
                          print(hash_function(21))<br>
                          print(hash_function(22))<br>
                          print(hash_function(23))<br></td>
      <td align="center">hash_function = limited_hash(10, 15)<br>
                          print(hash_function(9))<br>
                          print(hash_function(8))<br>
                          print(hash_function(4))<br>
                          print(hash_function(3))<br>
                          print(hash_function(2))<br></td>
    </tr>
    <tr>
      <td>Sample Output 1:</td>
      <td>Sample Output 2:</td>
      <td>Sample Output 3:</td>
      </tr>
    <tr>
      <td align="center">
                        10<br>
                        11<br>
                        15<br>
      </td>
      <td align="center">
                        10<br>
                        11<br>
                        15<br>
                        10<br>
                        11<br>
      </td>
      <td align="center">
                        15<br>
                        14<br>
                        10<br>
                        15<br>
                        14<br>
      </td>
    </tr>
  </tbody>
</table>



## Примеры решений:
* Первый вариант решения
```python
def limited_hash(left, right, hash_function=hash):
    def wrapper(obj):
        res  = hash_function(obj)
        while res not in range(left, right+1):
            if res > right:
                res =  left + res-right-1
            elif res < left:
                res = right + res- left + 1
        return res
    return wrapper
```
* Второй вариант решения

```python
def limited_hash(left, right, hash_function=hash):
    def inner_hash_function(x):
        return left + (hash_function(x) - left) % (right - left + 1)
    return inner_hash_function
```


