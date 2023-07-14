<h2 style="text-align:center">Класс AttrsIterator</h2>


### Реализуйте класс AttrsIterator. При создании экземпляра класс должен принимать один аргумент:
* obj — произвольный объект
#### Экземпляр класса AttrsIterator должен являться итератором, который генерирует все атрибуты объекта obj в виде кортежей из двух элементов, первый из которых представляет имя атрибута, второй — значение атрибута.
#### Класс Rectangle должен иметь два свойства:
##### Примечание 1. Порядок атрибутов при генерации должен совпадать с их порядком в словаре атрибутов __dict__.
##### Примечание 2. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.
#### Примечание 3. Класс AttrsIterator должен удовлетворять протоколу итератора, то есть иметь методы __iter__() и __next__(). Реализация же протокола может быть произвольной.

<table align="center">
  <tbody>
    <tr>
      <th>Sample Input 1: </th>
    </tr>
    <tr>
      <td align="center">class User:<br>
                              def __init__(self, name, surname, age):<br>
                                  self.name = name<br>
                                  self.surname = surname<br>
                                  self.age = age<br>
                          user = User('Debbie', 'Harry', 77)<br>
                          attrsiterator = AttrsIterator(user)<br>
                          print(*attrsiterator)<br>
<br></td>
    </tr>
    <tr>
      <td>Sample Output 1:</td>
      </tr>
    <tr>
      <td align="center">
                        ('name', 'Debbie') ('surname', 'Harry') ('age', 77)<br>
      </td>
    </tr>
  </tbody>
</table>



## Примеры решений:
* Первый вариант решения
```python
class AttrsIterator:
    def __init__(self, object):
        self.__lst_object = list(object.__dict__.items())
        self.__i = 0

    def __iter__(self):
        yield from self.__lst_object
    
    def __next__(self):
        if self.__i > len(self.__lst_object)-1:
            raise StopIteration
        self.__i += 1
        return self.__lst_object[self.__i-1]
```
* Второй вариант решения

```python
class AttrsIterator:
    def __init__(self, obj):
        self.iterator = iter(obj.__dict__.items())
        
    def __iter__(self):
        return self
    
    def __next__(self):
        return next(self.iterator)
```


