<h2 style="text-align:center">Класс DefaultObject</h2>

### Реализуйте класс DefaultObject. При создании экземпляра класс должен принимать один именованный аргумент default, имеющий значение по умолчанию None, а после произвольное количество именованных аргументов. Аргументы, передаваемые после default, должны устанавливаться создаваемому экземпляру в качестве атрибутов.

#### При обращении к несуществующему атрибуту экземпляра класса DefaultObject должно возвращаться значение default.

##### Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.
##### Примечание 2. Никаких ограничений касательно реализации класса DefaultObject нет, она может быть произвольной.



<table align="center">
  <tbody>
    <tr>
      <th>Sample Input 1: </th>
      <th>Sample Input 2: </th>
    </tr>
    <tr>
      <td align="center">god = DefaultObject(name='Ares', mythology='greek')
                        print(god.name)
                        print(god.mythology)
                        print(god.age)<br></td>
      <td align="center">god = DefaultObject(default=0, name='Tyr', mythology='scandinavian')
                        print(god.name)
                        print(god.mythology)
                        print(god.age)<br></td>
    </tr>
    <tr>
      <td>Sample Output 1:</td>
      <td>Sample Output 2:</td>
      </tr>
    <tr>
      <td align="center">
                        Ares
                          greek
                          None<br>
      </td>
      <td align="center">
                        Tyr
                        scandinavian
                        0<br>
      </td>
    </tr>
  </tbody>
</table>



## Примеры решений:
* Первый вариант решения
```python
class DefaultObject:
    def __init__(self, default=None, **kwargs):
        self.default = default
        for args in kwargs.items():
            setattr(self, *args)

    def __getattribute__(self, __name: str):
            return object.__getattribute__(self, __name)
    
    def __getattr__(self, __name: str):
        return self.default
        
```
* Второй вариант решения

```python
class DefaultObject:
    def __init__(self, default=None, **kwargs):
        self.default = default
        self.__dict__.update(kwargs)
        
    def __getattr__(self, name):
        return self.default
```


