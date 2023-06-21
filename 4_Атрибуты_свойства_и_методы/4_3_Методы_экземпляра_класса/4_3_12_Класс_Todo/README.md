<h2 style="text-align:center">Класс Todo</h2>

### Реализуйте класс Todo, описывающий список дел. При создании экземпляра класс не должен принимать никаких аргументов.
#### Экземпляр класса Todo должен иметь один атрибут:
* things — изначально пустой список дел, которые нужно выполнить

#### Класс Todo должен иметь четыре метода экземпляра:
* add() — метод, принимающий название дела и его приоритет (целое число) и добавляющий данное дело в список дел в виде кортежа:
(<название дела>, <приоритет>)
* get_by_priority() — метод, принимающий в качестве аргумента целое число n и возвращающий список названий дел, имеющих приоритет n
* get_low_priority() — метод, возвращающий список названий дел, имеющих самый низкий приоритет 
* get_high_priority() — метод, возвращающий список названий дел, имеющих самый высокий приоритет 

##### Примечание 1. Названия дел в списках, возвращаемых методами get_by_priority(), get_low_priority() и get_high_priority(), должны располагаться в том порядке, в котором они были добавлены в список.
##### Примечание 2. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.

<table align="center">
  <tbody>
    <tr>
      <th>Sample Input 1: </th>
      <th>Sample Input 2: </th>
      <th>Sample Input 3: </th>
    </tr>
    <tr>
      <td align="center">todo = Todo()<br>
                        print(todo.things)<br>
                        print(todo.get_by_priority(1))<br>
                        print(todo.get_low_priority())<br>
                        print(todo.get_high_priority())<br></td>
      <td align="center">todo = Todo()<br>
                        todo.add('Проснуться', 3)<br>
                        todo.add('Помыться', 2)<br>
                        todo.add('Поесть', 2)<br>
                        print(todo.get_by_priority(2))<br></td>
      <td align="center">todo = Todo()<br>
                          todo.add('Ответить на вопросы', 5)<br>
                          todo.add('Сделать картинки', 1)<br>
                          todo.add('Доделать задачи', 4)<br>
                          todo.add('Дописать конспект', 5)<br>
                          print(todo.get_low_priority())<br>
                          print(todo.get_high_priority())<br>
                          print(todo.get_by_priority(3))<br></td>
    </tr>
    <tr>
      <td>Sample Output 1:</td>
      <td>Sample Output 2:</td>
      <td>Sample Output 3:</td>
      </tr>
    <tr>
      <td align="center">
      []<br>
      []<br>
      []<br>
      []<br>
      </td>
      <td align="center">
                       ['Помыться', 'Поесть']<br>
      </td>
      <td align="center">
                        ['Сделать картинки']<br>
['Ответить на вопросы', 'Дописать конспект']<br>
                                          []<br>
      </td>
    </tr>
  </tbody>
</table>



## Примеры решений:
* Первый вариант решения
```python
class Todo:
    def __init__(self):
        self.things = []
        self.low_priority = 0
        self.high_priority = 0

    def add(self, name, n):
        self.things.append((name, n))
        self.low_priority = min(map(lambda y: y[1], self.things))
        self.high_priority = max(map(lambda y: y[1], self.things))


    def get_by_priority(self, n):
        return list(map(lambda y: y[0], filter(lambda x: x if n in x else [], self.things)))

    def get_low_priority(self):
        return list(map(lambda y: y[0], filter(lambda x: self.low_priority in x, self.things)))

    def get_high_priority(self):
        return list(map(lambda y: y[0], filter(lambda x: self.high_priority in x, self.things)))

```
* Второй вариант решения
```python
class Todo:
    def __init__(self):
        self.things = []

    def add(self, thing, priority):
        self.things.append((thing, priority))

    def get_by_priority(self, priority):
        return [t for t, p in self.things if p == priority]

    def get_low_priority(self):
        priority = min(map(lambda t: t[1], self.things)) if self.things else None
        return self.get_by_priority(priority)

    def get_high_priority(self):
        priority = max(map(lambda t: t[1], self.things)) if self.things else None
        return self.get_by_priority(priority)
```


