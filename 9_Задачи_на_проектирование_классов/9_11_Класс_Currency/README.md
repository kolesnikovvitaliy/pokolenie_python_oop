<h2 style="text-align:center">Класс Currency</h2>

### Реализуйте класс Currency для работы со значениями в различных валютах. Экземпляр класса Currency должен создаваться на основе числового значения и валюты:
```python
money1 = Currency(10, 'EUR')
money2 = Currency(20, 'USD')
```
#### Поддерживаемые валюты: EUR (евро), USD (доллар) и RUB (рубль).

#### В качестве неформального строкового представления экземпляр класса Currency должен иметь собственное числовое значение и валюту:
```python
print(money1)                                      # 10 EUR
print(money2)                                      # 20 USD
```
#### Экземпляр класса Currency должен поддерживать операцию конвертации в другую валюту с помощью метода change_to():
```python
money1.change_to('RUB')
print(money1)                                      # 900 RUB
```
#### Экземпляры класса Currency должны поддерживать между собой операции сложения, вычитания, умножения и деления с помощью операторов +, -, * и / соответственно:
```python
print(Currency(5, 'EUR') + Currency(5, 'EUR'))     # 10 EUR
print(Currency(5, 'EUR') + Currency(11, 'USD'))    # 15.0 EUR
print(Currency(5, 'RUB') + Currency(11, 'USD'))    # 905.0 RUB
print(Currency(5, 'USD') * Currency(5, 'EUR'))     # 27.5 USD
```
#### Обратите внимание, результирующую валюту должен определять левый операнд. 

##### Примечание. Таблица курсов валют:

<div>
<img align="center" src="https://github.com/kolesnikovvitaliy/pokolenie_python_oop/blob/main/7_Наследование_и_полиморфизм/7_5_Абстрактные_классы_модуль_abc/7_5_25_Класс_DNA/img/task.png" title="Git" **alt="Git">
​</div>


<table align="center">
  <tbody>
    <tr>
      <th>Sample Input 1: </th>
      <th>Sample Input 2: </th>
    </tr>
    <tr>
      <td align="center">money1 = Currency(10, 'EUR')<br>
                          money2 = Currency(20, 'USD')<br>
                          print(money1)<br>
                          print(money2)<br></td>
      <td align="center">money = Currency(10, 'EUR')<br>
                          money.change_to('RUB')<br>
                          print(money)<br></td>
    </tr>
    <tr>
      <td>Sample Output 1:</td>
      <td>Sample Output 2:</td>
      </tr>
    <tr>
      <td align="center">
                        10 EUR<br>
                        20 USD<br>
      </td>
      <td align="center">
                        900 RUB<br>
      </td>
    </tr>
  </tbody>
</table>



## Примеры решений:
* Первый вариант решения
```python

```
* Второй вариант решения

```python

```


