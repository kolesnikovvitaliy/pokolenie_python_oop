<h2 style="text-align:center">Класс Gun_3</h2>

### Реализуйте класс Gun, описывающий ружье. При создании экземпляра класс не должен принимать никаких аргументов.


#### Класс Gun должен иметь три метода экземпляра:
* shoot() — метод, при первом вызове которого выводится строка pif, при втором — paf, при третьем — pif, при четвертом — paf, и так далее
* shots_count() — метод, возвращающий актуальное количество вызовов метода shoot()
* shots_reset() — метод, сбрасывающий количество вызовов метода shoot() до нуля

<table align="center">
  <tbody>
    <tr>
      <th>Sample Input 1: </th>
      <th>Sample Input 2: </th>
    </tr>
    <tr>
      <td align="center">gun = Gun()<br>
                        print(gun.shots_count())<br>
                        gun.shoot()<br>
                        print(gun.shots_count())<br>
                        gun.shoot()<br>
                        print(gun.shots_count())<br></td>
      <td align="center">gun = Gun()<br>
                         gun.shoot()<br>
                          gun.shoot()<br>
                          print(gun.shots_count())<br>
                          gun.shots_reset()<br>
                          print(gun.shots_count())<br>
                          gun.shoot()<br>
                          print(gun.shots_count())<br></td>
    </tr>
    <tr>
      <td>Sample Output 1:</td>
      <td>Sample Output 2:</td>
      </tr>
    <tr>
      <td align="center">
                          0<br>
                          pif<br>
                          1<br>
                          paf<br>
                          2<br>
      </td>
      <td align="center">
                       pif<br>
                        paf<br>
                        2<br>
                        0<br>
                        pif<br>
                        1<br>
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
        if self.count % 2:
            print('paf')
        else: print('pif')
        self.count += 1

    def shots_count(self):
        return self.count

    def shots_reset(self):
        self.count = 0
        return self.count
```
* Второй вариант решения
```python
class Gun:
    def __init__(self):
        self.count = 0
        
    def shoot(self):
        print(('pif', 'paf')[self.count%2])
        self.count += 1
        
    def shots_count(self):
        return self.count
    
    def shots_reset(self):
        self.count = 0
```


