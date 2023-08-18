<h2 style="text-align:center">Иерархия классов </h2>

### С помощью наследования и приведенной ниже схемы постройте иерархию пустых классов:

<div>
<img align="center" src="https://github.com/kolesnikovvitaliy/pokolenie_python_oop/blob/main/7_Наследование_и_полиморфизм/7_6_Множественное_наследование/7_6_22_Иерархия_классов/img/task.png" title="Git" **alt="Git">
​</div>

<table align="center">
  <tbody>
    <tr>
      <th>Sample Input 1: </th>
      <th>Sample Input 2: </th>
      <th>Sample Input 3: </th>
    </tr>
    <tr>
      <td align="center">print(issubclass(D, H))<br>
                        print(issubclass(E, H))<br>
                        print(issubclass(F, H))<br>
                        print(issubclass(G, H))<br></td>
      <td align="center">print(issubclass(B, D))<br>
                        print(issubclass(B, E))<br>
                        print(issubclass(B, F))<br>
                        print(issubclass(B, G))<br></td>
      <td align="center">print(issubclass(C, D))<br>
                        print(issubclass(C, E))<br>
                        print(issubclass(C, F))<br>
                        print(issubclass(C, G))<br></td>
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
                        True<br>
      </td>
      <td align="center">
                        True<br>
                        True<br>
                        False<br>
                        False<br>
      </td>
      <td align="center">
                        False<br>
                        False<br>
                        True<br>
                        True<br>
      </td>
    </tr>
  </tbody>
</table>



## Примеры решений:
* Первый вариант решения
```python
class H:
    pass


class D(H):
    pass


class E(H):
    pass


class F(H):
    pass


class G(H):
    pass


class B(D, E):
    pass


class C(F, G):
    pass


class A(B, C):
    pass
```
* Второй вариант решения

```python
class H: ...

class D(H): ...
class E(H): ...
class F(H): ...
class G(H): ...

class B(D, E): ...
class C(F, G): ...

class A(B, C): ...
```


