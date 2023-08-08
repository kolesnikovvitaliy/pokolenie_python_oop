<h2 style="text-align:center">Контекстный менеджер reversed_print</h2>

### Реализуйте контекстный менеджер reversed_print с помощью декоратора @contextmanager, который не принимает никаких аргументов.

#### Контекстный менеджер reversed_print должен позволять выполнять все операции записи в стандартный поток вывода sys.stdout внутри блока with в обратном порядке.

##### Примечание 1. Наглядные примеры использования класса reversed_print продемонстрированы в тестовых данных.
##### Примечание 2. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный контекстный менеджер используется только с корректными данными.

<table align="center">
  <tbody>
    <tr>
      <th>Sample Input 1: </th>
      <th>Sample Input 2: </th>
      <th>Sample Input 3: </th>
    </tr>
    <tr>
      <td align="center">print('Вывод вне блока with')<br>
                          with reversed_print():<br>
                              print('Вывод внутри блока with')<br>
                          print('Вывод вне блока with')<br></td>
      <td align="center">with reversed_print():<br>
                              print('python')<br>
                              print('beegeek')<br>
                          print('Вывод вне блока with')<br></td>
      <td align="center">print('Если жизнь одаривает вас лимонами — не делайте лимонад')<br>
                          print('Заставьте жизнь забрать их обратно!')<br>
                          with reversed_print():<br>
                              print('Мне не нужны твои проклятые лимоны!')<br>
                              print('Что мне с ними делать?')<br>
                          print('Требуйте встречи с менеджером, отвечающим за жизнь!')<br></td>
    </tr>
    <tr>
      <td>Sample Output 1:</td>
      <td>Sample Output 2:</td>
      <td>Sample Output 3:</td>
      </tr>
    <tr>
      <td align="center">
                        Вывод вне блока with<br>
                        htiw аколб иртунв довыВ<br>
                        Вывод вне блока with<br>
      </td>
      <td align="center">
                        nohtyp<br>
                        keegeeb<br>
                        Вывод вне блока with<br>
      </td>
      <td align="center">
                        Если жизнь одаривает вас лимонами — не делайте лимонад<br>
                          Заставьте жизнь забрать их обратно!<br>
                          !ыномил еытялкорп иовт ынжун ен енМ<br>
                          ?ьталед имин с енм отЧ<br>
                          Требуйте встречи с менеджером, отвечающим за жизнь!<br>
      </td>
    </tr>
  </tbody>
</table>



## Примеры решений:
* Первый вариант решения
```python
from contextlib import contextmanager
import sys


@contextmanager
def reversed_print():
    func = sys.stdout.write
    sys.stdout.write = lambda x: func(''.join(reversed(x)))
    yield
    sys.stdout.write = func
```
* Второй вариант решения

```python
import sys
from contextlib import contextmanager


@contextmanager
def reversed_print():
    original_write = sys.stdout.write

    def reverse_write(text):
        original_write(text[::-1])

    sys.stdout.write = reverse_write
    yield
    sys.stdout.write = original_write
```


