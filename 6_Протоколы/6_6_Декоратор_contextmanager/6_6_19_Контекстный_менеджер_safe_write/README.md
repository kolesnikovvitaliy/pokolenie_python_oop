<h2 style="text-align:center">Контекстный менеджер safe_write</h2>


### Реализуйте контекстный менеджер safe_write с помощью декоратора @contextmanager, который принимает один аргумент:
* filename — имя файла
#### Контекстный менеджер должен открывать файл с именем filename в режиме w и позволять выполнять с ним соответствующие операции. Причем если во время записи в файл было возбуждено какое-либо исключение, контекстный менеджер должен поглотить его, отменить все выполненные ранее записи в файл, если они были, вернуть файл в исходное состояние и проинформировать о возбужденном исключении выводом следующего текста:
> Во время записи в файл было возбуждено исключение <тип исключения>

##### Примечание 1. Наглядные примеры использования контекстного менеджера safe_write продемонстрированы в тестовых данных.
##### Примечание 2. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный контекстный менеджер используется только с корректными данными.

<table align="center">
  <tbody>
    <tr>
      <th>Sample Input 1: </th>
      <th>Sample Input 2: </th>
    </tr>
    <tr>
      <td align="center">with safe_write('undertale.txt') as file:
                              file.write('Тень от руин нависает над вами, наполняя вас решительностью')
                          with open('undertale.txt') as file:
                              print(file.read())<br></td>
      <td align="center">with safe_write('undertale.txt') as file:
                              file.write('Тень от руин нависает над вами, наполняя вас решительностью\n')
                          with safe_write('undertale.txt') as file:
                              print('Под весёлый шорох листвы вы наполняетесь решительностью', file=file)
                              raise ValueError
                          with open('undertale.txt') as file:
                              print(file.read())<br></td>
    </tr>
    <tr>
      <td>Sample Output 1:</td>
      <td>Sample Output 2:</td>
      </tr>
    <tr>
      <td align="center">
                        Тень от руин нависает над вами, наполняя вас решительностью<br>
      </td>
      <td align="center">
                        Во время записи в файл было возбуждено исключение ValueError
                        Тень от руин нависает над вами, наполняя вас решительностью<br>
      </td>
    </tr>
  </tbody>
</table>



## Примеры решений:
* Первый вариант решения
```python
from contextlib import contextmanager


@contextmanager
def safe_write(filename):
    copy_file = f'copy_{filename}'
    try:
        tmp = open(copy_file, 'w')
        yield tmp
        tmp.close()
        tmp = open(copy_file, 'r')
        file = open(filename, 'w')
        file.write(tmp.read())
        tmp.close()
        file.close()
    except Exception as error:
        print(f"Во время записи в файл было возбуждено исключение {type(error).__name__}")
        file = open(filename, 'r')
        tmp = open(copy_file, 'w')
        tmp.write(file.read())
        file.close()
    finally:
        tmp.close()
```
* Второй вариант решения

```python
from contextlib import contextmanager

@contextmanager
def safe_write(filename):
    try:
        with open(filename + '_', 'w') as f_copy:
            yield f_copy
        with open(filename, 'w') as f_orig, open(filename + '_', 'r') as f_copy:
            f_orig.write(f_copy.read())
    except Exception as e:
        print(f"Во время записи в файл было возбуждено исключение {type(e).__name__}")
```


