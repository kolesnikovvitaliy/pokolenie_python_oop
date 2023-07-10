<h2 style="text-align:center">Класс SortKey</h2>

### Реализуйте класс SortKey, описывающий ключ для сортировки объектов на основе значений их определенных атрибутов. При создании экземпляра класс должен принимать произвольное количество позиционных аргументов, каждый из которых представляет имя атрибута, участвующего в сортировке.

##### Примечание 1. Имена атрибутов при создании экземпляра класса SortKey передаются в порядке приоритета, то есть при сортировке сначала должно учитываться значение первого атрибута, затем второго, и так далее.
##### Примечание 2. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.
#### Примечание 3. Никаких ограничений касательно реализации класса SortKey нет, она может быть произвольной.
<table align="center">
  <tbody>
    <tr>
      <th>Sample Input 1: </th>
      <th>Sample Input 2: </th>
    </tr>
    <tr>
      <td align="center">class User:<br>
                          def __init__(self, name, age):<br>
                              self.name = name<br>
                              self.age = age<br>
                          def __repr__(self):<br>
                              return f'User({self.name}, {self.age})'<br>
                      users = [User('Gvido', 67), User('Timur', 30), User('Arthur', 20), User('Timur', 45), User<br>('Gvido', 60)]<br>
                      print(sorted(users, key=SortKey('name')))<br>
                      print(sorted(users, key=SortKey('name', 'age')))<br>
                      print(sorted(users, key=SortKey('age')))<br>
                      print(sorted(users, key=SortKey('age', 'name')))<br></td>
      <td align="center">class User:<br>
                          def __init__(self, name, age):<br>
                              self.name = name<br>
                              self.age = age<br>
                          def __repr__(self):<br>
                              return f'User({self.name}, {self.age})'<br>
                      users = [User('Gvido', 67), User('Timur', 30), User('Arthur', 20), User('Timur', 45), User<br>('Gvido', 60)]<br>
                      print(max(users, key=SortKey('name')))<br>
                      print(max(users, key=SortKey('age')))<br>
                      print(max(users, key=SortKey('name', 'age')))<br>
                      print(max(users, key=SortKey('age', 'name')))<br></td>
    </tr>
    <tr>
      <td>Sample Output 1:</td>
      <td>Sample Output 2:</td>
      </tr>
    <tr>
      <td align="center">
                        [User(Arthur, 20), User(Gvido, 67), User(Gvido, 60), User(Timur, 30), User(Timur, 45)]<br>
                        [User(Arthur, 20), User(Gvido, 60), User(Gvido, 67), User(Timur, 30), User(Timur, 45)]<br>
                        [User(Arthur, 20), User(Timur, 30), User(Timur, 45), User(Gvido, 60), User(Gvido, 67)]<br>
                        [User(Arthur, 20), User(Timur, 30), User(Timur, 45), User(Gvido, 60), User(Gvido, 67)]<br>
      </td>
      <td align="center">
                        User(Timur, 30)<br>
                        User(Gvido, 67)<br>
                        User(Timur, 45)<br>
                        User(Gvido, 67)<br>
      </td>
    </tr>
  </tbody>
</table>



## Примеры решений:
* Первый вариант решения
```python
class SortKey:
    def __init__(self, *args):
       self.arg = args

    def __call__(self, obj):
        __result = []
        for key in self.arg:
            __result.append(obj.__dict__[key])
        return __result
```
* Второй вариант решения

```python
class SortKey:
    def __init__(self, *attributes):
        self.attributes = attributes

    def __call__(self, instance):
        return [getattr(instance, attribute) for attribute in self.attributes]
```


