<h2 style="text-align:center">Класс Gun</h2>

### Реализуйте класс Gun, описывающий ружье. При создании экземпляра класс не должен принимать никаких аргументов.
#### Класс Gun должен иметь один метод экземпляра:
* shoot() — метод, при вызове которого выводится строка pif



<table align="center">
  <tbody>
    <tr>
      <th>Sample Input 1: </th>
      <th>Sample Input 2: </th>
    </tr>
    <tr>
      <td align="center">gun = Gun()<br>
                         gun.shoot()<br></td>
      <td align="center">gun = Gun()<br>
                         gun.shoot()<br>
                         gun.shoot()<br>
                         gun.shoot()<br></td>
    </tr>
    <tr>
      <td>Sample Output 1:</td>
      <td>Sample Output 2:</td>
      </tr>
    <tr>
      <td align="center">
      pif<br>
      </td>
      <td align="center">
                        pif<br>
                        pif<br>
                        pif<br>
      </td>
    </tr>
  </tbody>
</table>



## Примеры решений:
* Первый вариант решения
```python
class Gun:
    def shoot(self):
        print('pif')
```
* Второй вариант решения
```python
class Gun():
    def __init__(self):
        pass
    def shoot(self):
        print('pif')
```


