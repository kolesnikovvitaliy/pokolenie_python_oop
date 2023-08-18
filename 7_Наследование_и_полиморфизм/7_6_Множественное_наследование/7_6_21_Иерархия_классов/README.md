<h2 style="text-align:center">Иерархия классов </h2>

### С помощью наследования и приведенной ниже схемы постройте иерархию пустых классов:

<div>
<img align="center" src="https://github.com/kolesnikovvitaliy/pokolenie_python_oop/blob/main/7_Наследование_и_полиморфизм/7_6_Множественное_наследование/7_6_21_Иерархия_классов/img/task.png" title="Git" **alt="Git">
​</div>

<table align="center">
  <tbody>
    <tr>
      <th>Sample Input 1: </th>
      <th>Sample Input 2: </th>
    </tr>
    <tr>
      <td align="center">print(issubclass(E, B))<br>
                        print(issubclass(E, C))<br>
                        print(issubclass(E, D))<br></td>
      <td align="center">print(issubclass(B, A))<br>
                          print(issubclass(C, A))<br>
                          print(issubclass(D, A))<br></td>
    </tr>
    <tr>
      <td>Sample Output 1:</td>
      <td>Sample Output 2:</td>
      </tr>
    <tr>
      <td align="center">
                        True<br>
                        False<br>
                        True<br>
      </td>
      <td align="center">
                        True<br>
                        True<br>
                        True<br>
      </td>
    </tr>
  </tbody>
</table>



## Примеры решений:
* Первый вариант решения
```python
class A:
    pass


class B(A):
    pass


class D(A):
    pass


class C(A):
    pass


class E(B, D):
    pass
```
* Второй вариант решения

```python
class A: ...

class B(A): ...
class C(A): ...
class D(A): ...

class E(B, D): ...
```


