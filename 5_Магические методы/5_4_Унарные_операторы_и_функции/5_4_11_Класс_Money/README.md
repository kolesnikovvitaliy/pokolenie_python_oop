<h2 style="text-align:center">Класс Money</h2>

### Реализуйте класс Money, описывающий денежную сумму в рублях. При создании экземпляра класс должен принимать один аргумент:
* amount — количество денег
#### Экземпляр класса Money должен иметь следующее неформальное строковое представление:
> <количество денег> руб.
#### Также экземпляр класса Money должен поддерживать унарные операторы + и -:
* результатом унарного + должен являться новый экземпляр класса Money с неотрицательным количеством денег
* результатом унарного - должен являться новый экземпляр класса Money с отрицательным количеством денег
##### Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.
##### Примечание 2. Никаких ограничений касательно реализации класса Money нет, она может быть произвольной.

<table align="center">
  <tbody>
    <tr>
      <th>Sample Input 1: </th>
      <th>Sample Input 2: </th>
    </tr>
    <tr>
      <td align="center">money = Money(100)<br>
                          print(money)<br>
                          print(+money)<br>
                          print(-money)<br></td>
      <td align="center">money = Money(-100)<br>
                          print(money)<br>
                          print(+money)<br>
                          print(-money)<br></td>
    </tr>
    <tr>
      <td>Sample Output 1:</td>
      <td>Sample Output 2:</td>
      </tr>
    <tr>
      <td align="center">
                        100 руб.<br>
                        100 руб.<br>
                        -100 руб.
                        <br>
      </td>
      <td align="center">
                        -100 руб.<br>
                          100 руб.<br>
                          -100 руб.
                          <br>
      </td>
    </tr>
  </tbody>
</table>



## Примеры решений:
* Первый вариант решения
```python
class Money:
    def __init__(self, amount: int) -> str:
        self.amount = amount

    def __str__(self) -> str:
        return f"{self.amount} руб."
    
    def __pos__(self) -> int:
        if self.amount >= 0:
            return __class__(self.amount)
        return __class__(~self.amount+1)
    
    def __neg__(self) -> int:
        if self.amount >= 0:
            return __class__(-self.amount)
        return __class__(self.amount)
```
* Второй вариант решения

```python
class Money:
    def __init__(self, amount):
        self.amount = amount

    def __str__(self):
        return f'{self.amount} руб.'

    def __pos__(self):
        return Money(abs(self.amount))

    def __neg__(self):
        return Money(-abs(self.amount))
```


