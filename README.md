# Конспект:
##  Курс поколение Python : ООП на Stepik  
### В этом репозитории я документирую этапы прохождения кура и решаемые мной задачи.
## Курс состоит из 7 разделов:
1. <a href="https://github.com/kolesnikovvitaliy/pokolenie_python_oop/tree/main/2_Повторяем_основные_конструкции_языка">Повторяем основные конструкции языка Python</a>
2. <a href="https://github.com/kolesnikovvitaliy/pokolenie_python_oop/tree/main/4_Атрибуты_свойства_и_методы">Атрибуты, свойства и методы</a>
3. <a href="https://github.com/kolesnikovvitaliy/pokolenie_python_oop/tree/main/5_Магические методы">Магические методы</a>
4. <a href="https://github.com/kolesnikovvitaliy/pokolenie_python_oop/tree/main/6_Протоколы">Протоколы</a>
5. <a href="https://github.com/kolesnikovvitaliy/pokolenie_python_oop/tree/main/7_Наследование_и_полиморфизм">Наследование и полиморфизм</a>
6. <a href="https://github.com/kolesnikovvitaliy/pokolenie_python_oop/tree/main/8_Дополнительные_возможности">Дополнительные возможности</a>
7. <a href="https://github.com/kolesnikovvitaliy/pokolenie_python_oop/tree/main/9_Задачи_на_проектирование_классов">Задачи на проектирование классов</a>
8. <a href="https://github.com/kolesnikovvitaliy/pokolenie_python_oop/tree/main/10_Сертификат">Сертификат 100%</a>

#### Для скачивания репозитория вам потребуется:
1. Создать каталог для скачивания:
   ```bash
   mkdir course_oop
    ```
2. Перейти в каталог course_oop:
   ```bash
   cd course_oop
    ```
3. Клонировать репозиторий себе на локальный компьютер:
   ```bash
   git clone https://github.com/kolesnikovvitaliy/pokolenie_python_oop.git
    ```
4. Перейти в каталог pokolenie_python_oop:
   ```bash
   cd pokolenie_python_oop
    ```
# ПРИМЕРЫ РЕШЕННЫХ ЗАДАЧЬ:
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
#

<h2 style="text-align:center">Класс MultiKeyDict</h2>

### Реализуйте класс MultiKeyDict, который практически во всем повторяет класс dict. Создание экземпляра класса MultiKeyDict должно происходить аналогично созданию экземпляра класса dict:

```python 
multikeydict1 = MultiKeyDict(x=1, y=2, z=3)
multikeydict2 = MultiKeyDict([('x', 1), ('y', 2), ('z', 3)])

print(multikeydict1['x'])        # 1
print(multikeydict2['z'])        # 3
```
#### Особенностью класса MultiKeyDict должен являться метод alias(), который должен позволять давать имеющимся ключам псевдонимы. Обращение по созданному псевдониму не должно ничем отличаться от обращения по оригинальному ключу, то есть с момента создания псевдонима у значения становится два ключа (или больше, если псевдонимов несколько):
```python 
multikeydict = MultiKeyDict(x=100, y=[10, 20])

multikeydict.alias('x', 'z')     # добавление ключу 'x' псевдонима 'z'
multikeydict.alias('x', 't')     # добавление ключу 'x' псевдонима 't'
print(multikeydict['z'])         # 100
multikeydict['t'] += 1
print(multikeydict['x'])         # 101

multikeydict.alias('y', 'z')     # теперь 'z' становится псевдонимом ключа 'y'
multikeydict['z'] += [30]
print(multikeydict['y'])         # [10, 20, 30]
```
#### Значение должно оставаться доступным по псевдониму даже в том случае, если оригинальный ключ был удален:
```python 
multikeydict = MultiKeyDict(x=100)

multikeydict.alias('x', 'z')
del multikeydict['x']
print(multikeydict['z'])         # 100
```
#### Ключи должны иметь приоритет над псевдонимами. Если некоторые ключ и псевдоним совпадают, то все операции при обращении к ним должны выполняться именно с ключом:
```python 
multikeydict = MultiKeyDict(x=100, y=[10, 20])

multikeydict.alias('x', 'y')
print(multikeydict['y'])         # [10, 20]
```

