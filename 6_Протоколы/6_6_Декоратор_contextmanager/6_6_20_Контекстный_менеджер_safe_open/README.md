<h2 style="text-align:center">Контекстный менеджер safe_open</h2>


### Реализуйте контекстный менеджер safe_open с помощью декоратора @contextmanager, который принимает два аргумента в следующем порядке:
* filename — имя файла
* mode — режим открытия файла (r, w, a и так далее), по умолчанию имеет значение r
#### Контекстный менеджер должен открывать файл с именем filename в режиме mode и позволять выполнять с ним соответствующие операции. Причем если открытие файла было выполнено без исключений, в качестве значения, используемого в блоке with, контекстный менеджер должен вернуть кортеж из двух элементов, первым из которых является необходимый файловый объект, вторым — значение None. Однако если при открытии файла было возбуждено исключение, то в качестве значения, используемого в блоке with, контекстный менеджер должен вернуть кортеж из двух элементов, первым из которых является значение None, вторым — возбужденное при открытии исключение. Также контекстный менеджер должен закрывать открытый им файл после выполнения кода внутри блока with.

##### Примечание 1. Наглядные примеры использования контекстного менеджера safe_open продемонстрированы в тестовых данных.
##### Примечание 2. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный контекстный менеджер используется только с корректными данными.

<table align="center">
  <tbody>
    <tr>
      <th>Sample Input 1: </th>
      <th>Sample Input 2: </th>
    </tr>
    <tr>
      <td align="center">with open('Ellies_jokes.txt', 'w') as file:<br>
                              file.write('Знаешь, кто не прав? Лев\n')<br>
                              file.write('Что треугольник сказал кругу? Катись отсюда')<br>
                          with safe_open('Ellies_jokes.txt') as file:<br>
                              file, error = file<br>
                              print(error)<br>
                              print(file.read())<br></td>
      <td align="center">with safe_open('Ellies_jokes_2.txt') as file:<br>
                                file, error = file<br>
                                print(file)<br>
                                print(error)<br></td>
    </tr>
    <tr>
      <td>Sample Output 1:</td>
      <td>Sample Output 2:</td>
      </tr>
    <tr>
      <td align="center">
                        None<br>
                        Знаешь, кто не прав? Лев<br>
                        Что треугольник сказал кругу? Катись отсюда<br>
      </td>
      <td align="center">
                        None<br>
                        [Errno 2] No such file or directory: 'Ellies_jokes_2.txt'<br>
      </td>
    </tr>
  </tbody>
</table>



## Примеры решений:
* Первый вариант решения
```python
from contextlib import contextmanager


@contextmanager
def safe_open(filename, mode='r'):
    try:
        file_ = open(filename, mode)
        result = (file_, None)
        yield result
        file_.close()
    except Exception as error:
        result = (None, error)
        yield result
```
* Второй вариант решения

```python
from contextlib import contextmanager

@contextmanager
def safe_open(filename, mode='r', file=None):
    try:
        file = open(filename, mode)
        yield file, None
    except Exception as e:
        yield None, e
    finally:
        if file:
            file.close()
```


