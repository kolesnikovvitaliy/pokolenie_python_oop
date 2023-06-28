<h2 style="text-align:center">Класс StrExtension</h2>

### Реализуйте класс StrExtension, описывающий набор функций для работы со строками. При создании экземпляра класс не должен принимать никаких аргументов.

#### Класс StrExtension должен иметь три статических метода:
* remove_vowels() — метод, который принимает в качестве аргумента строку, удаляет из нее все гласные латинские буквы без учета регистра и возвращает полученный результат
* leave_alpha() — метод, который принимает в качестве аргумента строку, удаляет из нее все символы, не являющиеся латинскими буквами, и возвращает полученный результат
* replace_all() — метод, который принимает три строковых аргумента string, chars и char, заменяет в строке string все символы из chars на char с учетом регистра и возвращает полученный результат.

##### Примечание 1. Гарантируется, что все буквенные символы относятся к латинскому алфавиту.
##### Примечание 2. Латинские гласные буквы: a, e, i, o, u, y.
##### Примечание 3. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.

<table align="center">
  <tbody>
    <tr>
      <th>Sample Input 1: </th>
      <th>Sample Input 2: </th>
      <th>Sample Input 3: </th>
    </tr>
    <tr>
      <td align="center">print(StrExtension.remove_vowels('Python'))<br>
                          print(StrExtension.remove_vowels('Stepik'))<br></td>
      <td align="center">print(StrExtension.leave_alpha('Python111'))<br>
                          print(StrExtension.leave_alpha('__Stepik__()'))<br></td>
      <td align="center">print(StrExtension.replace_all('Python', 'Ptn', '-'))<br>
                          print(StrExtension.replace_all('Stepik', 'stk', '#'))<br></td>
    </tr>
    <tr>
      <td>Sample Output 1:</td>
      <td>Sample Output 2:</td>
      <td>Sample Output 3:</td>
      </tr>
    <tr>
      <td align="center">
                        Pthn<br>
                        Stpk<br>
      </td>
      <td align="center">
                        Python<br>
                        Stepik<br>
      </td>
      <td align="center">
                        -y-ho-<br>
                        S#epi#<br>
      </td>
    </tr>
  </tbody>
</table>



## Примеры решений:
* Первый вариант решения
```python
import re


class StrExtension:
    
    @staticmethod
    def  remove_vowels(text):
        return ''.join(map(lambda x: x if not re.findall(r'[aeiouy]', x, re.IGNORECASE) else '', text))

    @staticmethod
    def leave_alpha(text):
        return ''.join(map(lambda x: x if re.findall(r'[a-z]', x, re.IGNORECASE) else '', text))
    
    @staticmethod  
    def replace_all(string, chars, char):
        return ''.join(map(lambda x: x if not re.findall(f'[{chars}]', x) else char, string))
```
* Второй вариант решения

```python
import re
class StrExtension:
    @staticmethod
    def remove_vowels(string):
        return re.sub(r'[aeiouy]', '', string, flags=re.I)
    
    @staticmethod
    def leave_alpha(string):
        return re.sub(r'[^A-Za-z]', '', string)
    
    @staticmethod
    def replace_all(string, chars, char):
        return re.sub(fr'[{chars}]', char, string)
```


