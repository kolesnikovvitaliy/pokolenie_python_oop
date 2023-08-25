<h2 style="text-align:center">Декоратор @track_instances</h2>

### Реализуйте декоратор @track_instances для декорирования класса. Декоратор должен добавлять декорируемому классу атрибут instances, содержащий список всех созданных экземпляров этого класса.

##### Примечание 1. Экземпляры декорируемого класса в списке по атрибуту instances должны располагаться в том порядке, в котором они были созданы.



<table align="center">
  <tbody>
    <tr>
      <th>Sample Input 1: </th>
    </tr>
    <tr>
      <td align="center">@track_instances<br>
                          class Person:<br>
                              def __init__(self, name):<br>
                                  self.name = name<br>
                              def __repr__(self):<br>
                                  return f'Person({self.name!r})'<br>
                          obj1 = Person('object 1')<br>
                          obj2 = Person('object 2')<br>
                          print(Person.instances)<br></td>
    </tr>
    <tr>
      <td>Sample Output 1:</td>
      </tr>
    <tr>
      <td align="center">
                        [Person('object 1'), Person('object 2')]<br>
      </td>
    </tr>
  </tbody>
</table>



## Примеры решений:
* Первый вариант решения
```python
import functools


def track_instances(cls):
    old_init = cls.__init__
    cls.instances = []

    @functools.wraps(old_init)
    def decorator(self, *args, **kwargs):
        old_init(self, *args, **kwargs)
        cls.instances.append(self)
    cls.__init__ = decorator
    return cls
```
* Второй вариант решения

```python
import functools


def track_instances(cls):
    cls_init = cls.__init__
    cls.instances = []

    @functools.wraps(cls_init)
    def new_init(self, *args, **kwargs):
        cls_init(self, *args, **kwargs)
        self.instances.append(self)

    cls.__init__ = new_init
    return cls
```


