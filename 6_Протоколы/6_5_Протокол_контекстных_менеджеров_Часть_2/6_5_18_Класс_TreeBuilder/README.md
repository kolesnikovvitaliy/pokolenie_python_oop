<h2 style="text-align:center">Класс TreeBuilder</h2>

### Дерево — одна из наиболее широко распространённых структур данных в информатике, эмулирующая древовидную структуру в виде набора связанных узлов.

<div>
<img align="center" src="https://github.com/kolesnikovvitaliy/pokolenie_python_oop/blob/main/6_Протоколы/6_5_Протокол_контекстных_менеджеров_Часть_2/6_5_18_Класс_TreeBuilder/img/task.png" title="Git" **alt="Git">
​</div>

### Элементы дерева называются узлами. На рисунке выше узлами являются значения 8, 3, 1, 6, 4, 7, 10, 14 и 13. Узлы без потомков называются листьями. На рисунке выше листьями являются значения 1, 4, 7 и 13. 

### Реализуйте класс TreeBuilder. При создании экземпляра класс не должен принимать никаких аргументов.
#### Экземпляр класса TreeBuilder должен являться реентерабельным контекстным менеджером, который позволяет пошагово строить древовидную структуру данных (дерево).
#### Класс TreeBuilder должен иметь два метода экземпляра:
* add() — метод, принимающий в качестве аргумента произвольный объект (лист) и добавляющий его в текущий узел дерева
* structure() — метод, возвращающий структуру дерева в виде вложенных списков
#### Добавление узлов в дерево должно происходить с помощью оператора with. Узел считается текущим в рамках своего блока with. Если в узел не было добавлено ни одного листа, то этот узел не должен появляться в структуре дерева, возвращаемой методом structure().


##### Примечание 1. Структура дерева может быть произвольной, то есть узел может содержать другой узел, тот, в свою очередь, другой, и так далее.

##### Примечание 2. Гарантируется, что структура дерева не выводится внутри блоков with, то есть структура дерева выводится лишь после ее построения.

##### Примечание 3. Наглядные примеры использования класса TreeBuilder продемонстрированы в тестовых данных.

##### Примечание 4. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.

##### Примечание 5. Класс TreeBuilder должен удовлетворять протоколу контекстного менеджера, то есть иметь методы __enter__() и __exit__(). Реализация же протокола может быть произвольной.

<table align="center">
  <tbody>
    <tr>
      <th>Sample Input 1: </th>
      <th>Sample Input 2: </th>
      <th>Sample Input 2: </th>
    </tr>
    <tr>
      <td align="center">tree = TreeBuilder()<br>
                        print(tree.structure())<br>
                        tree.add('1st')<br>
                        print(tree.structure())<br>
                        with tree:<br>
                            tree.add('2nd')<br>
                            with tree:<br>
                                tree.add('3rd')<br>
                            tree.add('4th')<br>
                            with tree:<br>
                                pass<br>
                        print(tree.structure())<br></td>
      <td align="center">tree = TreeBuilder()<br>
                        tree.add('1st')<br>
                        with tree:<br>
                            tree.add('2nd')<br>
                            with tree:<br>
                                tree.add('3rd')<br>
                                with tree:<br>
                                    tree.add('4th')<br>
                                    with tree:<br>
                                        tree.add('5th')<br>
                            with tree:<br>
                                pass<br>
                        tree.add('6th')<br>
                        print(tree.structure())<br></td>
      <td align="center">tree = TreeBuilder()<br>
                          with tree:<br>
                              tree.add(1)<br>
                              tree.add(2)<br>
                              with tree:<br>
                                  tree.add(3)<br>
                                  with tree:<br>
                                      tree.add(4)<br>
                              with tree:<br>
                                  tree.add(5)<br>
                          print(tree.structure())<br></td>
    </tr>
    <tr>
      <td>Sample Output 1:</td>
      <td>Sample Output 2:</td>
      <td>Sample Output 2:</td>
      </tr>
    <tr>
      <td align="center">
                        []<br>
                        ['1st']<br>
                        ['1st', ['2nd', ['3rd'], '4th']]<br>
      </td>
      <td align="center">
                        ['1st', ['2nd', ['3rd', ['4th', ['5th']]]], '6th']<br>
      </td>
      <td align="center">
                        [[1, 2, [3, [4]], [5]]]<br>
      </td>
    </tr>
  </tbody>
</table>



## Примеры решений:
* Первый вариант решения
```python
class TreeBuilder:
    def __init__(self):
        ''' '''
        self.index = 0
        self._structure = {0: []}

    def __enter__(self):
        self.index += 1
        self._structure[self.index] = []
        return self

    def add(self, obj):
        self._structure.setdefault(self.index, []).append(obj)

    def __exit__(self, exc_type, exc_val, exc_tb):
        last = max(self._structure.keys())
        if self._structure[last]:
            self._structure[last-1].append(self._structure.pop(last))
        else:
            self._structure.pop(last)
        self.index -= 1

    def structure(self):
        return self._structure[0]
```
* Второй вариант решения

```python
class TreeBuilder:
    def __init__(self):
        self.knots = [[]]
        
    def __enter__(self):
        self.knots.append([])
        
    def __exit__(self, *args, **kwargs):
        if self.knots[-1]:
            self.knots[-2].append(self.knots[-1])
        self.knots.pop()
    
    def add(self, value):
        self.knots[-1].append(value)
        
    def structure(self):
        return self.knots[-1]
```


