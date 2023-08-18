<h2 style="text-align:center">Класс MROHelper</h2>



### Реализуйте класс MROHelper, описывающий набор функций для работы с MRO произвольных классов. При создании экземпляра класс не должен принимать никаких аргументов.
#### Класс MROHelper должен иметь три статических метода:
* len() — метод, принимающий в качестве аргумента класс и возвращающий количество элементов в его MRO
* class_by_index() — метод, принимающий в качестве аргументов класс cls и целое число n, по умолчанию равное нулю, и возвращающий класс с индексом n в MRO класса cls
* index_by_class() — метод, принимающий в качестве аргументов два класса child и parent и возвращающий целое число — индекс класса parent в MRO класса child

##### Примечание 1. Нумерация классов в MRO начинается с нуля.
##### Примечание 2. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.
##### Примечание 3. Никаких ограничений касательно реализации класса MROHelper нет, она может быть произвольной.

<table align="center">
  <tbody>
    <tr>
      <th>Sample Input 1: </th>
      <th>Sample Input 2: </th>
      <th>Sample Input 3: </th>
    </tr>
    <tr>
      <td align="center">class A:<br>
                              pass<br>
                          class B(A):<br>
                              pass<br>
                          class C(A):<br>
                              pass<br>
                          class D(B, C):<br>
                              pass<br>
                          print(MROHelper.len(D))<br></td>
      <td align="center">class A:<br>
                              pass<br>
                          class B(A):<br>
                              pass<br>
                          class C(A):<br>
                              pass<br>
                          class D(B, C):<br>
                              pass<br>
                          print(MROHelper.class_by_index(D, 2))<br>
                          print(MROHelper.class_by_index(B))<br></td>
      <td align="center">class A:<br>
                              pass<br>
                          class B(A):<br>
                              pass<br>
                          class C(A):<br>
                              pass<br>
                          class D(B, C):<br>
                              pass<br>
                          print(MROHelper.index_by_class(D, A))<br></td>
    </tr>
    <tr>
      <td>Sample Output 1:</td>
      <td>Sample Output 2:</td>
      <td>Sample Output 3:</td>
      </tr>
    <tr>
      <td align="center">
                        5<br>
      </td>
      <td align="center">
                        class '__main__.C'<br>
                        class '__main__.B'<br>
      </td>
      <td align="center">
                        3<br>
      </td>
    </tr>
  </tbody>
</table>



## Примеры решений:
* Первый вариант решения
```python
class MROHelper:
    @staticmethod
    def len(cls):
        return len(cls.mro())

    @staticmethod
    def class_by_index(cls, n=0):
        return cls.mro()[n]

    @staticmethod
    def index_by_class(child, parent):
        return child.mro().index(parent)
```
* Второй вариант решения

```python
class MROHelper:

    @staticmethod
    def len(cls):
        return len(cls.__mro__)

    @staticmethod
    def class_by_index(child, n=0):
        return child.__mro__[n]

    @staticmethod
    def index_by_class(child, parent):
        return child.__mro__.index(parent)
```


