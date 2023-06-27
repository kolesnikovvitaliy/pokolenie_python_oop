<h2 style="text-align:center">Класс Account</h2>

### В целях безопасности в базах данных пароли от аккаунтов пользователей хранятся не в явном виде, а в виде хеш-значений — чисел, вычисленных по специальному алгоритму на основе паролей.
#### Вам доступна функция hash_function(), которая принимает в качестве аргумента пароль и возвращает его хеш-значение.
```python
def hash_function(password):
    hash_value = 0
    for char, index in zip(password, range(len(password))):
         hash_value += ord(char) * index
    return hash_value % 10**9
```
### Реализуйте класс Account, описывающий аккаунт интернет-пользователя на некотором сервисе. При создании экземпляра класс должен принимать два аргумента в следующем порядке:
* login — логин пользователя
* password — пароль пользователя

#### Класс Account должен иметь два свойства:
* login — свойство, доступное только для чтения, возвращающее логин пользователя. При попытке изменения свойство должно быть возбуждено исключение AttributeError с текстом:
>  Изменение логина невозможно
* password — свойство, доступное для чтения и записи, возвращающее хеш-значение пароля от аккаунта пользователя. При изменении свойство должно вычислять хеш-значение нового пароля и сохранять его, а не сам пароль

##### Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.
##### Примечание 2. Никаких ограничений касательно реализации класса Account нет, она может быть произвольной.

<table align="center">
  <tbody>
    <tr>
      <th>Sample Input 1: </th>
      <th>Sample Input 2: </th>
      <th>Sample Input 3: </th>
    </tr>
    <tr>
      <td align="center">account = Account('hannymad', 'cakeisalie')<br>
                        print(account.login)<br>
                        print(account.password)<br></td>
      <td align="center">account = Account('timyr-guev', 'lovebeegeek')<br>
                        print(account.password)<br>
                        account.password = 'verylovebeegeek'<br>
                        print(account.password)<br></td>
      <td align="center">account = Account('timyr-guev', 'lovebeegeek')<br>
                        try:<br>
                            account.login = 'timyrik30'<br>
                        except AttributeError as e:<br>
                            print(e)<br></td>
    </tr>
    <tr>
      <td>Sample Output 1:</td>
      <td>Sample Output 2:</td>
      <td>Sample Output 3:</td>
      </tr>
    <tr>
      <td align="center">
                        hannymad<br>
                        4696<br>
      </td>
      <td align="center">
                        5661<br>
                        10953<br>
      </td>
      <td align="center">
                        Изменение логина невозможно<br>
      </td>
    </tr>
  </tbody>
</table>



## Примеры решений:
* Первый вариант решения
```python
class Account:
    def __init__(self, login, password):
        self._login = login
        self.password = password

    @property
    def login(self):
        return self._login
    
    @login.setter
    def login(self, login):
        raise AttributeError('Изменение логина невозможно')
    
    @property
    def password(self):
        hash_value = 0
        for char, index in zip(self._password, range(len(self._password))):
            hash_value += ord(char) * index
        return hash_value % 10**9
    
    @password.setter
    def password(self, password):
        self._password = password
```
* Второй вариант решения

```python
def hash_function(password):
    hash_value = 0
    for char, index in zip(password, range(len(password))):
        hash_value += ord(char) * index
    return hash_value % 10 ** 9


class Account:
    def __init__(self, login, password):
        self._login = login
        self.password = password

    @property
    def login(self):
        return self._login

    @login.setter
    def login(self, login):
        raise AttributeError('Изменение логина невозможно')
            
    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        self._password = hash_function(password)
```


