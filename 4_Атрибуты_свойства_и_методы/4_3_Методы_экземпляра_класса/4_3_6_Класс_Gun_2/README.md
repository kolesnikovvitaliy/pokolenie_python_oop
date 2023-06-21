<h2 style="text-align:center">Класс Gun_2</h2>

### Реализуйте класс Gun, описывающий ружье. При создании экземпляра класс не должен принимать никаких аргументов.
#### Класс Gun должен иметь один метод экземпляра:
* shoot() — метод, при первом вызове которого выводится строка pif, при втором — paf, при третьем — pif, при четвертом — paf, и так далее

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
                       paf<br>
                       pif<br>
                       paf<br>
      </td>
    </tr>
  </tbody>
</table>



## Примеры решений:
* Первый вариант решения
```python
class Gun:
    def __init__(self):
        self.count = 0

    def shoot(self):
        a = ['pif','paf']
        if self.count % 2 == 0:
            print(a[0])
        else: print(a[1])
        self.count += 1
```
* Второй вариант решения
```python
from itertools import cycle


class Gun:
    def __init__(self):
        self.shots = cycle(('pif', 'paf'))
        
    def shoot(self):
        print(next(self.shots))
```


