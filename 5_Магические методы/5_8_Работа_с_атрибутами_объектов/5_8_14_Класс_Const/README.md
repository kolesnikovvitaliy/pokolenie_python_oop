<h2 style="text-align:center">Класс Const</h2>

### Реализуйте класс Const. При создании экземпляра класс должен принимать произвольное количество именованных аргументов. Все передаваемые аргументы должны устанавливаться создаваемому экземпляру в качестве атрибутов.
#### Класс Const должен разрешать устанавливать атрибуты своим экземплярам и получать их значения, но не разрешать изменять значения этих атрибутов, а также удалять их. При попытке изменить значение атрибута должно возбуждаться исключение AttributeError с текстом:
> Изменение значения атрибута невозможно

#### При попытке удалить атрибут должно возбуждаться исключение AttributeError с текстом:
> Удаление атрибута невозможно

##### Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.
##### Примечание 2. Никаких ограничений касательно реализации класса Const нет, она может быть произвольной.

<table align="center">
  <tbody>
    <tr>
      <th>Sample Input 1: </th>
      <th>Sample Input 2: </th>
      <th>Sample Input 3: </th>
    </tr>
    <tr>
      <td align="center">videogame = Const(name='Cuphead')<br>
                          videogame.developer = 'Studio MDHR'<br>
                          print(videogame.name)<br>
                          print(videogame.developer)<br></td>
      <td align="center">videogame = Const(name='Dicso Elysium')<br>
                          try:<br>
                              videogame.name = 'Half-Life: Alyx'<br>
                          except AttributeError as e:<br>
                              print(e)<br></td>
      <td align="center">videogame = Const(name='The Last of Us')
                          try:<br>
                              del videogame.name<br>
                          except AttributeError as e:<br>
                              print(e)<br></td>
    </tr>
    <tr>
      <td>Sample Output 1:</td>
      <td>Sample Output 2:</td>
      <td>Sample Output 3:</td>
      </tr>
    <tr>
      <td align="center">
                        Cuphead<br>
                        Studio MDHR<br>
      </td>
      <td align="center">
                        Изменение значения атрибута невозможно<br>
      </td>
      <td align="center">
                        Удаление атрибута невозможно<br>
      </td>
    </tr>
  </tbody>
</table>



## Примеры решений:
* Первый вариант решения
```python
class Const:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def __setattr__(self, __name: str, __value):
        if __name in self.__dict__:
            raise AttributeError('Изменение значения атрибута невозможно')
        return object.__setattr__(self, __name, __value)
    
    def __getattribute__(self, __name: str):
        return object.__getattribute__(self, __name)
    
    def __delattr__(self, __name: str):
        raise AttributeError('Удаление атрибута невозможно')
```
* Второй вариант решения

```python
class Const:
    def __init__(self, **kwargs): 
        self.__dict__.update(kwargs)
        
    def __setattr__(self, name, value):
        if hasattr(self, name):
            raise AttributeError('Изменение значения атрибута невозможно')
        super().__setattr__(name, value)
        
    def __delattr__(self, name): 
        raise AttributeError('Удаление атрибута невозможно')       
```