<table align="center">
  <tbody>
    <tr>
      <th>Sample Input 1: </th>
      <th>Sample Input 2: </th>
      <th>Sample Input 3: </th>
      <th>Sample Input 4: </th>
    </tr>
    <tr>
      <td align="center">multikeydict = MultiKeyDict(x=100, y=[10, 20])<br>
                        multikeydict.alias('x', 'z')<br>
                        multikeydict.alias('x', 't')<br>
                        print(multikeydict['z'])<br>
                        multikeydict['t'] += 1<br>
                        print(multikeydict['x'])<br>
                        multikeydict.alias('y', 'z')<br>
                        multikeydict['z'] += [30]<br>
                        print(multikeydict['y'])<br></td>
      <td align="center">multikeydict = MultiKeyDict(x=100)<br>
                        multikeydict.alias('x', 'z')<br>
                        del multikeydict['x']<br>
                        print(multikeydict['z'])<br>
                        try:<br>
                            print(multikeydict['x'])<br>
                        except KeyError:<br>
                            print('Ключ отстутствует')<br></td>
      <td align="center">multikeydict = MultiKeyDict(x=100, y=[10, 20])<br>
                          multikeydict.alias('x', 'y')<br>
                          print(multikeydict['y'])<br>
                          multikeydict['y'] += [30]<br>
                          print(multikeydict['y'])<br></td>
      <td align="center">multikeydict = MultiKeyDict(lecture='python', lesson='object oriented programming')<br>
                          multikeydict.alias('lecture', 'lesson')<br>
                          print(multikeydict['lesson'])<br>
                          multikeydict.alias('lecture', 'lesson')<br>
                          print(multikeydict['lesson'])<br>
                          del multikeydict['lesson']<br>
                          print(multikeydict['lesson'])<br></td>
    </tr>
    <tr>
      <td>Sample Output 1:</td>
      <td>Sample Output 2:</td>
      <td>Sample Output 3:</td>
      <td>Sample Output 4:</td>
      </tr>
    <tr>
      <td align="center">
                        100<br>
                        101<br>
                        [10, 20, 30]<br>
      </td>
      <td align="center">
                        100<br>
                        Ключ отстутствует<br>
      </td>
      <td align="center">
                        [10, 20]<br>
                        [10, 20, 30]<br>
      </td>
      <td align="center">
                        object oriented programming<br>
                        object oriented programming<br>
                        python<br>
      </td>
    </tr>
  </tbody>
</table>



## Примеры решений:
* Первый вариант решения
```python
from collections import UserDict


class MultiKeyDict(UserDict):
    def __init__(self, *args, **kwargs):
        self._key = {}
        super().__init__(*args, **kwargs)
        self._key = {k: k for k in self.data.keys()}

    def alias(self, key, alias):
        if alias not in self.data:
            self._key[alias] = key

    def __getitem__(self, __key):
        if __key in self._key:
            return super().__getitem__(self._key[__key])
        return super().__getitem__(__key)

    def __setitem__(self, __key, __value):
        if __key in self._key:
            self.data[self._key[__key]] = __value
        else:
            self.data[__key] = __value

    def __delitem__(self, __key):
        new_key = [i for i in self._key.keys() if i != __key][0]
        if new_key not in self.data:
            del self._key[__key]
            self._key[new_key] = new_key
            self.data[new_key] = self.data.pop(__key)
            if __key in self._key.values():
                key_2 = [k for k, v in self._key.items() if v == __key][0]
                self._key[key_2] = new_key
        else:
            self.data[__key] = self.data.pop(self._key[__key])
            self._key[__key] = new_key
            del self._key[new_key]
            del self.data[__key]
```
* Второй вариант решения

```python
from collections import UserDict


class MultiKeyDict(UserDict):
    def __init__(self, *args, **kwargs):
        self._aliases = {}
        super().__init__(*args, **kwargs)

    def alias(self, key, alias):
        self._aliases[alias] = key

    def __getitem__(self, key):
        return self.data.get(key) or self.data.get(self._aliases[key])

    def __setitem__(self, key, value):
        if key in self.data or key not in self._aliases:
            self.data[key] = value
        else:
            self.data[self._aliases[key]] = value

    def __delitem__(self, del_key):
        for alias_key, key in self._aliases.items():
            if key == del_key:
                self.data[alias_key] = self.data[del_key]
        del self.data[del_key]

```

#

<h2 style="text-align:center">Декоратор @predicate</h2>

### Предикат — это функция, которая возвращает True или False в зависимости от переданных аргументов.

