<h2 style="text-align:center">Класс DNA</h2>

### ДНК состоит из двух цепей, ориентированных азотистыми основаниями друг к другу. В ДНК встречается четыре вида азотистых оснований: аденин (A), гуанин (G), тимин (T) и цитозин (C). Азотистые основания одной из цепей соединены с азотистыми основаниями другой цепи водородными связями согласно принципу комплементарности: аденин (A) соединяется только с тимином (T), гуанин (G) — только с цитозином (C).

<div>
<img align="center" src="https://github.com/kolesnikovvitaliy/pokolenie_python_oop/blob/main/7_Наследование_и_полиморфизм/7_5_Абстрактные_классы_модуль_abc/7_5_25_Класс_DNA/img/task.png" title="Git" **alt="Git">
​</div>

### Реализуйте класс DNA, описывающий двухцепочную спираль ДНК. При создании экземпляра класс должен принимать один аргумент:
* chain — первая цепь ДНК, представляющая собой строку из символов A, G, T и C (азотистых оснований)
#### Экземпляр класса DNA должен иметь следующее неформальное строковое представление:
> <азотистые основания первой цепи ДНК>
#### При передаче экземпляра класса DNA в функцию len() должно возвращаться количество азотистых оснований в одной из его цепей. При передаче экземпляра класса в функцию reversed() должен возвращаться итератор, элементами которого являются элементы переданного экземпляра класса DNA, расположенные в обратном порядке.
#### Помимо этого, экземпляр класса DNA должен быть итерируемым объектом, то есть позволять перебирать свои элементы, например, с помощью цикла for.
#### Также экземпляр класса DNA должен позволять получать значения своих элементов с помощью индексов, причем как положительных, так и отрицательных.
#### В случае с функцией reversed(), итерацией и доступу по индексам элементы экземпляра класса DNA должны быть представлены в виде кортежей из двух элементов, первым из которых является основание первой цепи ДНК по указанному индексу, вторым — азотистое основание второй цепи ДНК по указанному индексу. Азотистое основание второй цепи ДНК можно получить при помощи принципа комплементарности.
#### Вдобавок ко всему, экземпляр класса DNA должен поддерживать операцию проверки на принадлежность с помощью оператора in. В данном случае должно проверяться, входит ли азотистое основание в первую цепь ДНК.
#### Экземпляры класса DNA должны поддерживать между собой операции сравнения с помощью операторов == и!=. Две ДНК считаются равными, если их первые цепи совпадают.
#### Наконец, экземпляры класса DNA должны поддерживать между собой операцию сложения с помощью оператора +, результатом которой должен являться новый экземпляр класса DNA, первой цепью которого является конкатенация первых цепей исходных экземпляров класса DNA.

##### Примечание 1. Перед решением подумайте, какой абстрактный класс из модуля collections.abc будет удобен в качестве родительского.
##### Примечание 2. Если объект, с которым выполняется операция сравнения или сложения, некорректен, метод, реализующий эту операцию, должен вернуть константу NotImplemented.
##### Примечание 3. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.
##### Примечание 4. Никаких ограничений касательно реализации класса DNA нет, она может быть произвольной.

<table align="center">
  <tbody>
    <tr>
      <th>Sample Input 1: </th>
      <th>Sample Input 2: </th>
      <th>Sample Input 3: </th>
      <th>Sample Input 4: </th>
    </tr>
    <tr>
      <td align="center">dna = DNA('AGTC')<br>
                        print(dna[0])<br>
                        print(dna[1])<br>
                        print(dna[2])<br>
                        print(dna[3])<br>
                        print(dna[-1])<br>
                        print(dna[-2])<br></td>
      <td align="center">dna = DNA('AGT')<br>
                        print(dna)<br>
                        print(len(dna))<br>
                        print('A' in dna)<br>
                        print('C' in dna)<br></td>
      <td align="center">dna1 = DNA('ACG')<br>
                        dna2 = DNA('TTTAAT')<br>
                        dna3 = dna1 + dna2<br>
                        dna4 = dna2 + dna1<br>
                        print(dna3, type(dna3))<br>
                        print(dna4, type(dna4))<br></td>
      <td align="center">dna1 = DNA('ACG')<br>
                          dna2 = DNA('TTTAAT')<br>
                          dna3 = DNA('TTTAAT')<br>
                          print(dna1 == dna2)<br>
                          print(dna2 == dna3)<br>
                          print(dna1 != dna3)<br>
                          print(dna2 != dna3)<br></td>
    </tr>
    <tr>
      <td>Sample Output 1:</td>
      <td>Sample Output 2:</td>
      <td>Sample Output 3:</td>
      <td>Sample Output 4:</td>
      </tr>
    <tr>
      <td align="center">
                        ('A', 'T')<br>
                        ('G', 'C')<br>
                        ('T', 'A')<br>
                        ('C', 'G')<br>
                        ('C', 'G')<br>
                        ('T', 'A')<br>
      </td>
      <td align="center">
                        AGT<br>
                        3<br>
                        True<br>
                        False<br>
      </td>
      <td align="center">
                        ACGTTTAAT class '__main__.DNA'<br>
                        TTTAATACG class '__main__.DNA'<br>
      </td>
      <td align="center">
                        False<br>
                        True<br>
                        True<br>
                        False<br>
      </td>
    </tr>
  </tbody>
</table>



## Примеры решений:
* Первый вариант решения
```python
from collections.abc import Sequence


class DNA(Sequence):
    def __init__(self, chain):
        self.dna = chain
        self._lst = self.combinations(chain)

    @staticmethod
    def combinations(data):
        __lst = []
        for i in data:
            if i == 'A':
                __lst.append(('A', 'T'))
            if i == 'G':
                __lst.append(('G', 'C'))
            if i == 'T':
                __lst.append(('T', 'A'))
            if i == 'C':
                __lst.append(('C', 'G'))
        return __lst

    def __str__(self):
        return ''.join(self.dna)

    def __getitem__(self, index):
        return self._lst[index]

    def __len__(self):
        return len(self.dna)

    def __reversed__(self):
        a = [i for i in reversed(self.dna)]
        return __class__(a)

    def __contains__(self, value):
        return value in self.dna

    def __eq__(self, __value):
        if isinstance(__value, __class__):
            return self._lst[0] == __value._lst[0]
        return NotImplemented

    def __ne__(self, __value):
        if isinstance(__value, __class__):
            return self._lst[0] != __value._lst[0]
        return NotImplemented

    def __add__(self, obj):
        if isinstance(obj, __class__):
            return __class__(f'{self.dna}{obj.dna}')
        return NotImplemented
```
* Второй вариант решения

```python
from collections.abc import Sequence


class DNA(Sequence):
    __BASE = {'A': 'T', 'G': 'C', 'T': 'A', 'C': 'G'}

    def __init__(self, chain):
        self._chain = chain

    def __str__(self):
        return self._chain

    def __len__(self):
        return len(self._chain)

    def __getitem__(self, index):
        if isinstance(index, (int, slice)):
            return self._chain[index], type(self).__BASE[self._chain[index]]
        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, type(self)):
            return self._chain == other._chain
        return NotImplemented

    def __add__(self, other):
        if isinstance(other, type(self)):
            return type(self)(self._chain + other._chain)
        return NotImplemented

    def __contains__(self, item):
        return item in self._chain
```


