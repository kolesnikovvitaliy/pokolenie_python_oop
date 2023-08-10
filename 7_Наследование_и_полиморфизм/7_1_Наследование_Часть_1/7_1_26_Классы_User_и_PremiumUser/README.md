<h2 style="text-align:center">Классы User и PremiumUser</h2>

### Реализуйте класс User, описывающий пользователя некоторого интернет-ресурса. При создании экземпляра класс должен принимать один аргумент:
* name — имя пользователя
#### Класс User должен иметь один метод экземпляра:
* skip_ads() — метод, всегда возвращающий False

### Также реализуйте класс PremiumUser, наследника класса User, описывающий пользователя некоторого интернет-ресурса с премиум подпиской. Процесс создания экземпляра класса PremiumUser должен совпадать с процессом создания экземпляра класса User.
#### Класс PremiumUser должен иметь один метод экземпляра:
* skip_ads() — метод, всегда возвращающий True 

##### Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.
##### Примечание 2. Никаких ограничений касательно реализации классов нет, она может быть произвольной.

<table align="center">
  <tbody>
    <tr>
      <th>Sample Input 1: </th>
      <th>Sample Input 2: </th>
    </tr>
    <tr>
      <td align="center">print(issubclass(PremiumUser, User))<br></td>
      <td align="center">user = User('Arthur')<br>
                          premium_user = PremiumUser('Arthur')<br>
                          print(user.skip_ads())<br>
                          print(premium_user.skip_ads())<br></td>
    </tr>
    <tr>
      <td>Sample Output 1:</td>
      <td>Sample Output 2:</td>
      </tr>
    <tr>
      <td align="center">
                        True<br>
      </td>
      <td align="center">
                        False<br>
                        True<br>
      </td>
    </tr>
  </tbody>
</table>



## Примеры решений:
* Первый вариант решения
```python
class User:
    def __init__(self, name: str):
        self._name = name

    def skip_ads(self):
        return False


class PremiumUser(User):
    def skip_ads(self):
        return True
```
* Второй вариант решения

```python
class User:
    def __init__(self, name: str):
        self._name = name

    def skip_ads(self):
        return False


class PremiumUser(User):
    def __init__(self, name):
        super().__init__(name)

    def skip_ads(self):
        return True
```


