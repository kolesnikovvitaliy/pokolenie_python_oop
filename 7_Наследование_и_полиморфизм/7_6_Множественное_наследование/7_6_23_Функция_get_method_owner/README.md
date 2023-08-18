<h2 style="text-align:center">Функция get_method_owner()</h2>


### Реализуйте функцию get_method_owner(), которая принимает два аргумента в следующем порядке:
* cls — произвольный класс
* method — строковое название метода
#### Функция должна возвращать класс, от которого класс cls унаследовал метод method. Если метода method нет ни в самом классе, ни в одном другом классе из его иерархии, функция get_method_owner() должна вернуть значение None.

##### Примечание 1. В тестирующую систему сдайте программу, содержащую только необходимую функцию get_method_owner(), но не код, вызывающий ее.
##### Примечание 2. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.

<table align="center">
  <tbody>
    <tr>
      <th>Sample Input 1: </th>
      <th>Sample Input 2: </th>
      <th>Sample Input 3: </th>
    </tr>
    <tr>
      <td align="center">class A:<br>
                              def m(self):<br>
                                  pass<br>
                          class B(A):<br>
                              pass<br>
                          print(get_method_owner(B, 'm'))<br></td>
      <td align="center">class A:<br>
                              def m(self):<br>
                                  pass<br>
                          class B(A):<br>
                              def m(self):<br>
                                  pass<br>
                          print(get_method_owner(B, 'm'))<br></td>
      <td align="center">class A:<br>
                              pass<br>
                          class B(A):<br>
                              pass<br>
                          print(get_method_owner(B, 'm'))<br></td>
    </tr>
    <tr>
      <td>Sample Output 1:</td>
      <td>Sample Output 2:</td>
      <td>Sample Output 3:</td>
      </tr>
    <tr>
      <td align="center">
                        class '__main__.A'<br>
      </td>
      <td align="center">
                        class '__main__.B'<br>
      </td>
      <td align="center">
                        None<br>
      </td>
    </tr>
  </tbody>
</table>



## Примеры решений:
* Первый вариант решения
```python
def get_method_owner(cls, method):
    for class_ in cls.mro()[:-1]:
        if method in class_.__dict__:
            return class_
    return None
```
* Второй вариант решения

```python
def get_method_owner(cls, method):
    '''Return class location of method'''
    for el in cls.mro():
        if method in el.__dict__:
            return el
```


