<h2 style="text-align:center">Декоратор @CountCalls</h2>

### Реализуйте декоратор @CountCalls, который считает количество вызовов декорируемой функции. Счетчик вызовов должен быть доступен по атрибуту calls.

##### Примечание 1. Не забывайте про то, что декоратор не должен поглощать возвращаемое значение декорируемой функции, а также должен уметь декорировать функции с произвольным количеством позиционных и именованных аргументов.
##### Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимый декоратор @CountCalls, но не код, вызывающий его.

<table align="center">
  <tbody>
    <tr>
      <th>Sample Input 1: </th>
      <th>Sample Input 2: </th>
    </tr>
    <tr>
      <td align="center">@CountCalls<br>
                          def add(a, b):<br>
                              return a + b<br>
                          print(add(1, 2))<br>
                          print(add(2, 3))<br>
                          print(add.calls)<br></td>
      <td align="center">@CountCalls<br>
                        def square(a):<br>
                            return a ** 2<br>
                        for i in range(100):<br>
                            square(i)<br>
                        print(square.calls)<br></td>
    </tr>
    <tr>
      <td>Sample Output 1:</td>
      <td>Sample Output 2:</td>
      </tr>
    <tr>
      <td align="center">
                        3<br>
                        5<br>
                        2<br>
      </td>
      <td align="center">
                        100<br>
      </td>
    </tr>
  </tbody>
</table>



## Примеры решений:
* Первый вариант решения
```python
class CountCalls:
    calls = 0
    def __init__(self, func):
        self.func = func
    def __call__(self, *args, **kwargs):
            self.calls +=1
            return self.func(*args, **kwargs)
```
* Второй вариант решения

```python
def CountCalls(func):
    def wrapper(*args, **kwargs):
        wrapper.calls += 1
        value = func(*args, **kwargs)
        return value
    wrapper.calls = 0
    return wrapper
```


