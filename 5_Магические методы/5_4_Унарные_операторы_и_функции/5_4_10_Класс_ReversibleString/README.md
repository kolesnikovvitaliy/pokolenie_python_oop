<h2 style="text-align:center">Класс ReversibleString</h2>



### Реализуйте класс ReversibleString, описывающий строку. При создании экземпляра класс должен принимать один аргумент:
* string — значение строки
#### Экземпляр класса ReversibleString должен иметь следующее неформальное строковое представление:
> <значение строки>
##### Также экземпляр класса ReversibleString должен поддерживать унарный оператор -, результатом которого должен являться новый экземпляр класса ReversibleString со значением строки в обратном порядке.

##### Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.
##### Примечание 2. Никаких ограничений касательно реализации класса ReversibleString нет, она может быть произвольной.

<table align="center">
  <tbody>
    <tr>
      <th>Sample Input 1: </th>
    </tr>
    <tr>
      <td align="center">string = ReversibleString('python')<br>
                          print(string)<br>
                          print(-string)<br>
<br></td>
    </tr>
    <tr>
      <td>Sample Output 1:</td>
      </tr>
    <tr>
      <td align="center">
                        python<br>
                        nohtyp<br>
      </td>
    </tr>
  </tbody>
</table>



## Примеры решений:
* Первый вариант решения
```python
class ReversibleString:
    def __init__(self, string: str) -> str:
        self.string = string

    def __str__(self) -> str:
        return f"{self.string}"

    def __neg__(self):
        return ReversibleString(''.join(reversed(self.string)))
```
* Второй вариант решения

```python
class ReversibleString:
    def __init__(self, string):
        self.string = string

    def __str__(self):
        return self.string

    def __neg__(self):
        return ReversibleString(self.string[::-1])
```


