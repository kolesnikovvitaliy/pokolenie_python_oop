<h2 style="text-align:center">Контекстный менеджер make_tag</h2>



### Реализуйте контекстный менеджер make_tag с помощью декоратора @contextmanager, который принимает один аргумент:
* tag — произвольная строка
#### Контекстный менеджер должен выводить строку tag при входе в блок with и после выхода из блока with.


##### Примечание 1. Наглядные примеры использования контекстного менеджера make_tag продемонстрированы в тестовых данных.
##### Примечание 2. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный контекстный менеджер используется только с корректными данными.

<table align="center">
  <tbody>
    <tr>
      <th>Sample Input 1: </th>
    </tr>
    <tr>
      <td align="center">with make_tag('---'):<br>
                            print('Поколение Python')<br></td>
    </tr>
    <tr>
      <td>Sample Output 1:</td>
      </tr>
    <tr>
      <td align="center">
                        ---<br>
                        Поколение Python<br>
                        ---<br>
      </td>
    </tr>
  </tbody>
</table>



## Примеры решений:
* Первый вариант решения
```python
from contextlib import contextmanager


@contextmanager
def make_tag(tag):
    print(f'{tag}')
    yield
    print(f'{tag}')
```
* Второй вариант решения

```python
from contextlib import contextmanager


@contextmanager
def make_tag(tag):
    print(tag)
    yield
    print(tag)
```


