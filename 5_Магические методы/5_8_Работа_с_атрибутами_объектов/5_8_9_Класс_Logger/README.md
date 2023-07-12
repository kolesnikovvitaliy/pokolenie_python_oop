<h2 style="text-align:center">Класс Logger</h2>


### Требовалось реализовать класс Logger. При создании экземпляра класс не должен был принимать никаких аргументов.

> Изменение значения атрибута <имя атрибута> на <новое значение атрибута>

#### Также планировалось, что при удалении атрибута будет выводиться текст:
> Удаление атрибута <имя атрибута>


#### Программист торопился и решил задачу неправильно. Дополните приведенный ниже код и реализуйте правильный класс Logger.
```python
class Logger:
    def __setattr__(self, name, value):
        print(f'Изменение значения атрибута {name} на {value}')
        self.name = value

    def __delattr__(self, name):
        print(f'Удаление атрибута {name}')
        del self.name
```

##### Примечание. Никаких ограничений касательно реализации класса Logger нет, она может быть произвольной.


<table align="center">
  <tbody>
    <tr>
      <th>Sample Input 1: </th>
      <th>Sample Input 2: </th>
    </tr>
    <tr>
      <td align="center">obj = Logger()<br>
                        obj.attr = 1<br>
                        del obj.attr<br></td>
      <td align="center">obj = Logger()<br>
                          obj.name = 'pygen'<br>
                          obj.rating = '5*'<br>
                          obj.ceo = 'Timur'<br>
                          del obj.rating<br>
                          obj.rating = '6*'<br></td>
    </tr>
    <tr>
      <td>Sample Output 1:</td>
      <td>Sample Output 2:</td>
      </tr>
    <tr>
      <td align="center">
                        Изменение значения атрибута attr на 1<br>
                        Удаление атрибута attr<br>
      </td>
      <td align="center">
                        Изменение значения атрибута name на pygen<br>
                        Изменение значения атрибута rating на 5*<br>
                        Изменение значения атрибута ceo на Timur<br>
                        Удаление атрибута rating<br>
                        Изменение значения атрибута rating на 6*<br>
      </td>
    </tr>
  </tbody>
</table>



## Примеры решений:
* Первый вариант решения
```python
class Logger:
    def __setattr__(self, name, value):
        print(f'Изменение значения атрибута {name} на {value}')
        self.__dict__[name] = value
        # self.__dict__[attr] = value

    def __delattr__(self, name):
        print(f'Удаление атрибута {name}')
        del self.__dict__[name]
```
* Второй вариант решения

```python
class Logger:
    def __setattr__(self, name, value):
        print(f'Изменение значения атрибута {name} на {value}')
        object.__setattr__(self, name, value)

    def __delattr__(self, name):
        print(f'Удаление атрибута {name}')
        object.__delattr__(self, name)
```


