<h2 style="text-align:center">Функция non_closed_files()</h2>

### Реализуйте функцию non_closed_files(), которая принимает один аргумент:
* files — список файловых объектов
#### Функция должна возвращать список, элементами которого являются открытые файловые объекты из списка files.

##### Примечание 1. Файловые объекты в возвращаемом функцией списке должны располагаться в своем исходном порядке.
##### Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимую функцию non_closed_files(), но не код, вызывающий ее.

<table align="center">
  <tbody>
    <tr>
      <th>Sample Input 1: </th>
    </tr>
    <tr>
      <td align="center">with (<br>
                              open('file1.txt', 'w', encoding='utf-8') as file1,<br>
                              open('file2.txt', 'w', encoding='utf-8') as file2,<br>
                              open('file3.txt', 'w', encoding='utf-8') as file3<br>
                          ):<br>
                              file1.write('i am the first file')<br>
                              file2.write('i am the second file')<br>
                              file3.write('i am the third file')<br>
                          file1 = open('file1.txt', encoding='utf-8')<br>
                          file3 = open('file3.txt', encoding='utf-8')<br>
                          for file in non_closed_files([file1, file2, file3]):<br>
                              print(file.read())<br>
<br></td>
    </tr>
    <tr>
      <td>Sample Output 1:</td>
      </tr>
    <tr>
      <td align="center">
                        i am the first file<br>
                        i am the third file<br>
      </td>
    </tr>
  </tbody>
</table>



## Примеры решений:
* Первый вариант решения
```python
def non_closed_files(files):
    for i in files:
        if i.closed:
            continue
        yield i
```
* Второй вариант решения

```python
def non_closed_files(files):
    return [file for file in files if not file.closed]
```


