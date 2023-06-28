<h2 style="text-align:center">Класс CaseHelper</h2>

### Snake Case — стиль написания составных слов, при котором несколько слов разделяются символом нижнего подчеркивания (_) и не имеют пробелов в записи, причём каждое слово пишется с маленькой буквы. Например, bee_geek и hello_world.
### Upper Camel Case — стиль написания составных слов, при котором несколько слов пишутся слитно без пробелов, при этом каждое слово пишется с заглавной буквы. Например, BeeGeek и HelloWorld.
### Реализуйте класс CaseHelper, описывающий набор функций для работы со строками в стилях Snake Case и Upper Camel Case. При создании экземпляра класс не должен принимать никаких аргументов.
#### Класс CaseHelper должен иметь четыре статических метода:
* is_snake() — метод, принимающий в качестве аргумента строку и возвращающий True, если переданная строка записана в стиле Snake Case, или False в противном случае
* is_upper_camel() — метод, принимающий в качестве аргумента строку и возвращающий True, если переданная строка записана в стиле Upper Camel Case, или False в противном случае
* to_snake() — метод, который принимает в качестве аргумента строку в стиле Upper Camel Case, записывает ее в стиле Snake Case и возвращает полученный результат
* to_upper_camel() — метод, который принимает в качестве аргумента строку в стиле Snake Case, записывает ее в стиле Upper Camel Case и возвращает полученный результат

##### Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.

<table align="center">
  <tbody>
    <tr>
      <th>Sample Input 1: </th>
      <th>Sample Input 2: </th>
      <th>Sample Input 3: </th>
      <th>Sample Input 4: </th>
    </tr>
    <tr>
      <td align="center">print(CaseHelper.is_snake('beegeek'))<br>
                          print(CaseHelper.is_snake('bee_geek'))<br>
                          print(CaseHelper.is_snake('Beegeek'))<br>
                          print(CaseHelper.is_snake('BeeGeek'))<br></td>
      <td align="center">print(CaseHelper.is_upper_camel('beegeek'))<br>
                        print(CaseHelper.is_upper_camel('bee_geek'))<br>
                        print(CaseHelper.is_upper_camel('Beegeek'))<br>
                        print(CaseHelper.is_upper_camel('BeeGeek'))<br></td>
      <td align="center">print(CaseHelper.to_snake('Beegeek'))<br>
                          print(CaseHelper.to_snake('BeeGeek'))<br></td>
      <td align="center">print(CaseHelper.to_upper_camel('beegeek'))<br>
                          print(CaseHelper.to_upper_camel('bee_geek'))<br></td>
    </tr>
    <tr>
      <td>Sample Output 1:</td>
      <td>Sample Output 2:</td>
      <td>Sample Output 3:</td>
      <td>Sample Output 4:</td>
      </tr>
    <tr>
      <td align="center">
                        True<br>
                        True<br>
                        False<br>
                        False<br>
      </td>
      <td align="center">
                        False<br>
                        False<br>
                        True<br>
                        True<br>
      </td>
      <td align="center">
                        beegeek<br>
                        bee_geek<br>
      </td>
      <td align="center">
                        Beegeek<br>
                        BeeGeek<br>
      </td>
    </tr>
  </tbody>
</table>



## Примеры решений:
* Первый вариант решения
```python
import re


class CaseHelper:
    
    @staticmethod
    def is_snake(string):
        return False if (re.findall(r'[A-Z]', string) and not re.findall(r'_', string) or re.findall(r'__', string))  else True

    @staticmethod
    def is_upper_camel(string):
        return True if (re.findall(r'[A-Z]', string) and not re.findall(r'_', string) and re.findall(r'^[A-Z]', string)) else False

    @staticmethod
    def to_snake(string):
        return re.sub(r'(?<=\w)(?=[A-Z])', '_', string).lower()       

    @staticmethod
    def to_upper_camel(string):
        return ''.join(map(lambda x: x.title(), string.split('_')))
```
* Второй вариант решения

```python
import re

class CaseHelper:
    @staticmethod
    def is_snake(string):
        return re.match(r'^[a-z]+(_[a-z]+)*$', string) is not None

    @staticmethod
    def is_upper_camel(string):
        return re.match(r'^([A-Z][a-z]+)+$', string) is not None

    @staticmethod
    def to_snake(string):
        return re.sub(r'(?<!^)(?=[A-Z])', '_', string).lower()

    @staticmethod
    def to_upper_camel(string):
        return ''.join(map(str.capitalize, string.split('_')))
```


