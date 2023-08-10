<h2 style="text-align:center">Классы BasicPlan и подклассы</h2>


### 1. Реализуйте класс BasicPlan, описывающий подписку базового уровня на некотором онлайн-сервисе. При создании экземпляра класс не должен принимать никаких аргументов.
#### Класс BasicPlan должен иметь семь атрибутов:
* can_stream —  атрибут, имеющий значение True
* can_download — атрибут, имеющий значение True
* has_SD — атрибут, имеющий значение True
* has_HD — атрибут, имеющий значение False
* has_UHD — атрибут, имеющий значение False
* num_of_devices — атрибут, имеющий значение 1
* price — атрибут, имеющий значение 8.99$
### 2. Также реализуйте класс SilverPlan, наследника класса BasicPlan, описывающий подписку среднего уровня на некотором онлайн-сервисе. Процесс создания экземпляра класса SilverPlan должен совпадать с процессом создания экземпляра класса BasicPlan.
#### Класс SilverPlan должен иметь семь атрибутов:
* can_stream —  атрибут, имеющий значение True
* can_download — атрибут, имеющий значение True
* has_SD — атрибут, имеющий значение True
* has_HD — атрибут, имеющий значение True
* has_UHD — атрибут, имеющий значение False
* num_of_devices — атрибут, имеющий значение 2
* price — атрибут, имеющий значение 12.99$
### 3. Наконец, реализуйте класс GoldPlan, наследника класса BasicPlan, описывающий подписку высокого уровня на некотором онлайн-сервисе. Процесс создания экземпляра класса GoldPlan должен совпадать с процессом создания экземпляра класса BasicPlan.
#### Класс GoldPlan должен иметь семь атрибутов:
* can_stream —  атрибут, имеющий значение True
* can_download — атрибут, имеющий значение True
* has_SD — атрибут, имеющий значение True
* has_HD — атрибут, имеющий значение True
* has_UHD — атрибут, имеющий значение True
* num_of_devices — атрибут, имеющий значение 4
* price — атрибут, имеющий значение 15.99$

##### Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.
##### Примечание 2. Никаких ограничений касательно реализации классов нет, она может быть произвольной.

<table align="center">
  <tbody>
    <tr>
      <th>Sample Input 1: </th>
      <th>Sample Input 2: </th>
      <th>Sample Input 3: </th>
    </tr>
    <tr>
      <td align="center">print(BasicPlan.can_stream)<br>
                          print(BasicPlan.can_download)<br>
                          print(BasicPlan.has_SD)<br>
                          print(BasicPlan.has_HD)<br>
                          print(BasicPlan.has_UHD)<br>
                          print(BasicPlan.num_of_devices)<br>
                          print(BasicPlan.price)<br></td>
      <td align="center">print(SilverPlan.can_stream)<br>
                          print(SilverPlan.can_download)<br>
                          print(SilverPlan.has_SD)<br>
                          print(SilverPlan.has_HD)<br>
                          print(SilverPlan.has_UHD)<br>
                          print(SilverPlan.num_of_devices)<br>
                          print(SilverPlan.price)<br></td>
      <td align="center">print(GoldPlan.can_stream)<br>
                          print(GoldPlan.can_download)<br>
                          print(GoldPlan.has_SD)<br>
                          print(GoldPlan.has_HD)<br>
                          print(GoldPlan.has_UHD)<br>
                          print(GoldPlan.num_of_devices)<br>
                          print(GoldPlan.price)<br></td>
    </tr>
    <tr>
      <td>Sample Output 1:</td>
      <td>Sample Output 2:</td>
      <td>Sample Output 3:</td>
      </tr>
    <tr>
      <td align="center">
                        True<br>
                        True<br>
                        True<br>
                        False<br>
                        False<br>
                        1<br>
                        8.99$<br>
      </td>
      <td align="center">
                        True<br>
                        True<br>
                        True<br>
                        True<br>
                        False<br>
                        2<br>
                        12.99$<br>
      </td>
      <td align="center">
                        True<br>
                        True<br>
                        True<br>
                        True<br>
                        True<br>
                        4<br>
                        15.99$<br>
      </td>
    </tr>
  </tbody>
</table>



## Примеры решений:
* Первый вариант решения
```python
class BasicPlan:
    can_stream = True
    can_download = True
    has_SD = True
    has_HD = False
    has_UHD = False
    num_of_devices = 1
    price = '8.99$'


class SilverPlan(BasicPlan):
    has_HD = True
    num_of_devices = 2
    price = '12.99$'


class GoldPlan(BasicPlan):
    has_HD = True
    has_UHD = True
    num_of_devices = 4
    price = '15.99$'
```
* Второй вариант решения

```python
class BasicPlan:
    can_stream = True
    can_download = True
    has_SD = True
    has_HD = False
    has_UHD = False
    num_of_devices = 1
    price = '8.99$'


class SilverPlan(BasicPlan):
    has_HD = True
    num_of_devices = 2
    price = '12.99$'


class GoldPlan(SilverPlan):
    has_UHD = True
    num_of_devices = 4
    price = '15.99$'
```


