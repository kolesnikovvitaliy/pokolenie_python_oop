<h2 style="text-align:center">Функция print_file_content()</h2>

### Реализуйте функцию print_file_content(), которая принимает один аргумент:
* filename — имя текстового файла
#### Функция должна выводить содержимое файла с именем filename. Если файла с данным именем нет в папке с программой, функция должна вывести текст:
> Файл не найден

##### Примечание 1. Имя файла, передаваемого в функцию, уже содержит расширение.
##### Примечание 2. При открытии файла используйте явное указание кодировки UTF-8
##### Примечание 3. В тестирующую систему сдайте программу, содержащую только необходимую функцию print_file_content(), но не код, вызывающий ее.

<table align="center">
  <tbody>
    <tr>
      <th>Sample Input 1: </th>
      <th>Sample Input 2: </th>
    </tr>
    <tr>
      <td align="center">with open('Precepts_of_Zote.txt', 'w', encoding='utf-8') as file:<br>
                            file.write('Сражения и путешествия берут своё')<br>
                        print_file_content('Precepts_of_Zote.txt')<br></td>
      <td align="center">print_file_content('Precepts_of_Zote2.txt')<br></td>
    </tr>
    <tr>
      <td>Sample Output 1:</td>
      <td>Sample Output 2:</td>
      </tr>
    <tr>
      <td align="center">
                        Сражения и путешествия берут своё<br>
      </td>
      <td align="center">
                        Файл не найден<br>
      </td>
    </tr>
  </tbody>
</table>



## Примеры решений:
* Первый вариант решения
```python
def print_file_content(filename):
    try:
        with open(filename, mode='r', encoding='utf-8') as file:
            print(file.read())
    except:
        print('Файл не найден')
```
* Второй вариант решения

```python
class HandlerFileNotFoundError:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        try:
            return self.func(*args, **kwargs)
        except:
            print("Файл не найден")


@HandlerFileNotFoundError
def print_file_content(filename):
    with open(filename, encoding="utf-8") as f1:
        print(f1.read())

```


