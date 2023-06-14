<h2 style="text-align:center">Декоратор @jsonify</h2>


### Реализуйте декоратор @jsonify, преобразующий возвращаемое значение декорируемой функции в строку формата JSON.


#### Также декоратор должен сохранять имя и строку документации декорируемой функции.
##### Примечание 1. Гарантируется, что возвращаемое значение функции принадлежит типу, который поддерживается форматом JSON.
#####  Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимый декоратор @jsonify, но не код, вызывающий его.




<table align="center">
  <tbody>
    <tr>
      <th>Sample Input 1: </th>
      <th>Sample Input 2: </th>
      <th>Sample Input 3:</th>
    </tr>
    <tr>
      <td align="center"><pre class="step-text__limit-value">@jsonify
def make_user(id, live, options):
    return {'id': id, 'live': live, 'options': options}

print(make_user(4, False, None))</pre></td>
     <td align="center"><pre class="step-text__limit-value">@jsonify
def make_list(n):
    return list(range(1, n + 1))
    
print(make_list(10))</pre></td>
      <td align="center"><pre class="step-text__limit-value">@jsonify
def make_str(s1, s2):
    return (s1 + s2) * 5
    
print(make_str('bee', 'geek'))</pre>
            </td>
    </tr>
    <tr>
      <td>Sample Output 1:</td>
      <td>Sample Output 2:</td>
      <td>Sample Output 3:</td>
    </tr>
    <tr>
      <td align="center">
      {"id": 4, "live": false, "options": null}<br>
      </td>
      <td align="center">
      [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]<br>
      </td>
      <td align="center">
      "beegeekbeegeekbeegeekbeegeekbeegeek"<br>
      </td>
    </tr>
  </tbody>
</table>

## Примеры решений:
* Первый вариант решения
```python
def jsonify(func):
    import functools, json    
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return json.dumps(func(*args, **kwargs))
    return wrapper
```
* Второй вариант решения
```python
import json

def jsonify(func):
    def wrapper(*args):
        wrapper.__name__ = func.__name__
        wrapper.__doc__ = func.__doc__
        return json.dumps(func(*args))
    return wrapper
```
