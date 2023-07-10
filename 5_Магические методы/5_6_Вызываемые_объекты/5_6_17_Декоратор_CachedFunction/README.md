<h2 style="text-align:center">Декоратор @CachedFunction</h2>


### Реализуйте декоратор @CachedFunction, который кэширует вычисленные значения декорируемой функции. Кэш должен быть доступен по атрибуту cache и представлять собой словарь, ключом в котором является кортеж с аргументами, а значением — возвращаемое значение декорируемой функции при вызове с этими аргументами.

##### Примечание 1. Для однозначного кеширования гарантируется, что декорируемая функция принимает только позиционные аргументы.
##### Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимый декоратор @CachedFunction, но не код, вызывающий его.

<table align="center">
  <tbody>
    <tr>
      <th>Sample Input 1: </th>
      <th>Sample Input 2: </th>
    </tr>
    <tr>
      <td align="center">@CachedFunction<br>
                          def slow_fibonacci(n):<br>
                              if n == 1:<br>
                                  return 0<br>
                              elif n in (2, 3):<br>
                                  return 1<br>
                              return slow_fibonacci(n - 1) + slow_fibonacci(n - 2)<br>
                          print(slow_fibonacci(100))<br></td>
      <td align="center">@CachedFunction<br>
                        def slow_fibonacci(n):<br>
                            if n == 1:<br>
                                return 0<br>
                            elif n in (2, 3):<br>
                                return 1<br>
                            return slow_fibonacci(n - 1) + slow_fibonacci(n - 2)<br>
                        slow_fibonacci(5)<br>
                        for args, value in sorted(slow_fibonacci.cache.items()):<br>
                            print(args, value)<br></td>
    </tr>
    <tr>
      <td>Sample Output 1:</td>
      <td>Sample Output 2:</td>
      </tr>
    <tr>
      <td align="center">
                        218922995834555169026<br>
      </td>
      <td align="center">
                        (2,) 1<br>
                        (3,) 1<br>
                        (4,) 2<br>
                        (5,) 3<br>
      </td>
    </tr>
  </tbody>
</table>



## Примеры решений:
* Первый вариант решения
```python
class CachedFunction:
    cache = {}
    def __init__(self, func):
        self.func = func
    def __call__(self, *args):
        result = self.cache.get(args)
        if result is None:
            result = self.func(*args)
            self.cache[args] = result
        return result
```
* Второй вариант решения

```python
class CachedFunction:
    def __init__(self, func):
        self.func = func
        self.cache = {}
        
    def __call__(self, *args):
        if args not in self.cache:
            self.cache[args] = self.func(*args)
        return self.cache[args]
```


