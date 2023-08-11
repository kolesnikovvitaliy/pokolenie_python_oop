<h2 style="text-align:center">Класс UpperPrintString</h2>

### Реализуйте класс UpperPrintString, наследника класса str, описывающий строку. Процесс создания экземпляра класса UpperPrintString должен совпадать с процессом создания экземпляра класса str.

#### Экземпляр класса UpperPrintString должен иметь следующее неформальное строковое представление:
> <значение строки в верхнем регистре>

##### Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.
##### Примечание 2. Никаких ограничений касательно реализации класса UpperPrintString нет, она может быть произвольной.

<table align="center">
  <tbody>
    <tr>
      <th>Sample Input 1: </th>
      <th>Sample Input 2: </th>
    </tr>
    <tr>
      <td align="center">s1 = UpperPrintString('beegeek')<br>
                        s2 = UpperPrintString('BeeGeek')<br>
                        print(s1)<br>
                        print(s2)<br></td>
      <td align="center">s = UpperPrintString('beegeek')<br>
                          print(list(s))<br></td>
    </tr>
    <tr>
      <td>Sample Output 1:</td>
      <td>Sample Output 2:</td>
      </tr>
    <tr>
      <td align="center">
                        BEEGEEK<br>
                        BEEGEEK<br>
      </td>
      <td align="center">
                        ['b', 'e', 'e', 'g', 'e', 'e', 'k']<br>
      </td>
    </tr>
  </tbody>
</table>



## Примеры решений:
* Первый вариант решения
```python
class UpperPrintString(str):
    def __str__(self):
        return f'{super().__str__().upper()}'
```
* Второй вариант решения

```python
class UpperPrintString(str):
    def __str__(self):
        return self.upper()
```


