<h2 style="text-align:center">Класс TitledText</h2>


### Реализуйте класс TitledText, наследника класса str, который описывает текст, имеющий заголовок. При создании экземпляра класс должен принимать два аргумента в следующем порядке:
* content — текст
* text_title — заголовок текста
#### Класс TitleText должен иметь один метод экземпляра:
* title() — метод, возвращающий заголовок текста


##### Примечание 1. Значением экземпляра класса TitledText должен быть именно текст, а не заголовок текста или текст вместе с заголовком.
##### Примечание 2. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.
##### Примечание 3. Никаких ограничений касательно реализации класса TitledText нет, она может быть произвольной.

<table align="center">
  <tbody>
    <tr>
      <th>Sample Input 1: </th>
      <th>Sample Input 2: </th>
    </tr>
    <tr>
      <td align="center">titled = TitledText('Сreate a class Soda', 'Homework')<br>
                          print(titled)<br>
                          print(titled.title())<br>
                          print(issubclass(TitledText, str))<br></td>
      <td align="center">titled1 = TitledText('Сreate a class Soda', 'Homework')<br>
                          titled2 = TitledText('Сreate a class Soda', 'Exam')<br>
                          print(titled1 == titled2)<br></td>
    </tr>
    <tr>
      <td>Sample Output 1:</td>
      <td>Sample Output 2:</td>
      </tr>
    <tr>
      <td align="center">
                        Сreate a class Soda<br>
                          Homework<br>
                          True<br>
      </td>
      <td align="center">
                        True<br>
      </td>
    </tr>
  </tbody>
</table>



## Примеры решений:
* Первый вариант решения
```python
class TitledText(str):
    def __new__(cls, content, text_title):
        obj = super().__new__(cls, content)
        obj.text_title = text_title
        return obj

    def title(self):
        return self.text_title
```
* Второй вариант решения

```python
class TitledText(str):
    def __new__(cls, value, title):
        instance = super().__new__(cls, value)
        instance.title = lambda: title
        return instance
```


