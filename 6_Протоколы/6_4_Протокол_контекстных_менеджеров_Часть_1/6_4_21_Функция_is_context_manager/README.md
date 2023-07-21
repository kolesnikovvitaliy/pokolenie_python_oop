<h2 style="text-align:center">Функция is_context_manager()</h2>

### Реализуйте функцию is_context_manager(), которая принимает один аргумент:
* obj — произвольный объект
#### Функция должна возвращать True, если объект obj является контекстным менеджером, или False в противном случае. 
##### Примечание 1. В тестирующую систему сдайте программу, содержащую только необходимую функцию is_context_manager(), но не код, вызывающий ее.

<table align="center">
  <tbody>
    <tr>
      <th>Sample Input 1: </th>
    </tr>
    <tr>
      <td align="center">print(is_context_manager(open('output.txt', mode='w')))<br></td>
    </tr>
    <tr>
      <td>Sample Output 1:</td>
      </tr>
    <tr>
      <td align="center">
                        True<br>
      </td>
    </tr>
  </tbody>
</table>



## Примеры решений:
* Первый вариант решения
```python
def is_context_manager(obj):
    try:
        if obj.__enter__ and obj.__exit__:
            return True
    except:
        return False
```
* Второй вариант решения

```python
def is_context_manager(obj):
    return hasattr(obj, '__enter__') and hasattr(obj, '__exit__')
```


