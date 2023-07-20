<h2 style="text-align:center">Класс Grouper</h2>

### Нередко нам приходится группировать объекты по определенному признаку. Например, строки можно сгруппировать по их длине или первому символу. Реализуйте класс Grouper, описывающий объект, который группирует элементы некоторого итерируемого объекта на основе ключевой функции. При создании экземпляра класс должен принимать два аргумента в следующем порядке:
* iterable — итерируемый объект
* key — ключевая функция
### Элементы попадают в одну группу, если при их передаче в ключевую функцию она возвращает один и тот же результат.  Например, elem1 и elem2 попадают в одну группу, если key(elem1) == key(elem2). Значение key(elem1) будем называть ключом группы, а elem1 и elem2 — элементами группы по этому ключу.
#### Класс Grouper должен иметь два метода экземпляра:
* add() — метод, принимающий в качестве аргумента произвольный объект и добавляющий его в нужную группу экземпляра класса Grouper
* group_for() — метод, принимающий в качестве аргумента произвольный объект, определяющий, в какую группу экземпляра класса Grouper попадет этот объект, и возвращающий ключ этой группы
#### Класс Rectangle должен иметь два свойства:
* perimeter — свойство, доступное только для чтения, возвращающее периметр прямоугольника
* area — свойство, доступное только для чтения, возвращающее площадь прямоугольника
#### При передаче экземпляра класса Grouper в функцию len() должно возвращаться количество групп в нем.
#### Помимо этого, экземпляр класса Grouper должен быть итерируемым объектом, то есть позволять перебирать свои группы, например, с помощью цикла for. В данном случае группа — это кортеж, первым элементом которого является ключ группы, вторым — список элементов группы. Группы при итерировании могут располагаться в произвольном порядке.
#### Также экземпляр класса Grouper должен поддерживать операцию проверки на принадлежность с помощью оператора in, в которой проверяется наличие в экземпляре класса Grouper группы с искомым ключом.
#### Наконец, экземпляр класса Grouper должен позволять получать элементы группы по ключу. В данном случае элементы группы должны быть представлены в виде списка, при этом элементы в списке должны располагаться в том порядке, в котором они были добавлены.
##### Примечание 1. Экземпляр класса Grouper не должен зависеть от итерируемого объекта, на основе которого он был создан. Другими словами, если исходный итерируемый объект изменится, то экземпляр класса Grouper измениться  не должен.
##### Примечание 2. Реализация класса Grouper может быть произвольной, то есть требований к наличию определенных атрибутов нет.
##### Примечание 3. Дополнительная проверка данных на корректность в методах не требуется. Гарантируется, что реализованный класс используется только с корректными данными.

<table align="center">
  <tbody>
    <tr>
      <th>Sample Input 1: </th>
      <th>Sample Input 2: </th>
      <th>Sample Input 3: </th>
      <th>Sample Input 4: </th>
    </tr>
    <tr>
      <td align="center">grouper = Grouper(['bee', 'geek', 'one', 'two', 'five', 'hi'], key=len)<br>
                          print(grouper[2])<br>
                          print(grouper[3])<br>
                          print(grouper[4])<br></td>
      <td align="center">grouper = Grouper(['bee', 'geek', 'one', 'two', 'five', 'hi'], key=len)<br>
                          print(3 in grouper)<br>
                          print('bee' in grouper)<br></td>
      <td align="center">grouper = Grouper(['hi'], key=lambda s: s[0])<br>
                        print(len(grouper))<br>
                        grouper.add('hello')<br>
                        grouper.add('bee')<br>
                        grouper.add('big')<br>
                        print(len(grouper))<br>
                        grouper.add('geek')<br>
                        print(grouper['h'])<br>
                        print(grouper['b'])<br>
                        print(grouper['g'])<br>
                        print(len(grouper))<br></td>
      <td align="center">grouper = Grouper(['hi'], key=lambda s: s[0])<br>
                        print(grouper.group_for('hello'))<br>
                        print(grouper.group_for('bee'))<br>
                        print(grouper['h'])<br>
                        print('b' in grouper)<br></td>
    </tr>
    <tr>
      <td>Sample Output 1:</td>
      <td>Sample Output 2:</td>
      <td>Sample Output 3:</td>
      <td>Sample Output 4:</td>
      </tr>
    <tr>
      <td align="center">
                        ['hi']<br>
                        ['bee', 'one', 'two']<br>
                        ['geek', 'five']<br>
      </td>
      <td align="center">
                        True<br>
                        False<br>
      </td>
      <td align="center">
                        1<br>
                        2<br>
                        ['hi', 'hello']<br>
                        ['bee', 'big']<br>
                        ['geek']<br>
                        3<br>
      </td>
      <td align="center">
                        h<br>
                        b<br>
                        ['hi']<br>
                        False<br>
      </td>
    </tr>
  </tbody>
</table>



## Примеры решений:
* Первый вариант решения
```python
class Grouper:
    def __init__(self, iterable, key):
        self._func = key
        self._dict = dict()
        {self.add(item) for item in iterable}

    def add(self, item):
        if self._func(item) in self._dict:
            self._dict[self._func(item)].append(item)
        else:
            self._dict.setdefault(self._func(item),[]).append(item)
    
    def group_for(self, item):
        return self._func(item)
    
    def __len__(self):
        return len(self._dict)
    
    def __iter__(self):
        yield from self._dict.items()

    def __contains__(self, item):
        return item in self._dict
    
    def __getitem__(self, key):
        return self._dict[key]
```
* Второй вариант решения

```python
class Grouper:
    def __init__(self, iterable, key):
        self._iterable = list(iterable)
        self._key = key
        self._make_groups(self._iterable)

    def _make_groups(self, iterable):
        self._groups = {}
        for item in iterable:
            self.add(item)

    def add(self, item):
        self._groups.setdefault(self._key(item), []).append(item)

    def group_for(self, item):
        return self._key(item)

    def __len__(self):
        return len(self._groups)

    def __iter__(self):
        return iter(self._groups.items())

    def __contains__(self, item):
        return item in self._groups

    def __getitem__(self, key):
        return self._groups[key]
```


