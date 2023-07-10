<h2 style="text-align:center">Класс Strip</h2>


### Реализуйте класс Strip, экземпляры которого позволяют удалять из начала и конца строки определенные символы. При создании экземпляра класс должен принимать один аргумент:
* chars — строка, в которой перечислены удаляемые символы
#### Экземпляр класса Strip должен являться вызываемым объектом и принимать один аргумент:
* string — строка
#### Экземпляр класса Strip должен удалять из начала и конца строки string все символы, перечисленные в chars, и возвращать полученный результат.

##### Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.
##### Примечание 2. Никаких ограничений касательно реализации класса Strip нет, она может быть произвольной.

<table align="center">
  <tbody>
    <tr>
      <th>Sample Input 1: </th>
      <th>Sample Input 2: </th>
    </tr>
    <tr>
      <td align="center">strip = Strip('!? ')<br>
                        print(strip('     ?beegeek!'))<br>
                        print(strip('!bee?geek!'))<br></td>
      <td align="center">strip = Strip('.,+-')<br>
                          print(strip('     --++beegeek++--'))<br>
                          print(strip('-bee...geek-'))<br>
                          print(strip('-+,.b-e-e-g-e-e-k-+,.'))<br></td>
    </tr>
    <tr>
      <td>Sample Output 1:</td>
      <td>Sample Output 2:</td>
      </tr>
    <tr>
      <td align="center">
                        beegeek<br>
                        bee?geek<br>
      </td>
      <td align="center">
                             --++beegeek<br>
                          bee...geek<br>
                          b-e-e-g-e-e-k<br>
      </td>
    </tr>
  </tbody>
</table>



## Примеры решений:
* Первый вариант решения
```python
class Strip:
    def __init__(self, chars):
        self.chars = chars

    def __call__(self, string):
        return string.strip(self.chars)
```
* Второй вариант решения

```python
# import re

# class Strip:
#     def __init__(self, chars):
#         self.chars = re.escape(chars)
#     def __call__(self, string):
#         return re.sub(f"^[{self.chars}]*|[{self.chars}]*$", '', string)
```


