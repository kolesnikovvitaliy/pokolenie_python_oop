<h2 style="text-align:center">Декоратор @jsonattr</h2>

### Реализуйте декоратор @jsonattr для декорирования класса. Декоратор должен принимать один аргумент:

* filename — имя json файла, содержимым которого является JSON объект
#### Декоратор должен открывать файл filename и добавлять в качестве атрибута декорируемому классу каждую пару ключ-значение JSON объекта, содержащегося в этом файле.

<table align="center">
  <tbody>
    <tr>
      <th>Sample Input 1: </th>
    </tr>
    <tr>
      <td align="center">with open('test.json', 'w') as file:<br>
                              file.write('{"x": 1, "y": 2}')<br>
                          @jsonattr('test.json')<br>
                          class MyClass:<br>
                              pass<br>
                          print(MyClass.x)<br>
                          print(MyClass.y)<br></td>
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
import json


def jsonattr(filename):
    def decorator(cls):
        with open(filename, 'r', encoding='utf-8') as file:
            for attr, volue in json.loads(file.read()).items():
                setattr(cls, attr, volue)
        return cls
    return decorator
```
* Второй вариант решения

```python
import json


def jsonattr(filename):
    def wrapper(cls):
        with open(filename) as js:
            attrs = json.load(js)
        for attr, value in attrs.items():
            setattr(cls, attr, value)

        return cls

    return wrapper
```


