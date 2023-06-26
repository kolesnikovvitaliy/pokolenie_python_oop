<h2 style="text-align:center">Класс BankAccount</h2>

### Реализуйте класс BankAccount, описывающий банковский счет. При создании экземпляра класс должен принимать один аргумент:
* balance — баланс счета, по умолчанию имеет значение 0
#### Экземпляр класса BankAccount должен иметь один атрибут:
* _balance — баланс счета
#### Класс BankAccount должен иметь четыре метода экземпляра:
* get_balance() — метод, возвращающий актуальный баланс счета
* deposit() — метод, принимающий в качестве аргумента число amount и увеличивающий баланс счета на amount
* withdraw() — метод, принимающий в качестве аргумента число amount и уменьшающий баланс счета на amount. Если  amount превышает количество средств на балансе счета, должно быть возбуждено исключение ValueError с сообщением:

> На счете недостаточно средств

* transfer() — метод, принимающий в качестве аргументов банковский счет account и число amount. Метод должен уменьшать баланс текущего счета на amount и увеличивать баланс счета account на amount. Если amount превышает количество средств на балансе текущего счета, должно быть возбуждено исключение ValueError с сообщением:
> На счете недостаточно средств


##### Примечание 1. Числами будем считать экземпляры классов int и float.
##### Примечание 2. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.

<table align="center">
  <tbody>
    <tr>
      <th>Sample Input 1: </th>
      <th>Sample Input 2: </th>
      <th>Sample Input 3: </th>
      <th>Sample Input 4: </th>
    </tr>
    <tr>
      <td align="center">account = BankAccount()<br>
                        print(account.get_balance())<br>
                        account.deposit(100)<br>
                        print(account.get_balance())<br>
                        account.withdraw(50)<br>
                        print(account.get_balance())<br></td>
      <td align="center">account = BankAccount(100)<br>
                          try:<br>
                              account.withdraw(150)<br>
                          except ValueError as e:<br>
                              print(e)<br></td>
      <td align="center">account1 = BankAccount(100)<br>
                        account2 = BankAccount(200)<br>
                        account1.transfer(account2, 50)<br>
                        print(account1.get_balance())<br>
                        print(account2.get_balance())<br></td>
      <td align="center">account1 = BankAccount(100)<br>
                        account2 = BankAccount(200)<br>
                        try:<br>
                            account1.transfer(account2, 150)<br>
                        except ValueError as e:<br>
                            print(e)<br></td>
    </tr>
    <tr>
      <td>Sample Output 1:</td>
      <td>Sample Output 2:</td>
      <td>Sample Output 3:</td>
      <td>Sample Output 4:</td>
      </tr>
    <tr>
      <td align="center">
                        0<br>
                        100<br>
                        50<br>
      </td>
      <td align="center">
                        На счете недостаточно средств<br>
      </td>
      <td align="center">
                        50<br>
                        250<br>
      </td>
      <td align="center">
                        На счете недостаточно средств<br>
      </td>
    </tr>
  </tbody>
</table>



## Примеры решений:
* Первый вариант решения
```python
class BankAccount:
    def __init__(self, balance=0):
        self._balance = balance
    
    def get_balance(self):
        return self._balance
    
    def deposit(self, amount):
            self._balance += amount
            return self._balance
    
    def withdraw(self, amount):
        if (self._balance - amount) >= 0:
            self._balance -= amount
            return self._balance
        raise ValueError('На счете недостаточно средств')
    
    def transfer(self, account, amount):
        self.withdraw(amount)
        account.deposit(amount) 
```
* Второй вариант решения

```python
class BankAccount:
    def __init__(self, balance=0):
        self._balance = balance
    
    def get_balance(self):
        return self._balance
    
    def deposit(self, amount):
        self._balance += amount
    
    def withdraw(self, amount):
        if self._balance < amount:
            raise ValueError('На счете недостаточно средств')
        self._balance -= amount

    def transfer(self, account, amount):
        self.withdraw(amount)
        account.deposit(amount)
```


