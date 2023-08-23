<h2 style="text-align:center">Класс OrderStatus</h2>

### Реализуйте класс OrderStatus, описывающий флаг с состояниями интернет-заказов. Флаг должен иметь три элемента:

* ORDER_PLACED
* PAYMENT_RECEIVED
* SHIPPING_COMPLETE
##### Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.

##### Примечание 2. Никаких ограничений касательно реализации класса OrderStatus нет, она может быть произвольной.

<table align="center">
  <tbody>
    <tr>
      <th>Sample Input 1: </th>
    </tr>
    <tr>
      <td align="center">order_status = OrderStatus(0)<br>
                        order_status |= OrderStatus.ORDER_PLACED<br>
                        if OrderStatus.ORDER_PLACED in order_status:<br>
                            print('Заказ оформлен!')<br>
                        order_status |= OrderStatus.PAYMENT_RECEIVED<br>
                        if OrderStatus.PAYMENT_RECEIVED in order_status:<br>
                            print('Оплата получена!')<br>
                        order_status |= OrderStatus.SHIPPING_COMPLETE<br>
                        if OrderStatus.SHIPPING_COMPLETE in order_status:<br>
                            print('Доставка завершена!')<br></td>
    </tr>
    <tr>
      <td>Sample Output 1:</td>
      </tr>
    <tr>
      <td align="center">
                        Заказ оформлен!<br>
                        Оплата получена!<br>
                        Доставка завершена!<br>
      </td>
    </tr>
  </tbody>
</table>



## Примеры решений:
* Первый вариант решения
```python
from enum import Flag


class OrderStatus(Flag):
    ORDER_PLACED = 0b1
    PAYMENT_RECEIVED = 0b1_0
    SHIPPING_COMPLETE = 0b1_00
```
* Второй вариант решения

```python
from enum import Flag, auto


class OrderStatus(Flag):
    ORDER_PLACED = auto()
    PAYMENT_RECEIVED = auto()
    SHIPPING_COMPLETE = auto()
```


