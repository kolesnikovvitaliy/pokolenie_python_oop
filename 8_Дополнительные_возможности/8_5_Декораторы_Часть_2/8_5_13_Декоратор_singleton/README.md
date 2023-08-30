<h2 style="text-align:center">Декоратор @singleton</h2>

### Реализуйте декоратор @singleton для декорирования класса. Декоратор должен превращать декорируемый класс в синглтон, то есть в класс, при первом вызове создающий единственный свой экземпляр и при последующих вызовах возвращающий его же.

<table align="center">
  <tbody>
    <tr>
      <th>Sample Input 1: </th>
    </tr>
    <tr>
      <td align="center">@singleton<br>
                          class MyClass:<br>
                              pass<br>
                          obj1 = MyClass()<br>
                          obj2 = MyClass()<br>
                          print(obj1 is obj2)<br></td>
    </tr>
    <tr>
      <td>Sample Output 1:</td>
      </tr>
    <tr>
      <td align="center">
                        True<br>
      </td>
    </tr>
  </tbody>
</table>



## Примеры решений:
* Первый вариант решения
```python
def singleton(cls):
    cls._instance = None

    def decorator(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = object.__new__(cls)
        return cls._instance
    cls.__new__ = decorator
    return cls
```
* Второй вариант решения

```python
def singleton(cls):
    _instance = object.__new__(cls)
    
    def new_new(cls, *args, **kwargs):
        return _instance
    
    cls.__new__ = new_new
    return cls
```


