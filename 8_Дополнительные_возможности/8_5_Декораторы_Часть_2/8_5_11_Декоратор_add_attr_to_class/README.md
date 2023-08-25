<h2 style="text-align:center">Декоратор @add_attr_to_class</h2>


### Реализуйте декоратор @add_attr_to_class для декорирования класса. Декоратор должен принимать произвольное количество именованных аргументов и добавлять их декорируемому классу в качестве атрибутов.

<table align="center">
  <tbody>
    <tr>
      <th>Sample Input 1: </th>
    </tr>
    <tr>
      <td align="center">@add_attr_to_class(first_attr=1, second_attr=2)<br>
                          class MyClass:<br>
                              pass<br>
                          print(MyClass.first_attr)<br>
                          print(MyClass.second_attr)<br></td>
    </tr>
    <tr>
      <td>Sample Output 1:</td>
      </tr>
    <tr>
      <td align="center">
                        1<br>
                        2<br>
      </td>
    </tr>
  </tbody>
</table>



## Примеры решений:
* Первый вариант решения
```python
def add_attr_to_class(**attrs):
    def decorator(cls):
        for k, v in attrs.items():
            setattr(cls, k, v)
        return cls
    return decorator
```
* Второй вариант решения

```python
class add_attr_to_class:
    def __init__(self, **kwargs):
        self.attrs = kwargs

    def __call__(self, cls):
        for attr_name, attr_value in self.attrs.items():
            setattr(cls, attr_name, attr_value)
        return cls
```