### Реализуйте декоратор @predicate, который будет позволять удобно комбинировать предикаты с помощью операторов &, | и ~:
```python
@predicate
def is_even(num):
    return num % 2 == 0

@predicate
def is_positive(num):
    return num > 0

print((is_even & is_positive)(4))             # True; равнозначно is_even(4) and is_positive(4)
print((is_even & is_positive)(3))             # False; равнозначно is_even(3) and is_positive(3)
print((is_even | is_positive)(3))             # True; равнозначно is_even(3) or is_positive(3)
print((~is_even & is_positive)(3))            # True; равнозначно not is_even(3) and is_positive(3)
```
#### Декоратор должен уметь работать с любыми предикатами, независимо от того, сколько аргументов они принимают:
```python
@predicate
def to_be():
    return True

print((to_be | ~to_be)())                     # True; равнозначно to_be() or not to_be()

@predicate
def is_equal(a, b):
    return a == b

@predicate
def is_less_than(a, b):
    return a < b

print((is_less_than | is_equal)(1, 2))        # True; равнозначно is_less_than(1, 2) or is_equal(1, 2)
```
#### Также должны поддерживаться как позиционные аргументы, так и именованные:
```python
print((is_less_than | is_equal)(2, b=2))      # True; равнозначно is_less_than(2, b=2) or is_equal(2, b=2)
print((is_less_than | is_equal)(a=3, b=2))    # False; равнозначно is_less_than(a=3, b=2) or is_equal(a=3, b=2)
```
#### Задекорированная функция должна быть доступна вне комбинаций с другими функциями и вести себя как исходная функция:
```python
@predicate
def is_less_than(a, b):
    return a < b

print(is_less_than(1, 2))                     # True
print(is_less_than(2, 2))                     # False
print(is_less_than(3, 2))                     # False
```
#### Примечание 1. Гарантируется, что комбинируемые функции имеют одинаковые сигнатуры. 

<table align="center">
  <tbody>
    <tr>
      <th>Sample Input 1: </th>
      <th>Sample Input 2: </th>
    </tr>
    <tr>
      <td align="center">@predicate<br>
                            def to_be():<br>
                                return True<br>
                            print((to_be | ~to_be)())                     # True; равнозначно to_be() or not to_be()<br>
                            @predicate<br>
                            def is_equal(a, b):<br>
                                return a == b<br>
                            @predicate<br>
                            def is_less_than(a, b):<br>
                                return a < b<br>
                            print((is_less_than | is_equal)(1, 2))        # True; равнозначно is_less_than(1, 2) or is_equal(1, 2)<br>
                            print((is_less_than | is_equal)(2, b=2))      # True; равнозначно is_less_than(2, b=2) or is_equal(2, b=2)<br>
                            print((is_less_than | is_equal)(a=3, b=2))    # False; равнозначно is_less_than(a=3, b=2) or is_equal(a=3, b=2)<br></td>
      <td align="center">@predicate<br>
                          def is_even(num):<br>
                              return num % 2 == 0<br>
                          @predicate<br>
                          def is_positive(num):<br>
                              return num > 0<br>
                          print((is_even & is_positive)(4))             # True; равнозначно is_even(4) and is_positive(4)<br>
                          print((is_even & is_positive)(3))             # False; равнозначно is_even(3) and is_positive(3)<br>
                          print((is_even | is_positive)(3))             # True; равнозначно is_even(3) or is_positive(3)<br>
                          print((~is_even & is_positive)(3))            # True; равнозначно not is_even(4) and is_positive(4)<br></td>
    </tr>
    <tr>
      <td>Sample Output 1:</td>
      <td>Sample Output 2:</td>
      </tr>
    <tr>
      <td align="center">
                        True<br>
                        True<br>
                        True<br>
                        False<br>
      </td>
      <td align="center">
                        True<br>
                        False<br>
                        True<br>
                        True<br>
      </td>
    </tr>
  </tbody>
</table>



## Примеры решений:
* Первый вариант решения
```python
class Predicate:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        return self.func(*args, **kwargs)

    def __invert__(self):
        def invert_func(*args, **kwargs):
            return not self(*args, **kwargs)
        return __class__(invert_func)

    def __and__(self, other):
        def and_func(*args, **kwargs):
            return self(*args, **kwargs) and other(*args, **kwargs)
        return __class__(and_func)

    def __or__(self, other):
        def or_func(*args, **kwargs):
            return self(*args, **kwargs) or other(*args, **kwargs)
        return __class__(or_func)


def predicate(func):
    return Predicate(func)
```
* Второй вариант решения

```python
class predicate:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        return self.func(*args, **kwargs)

    def __invert__(self):
        def not_func(*args, **kwargs):
            return not self.func(*args, **kwargs)

        return type(self)(not_func)

    def __or__(self, other):
        def or_func(*args, **kwargs):
            return self.func(*args, **kwargs) or other.func(*args, **kwargs)

        return type(self)(or_func)

    def __and__(self, other):
        def and_func(*args, **kwargs):
            return self.func(*args, **kwargs) and other.func(*args, **kwargs)

        return type(self)(and_func)
```

