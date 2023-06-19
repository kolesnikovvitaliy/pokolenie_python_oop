<h2 style="text-align:center">Декоратор @recviz</h2>

#### Реализуйте декоратор @recviz, который полностью визуализирует выполнение декорируемой функции, в том числе и рекурсивной. Декоратор должен отображать все рекурсивные вызовы и возвращаемые значения, полученные при этих вызовах, причем рекурсивные вызовы, выполняемые в глубину, должны отделяться друг от друга четырьмя пробелами.

#### Очередной вызов декорируемой функции при визуализации должен включать в себя знак ->, имя декорируемой функции и аргументы, переданные при этом вызове. Возвращаемое значение при визуализации должно включать в себя знак <- и непосредственно само возвращаемое значение.

##### Примечание 1. Рекурсивный вызов и возвращаемое значение, полученное при этом вызове, должны находиться на одном уровне отступов.

##### Примечание 2. Не забывайте, что декоратор не должен поглощать возвращаемое значение декорируемой функции, а также должен уметь декорировать функции с произвольным количеством позиционных и именованных аргументов.

<table align="center">
  <tbody>
    <tr>
      <th>Sample Input 1: </th>
      <th>Sample Input 2: </th>
      <th>Sample Input 3:</th>
    </tr>
    <tr>
      <td align="center">@recviz<br>
                          def add(a, b):<br>
                              return a + b<br>
                          add(1, b=2)<br></td>
      <td align="center">@recviz<br>
                          def add(a, b, c, d, e):<br>
                              return (a + b + c) * (d + e)<br>
                          add('a', b='b', c='c', d=3, e=True)<br></td>
      <td align="center">@recviz<br>
                          def fib(n):<br>
                              if n <= 2:<br>
                                  return 1<br>
                              else:<br>
                                  return fib(n - 1) + fib(n - 2)<br>                                  
                          fib(4)<br></td>
    </tr>
    <tr>
      <td>Sample Output 1:</td>
      <td>Sample Output 2:</td>
      <td>Sample Output 3:</td>
    </tr>
    <tr>
      <td align="center">
      -> add(1, b=2)<br>
      <- 3<br>
      </td>
      <td align="center">
      -> add('a', b='b', c='c', d=3, e=True)<br>
      <- 'abcabcabcabc'<br>
      </td>
      <td align="center">
      -> fib(4)<br>
          -> fib(3)<br>
              -> fib(2)<br>
              <- 1<br>
              -> fib(1)<br>
              <- 1<br>
          <- 2<br>
          -> fib(2)<br>
          <- 1<br>
      <- 3<br>
      </td>
    </tr>
  </tbody>
</table>

## Примеры решений:
* Первый вариант решения
```python
def recviz(func): 
    import inspect
    def wrapper(*args,**kwargs):
        c = len(inspect.getouterframes(inspect.currentframe()))//2-1
        args_repr = [repr(a) for a in args]                      
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]  
        signature = ", ".join(args_repr + kwargs_repr)
        print(f'{"    "*c}-> {func.__name__}({signature})')
        value = func(*args,**kwargs)
        print(f'{"    "*c}<- {value!r}')    
        return value
    return wrapper
```
* Второй вариант решения
```python
import functools


def recviz(func):
    level = -1

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        nonlocal level
        level += 1

        pos_args = list(map(repr, args))
        keyword_args = [f'{k}={v!r}' for k, v in kwargs.items()]

        print('    ' * level + '->', f'{func.__name__}({", ".join(pos_args + keyword_args)})')
        value = func(*args, **kwargs)
        print('    ' * level + '<-', repr(value))

        level -= 1
        return value

    return wrapper
```


