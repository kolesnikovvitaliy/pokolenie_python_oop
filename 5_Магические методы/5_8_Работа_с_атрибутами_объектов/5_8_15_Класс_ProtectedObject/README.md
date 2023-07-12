<h2 style="text-align:center">Класс ProtectedObject</h2>


### Будем считать атрибут защищенным, если его имя начинается с символа нижнего подчеркивания (_). Например, _password, __email и __dict__.
#### Реализуйте класс ProtectedObject. При создании экземпляра класс должен принимать произвольное количество именованных аргументов. Все передаваемые аргументы должны устанавливаться создаваемому экземпляру в качестве атрибутов.

#### Класс ProtectedObject должен запрещать получать и изменять значения защищенных атрибутов своих экземпляров, а также удалять эти атрибуты. При попытке получить или изменить значение защищенного атрибута, а также попытке удалить атрибут, должно возбуждаться исключение AttributeError с текстом:
> Доступ к защищенному атрибуту невозможен
##### Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.
##### Примечание 2. Никаких ограничений касательно реализации класса ProtectedObject нет, она может быть произвольной.

<table align="center">
  <tbody>
    <tr>
      <th>Sample Input 1: </th>
    </tr>
    <tr>
      <td align="center">user = ProtectedObject(login='PG_kamiya', _password='alreadybanned')<br>
                        try:<br>
                            print(user.login)<br>
                            print(user._password)<br>
                        except AttributeError as e:<br>
                            print(e)<br></td>
    </tr>
    <tr>
      <td>Sample Output 1:</td>
      </tr>
    <tr>
      <td align="center">
                        PG_kamiya<br>
                        Доступ к защищенному атрибуту невозможен<br>
      </td>
    </tr>
  </tbody>
</table>



## Примеры решений:
* Первый вариант решения
```python
class ProtectedObject:
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            object.__setattr__(self, k, v)

    def __getattribute__(self, __name: str):
        if __name.startswith('_'):
            raise AttributeError('Доступ к защищенному атрибуту невозможен')
        return object.__getattribute__(self, __name)
    
    def __setattr__(self, __name: str, __value):
        if __name.startswith('_'):
            raise AttributeError('Доступ к защищенному атрибуту невозможен')
        return object.__setattr__(self, __name, __value)
    
    def __delattr__(self, __name: str):
        if __name.startswith('_'):
            raise AttributeError('Доступ к защищенному атрибуту невозможен')
        return object.__delattr__(self, __name)
```
* Второй вариант решения

```python
class ProtectedObject:    
    def __init__(self, **kwargs):
        for attr, value in kwargs.items():
            object.__setattr__(self, attr, value) 
        
    @staticmethod
    def _check_access(attr):
        if attr.startswith('_'):
            msg = 'Доступ к защищенному атрибуту невозможен'
            raise AttributeError(msg)
    
    def __getattribute__(self, attr):
        ProtectedObject._check_access(attr)
        return object.__getattribute__(self, attr)
       
    def __setattr__(self, attr, value):
        ProtectedObject._check_access(attr)
        object.__setattr__(self, attr, value)
        
    def __delattr__(self, attr):
        ProtectedObject._check_access(attr)
        object.__delattr__(self, attr)
```


