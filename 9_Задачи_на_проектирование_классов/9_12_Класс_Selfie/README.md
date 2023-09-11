<h2 style="text-align:center">Класс Selfie</h2>

### Реализуйте класс Selfie, экземпляры которого запоминают свои предыдущие состояния и умеют восстанавливаться до тех состояний, в которых они были раньше. Под состоянием объекта понимается определенный набор атрибутов и соответствующих значений. Во время жизни экземпляр класса Selfie может различными способами изменять свое состояние, например, получать новые атрибуты или изменять значения имеющихся:

```python 
obj = Selfie()

obj.x = 1
obj.y = 2
```
#### Для фиксации текущего состояния экземпляра класса Selfie должен использоваться метод save_state(): 
```python 
obj.save_state()              # фиксируем состояние: x=1, y=2
obj.x = 0                     # изменяем состояние
obj.y = 0                     # изменяем состояние
```
#### Зафиксированные состояния экземпляра класса Selfie должны индексироваться: первое зафиксированное состояние должно иметь индекс 0, второе — 1, третье — 2, и так далее. По этим же индексам должна быть возможность возвращаться к необходимым состояниям:
```python 
print(obj.x)                  # 0
print(obj.y)                  # 0
obj = obj.recover_state(0)    # возвращаемся к первому состоянию
print(obj.x)                  # 1
print(obj.y)                  # 2
```
#### Обратите внимание, что при возвращении к одному из предыдущих состояний с помощью метода recover_state() должен возвращаться новый экземпляр класса Selfie, имеющий необходимое состояние. Если в метод recover_state() передан индекс, по которому экземпляр класса Selfie не имеет состояния, должен быть возвращен текущий экземпляр:
```python 
obj = obj.recover_state(7)
print(obj.x)                  # 1
print(obj.y)                  # 2
```
#### Каждый экземпляр класса Selfie должен знать, сколько состояний он зафиксировал:
```python 
obj = Selfie()

print(obj.n_states())         # 0
obj.x = 0
obj.save_state()
obj.x = 1
obj.save_state()
obj.x = 2
obj.save_state()
print(obj.n_states())         # 3
```

<table align="center">
  <tbody>
    <tr>
      <th>Sample Input 1: </th>
      <th>Sample Input 2: </th>
    </tr>
    <tr>
      <td align="center">obj = Selfie()<br>
                          obj.x = 1<br>
                          obj.y = 2<br>
                          print(obj.x)<br>
                          print(obj.y)<br>
                          obj.save_state()<br>
                          obj.x = 0<br>
                          obj.y = 0<br>
                          print(obj.x)<br>
                          print(obj.y)<br>
                          obj = obj.recover_state(0)<br>
                          print(obj.x)<br>
                          print(obj.y)<br></td>
      <td align="center">obj = Selfie()<br>
                          print(obj.n_states())<br>
                          obj.x = 0<br>
                          obj.save_state()<br>
                          obj.x = 1<br>
                          obj.save_state()<br>
                          obj.x = 2<br>
                          obj.save_state()<br>
                          print(obj.n_states())<br></td>
    </tr>
    <tr>
      <td>Sample Output 1:</td>
      <td>Sample Output 2:</td>
      </tr>
    <tr>
      <td align="center">
                        1<br>
                        2<br>
                        0<br>
                        0<br>
                        1<br>
                        2<br>
      </td>
      <td align="center">
                        0<br>
                        3<br>
      </td>
    </tr>
  </tbody>
</table>



## Примеры решений:
* Первый вариант решения
```python
from copy import deepcopy


class Selfie:
    def __init__(self):
        self._history = []

    def save_state(self):
        self._history.append(deepcopy(self))

    def recover_state(self, n):
        if len(self._history) > n:
            return self._history[n]
        return self

    def n_states(self):
        return len(self._history)
```
* Второй вариант решения

```python
from copy import deepcopy


class Selfie:
    def __init__(self):
        self.states = {}

    def save_state(self):
        self.states[len(self.states)] = deepcopy(self)

    def recover_state(self, n):
        return self.states[n] if n in self.states else self

    def n_states(self):
        return len(self.states)
```


