<h2 style="text-align:center">Класс SuperInt</h2>


### Реализуйте класс SuperInt, наследника класса int, описывающий целое число с дополнительным функционалом. Процесс создания экземпляра класса SuperInt должен совпадать с процессом создания экземпляра класса int.
#### Класс SuperInt должен иметь четыре метода экземпляра:
* repeat() — метод, принимающий в качестве аргумента целое число n, по умолчанию равное 2, и возвращающий экземпляр класса SuperInt, продублированный n раз
* to_bin() — метод, возвращающий двоичное представление экземпляра класса SuperInt. Двоичное представление может быть как в виде экземпляра класса str, так и int
* next() — метод, возвращающий новый экземпляр класса SuperInt, который больше текущего на единицу
* prev() — метод, возвращающий новый экземпляр класса SuperInt, который меньше текущего на единицу
#### Также экземпляр класса SuperInt должен быть итерируемым объектом, элементами которого являются его цифры слева направо. Сами цифры так же должны быть представлены в виде экземпляров класса SuperInt.
##### Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.
##### Примечание 2. Никаких ограничений касательно реализации класса SuperInt нет, она может быть произвольной.

<table align="center">
  <tbody>
    <tr>
      <th>Sample Input 1: </th>
      <th>Sample Input 2: </th>
      <th>Sample Input 3: </th>
      <th>Sample Input 4: </th>
    </tr>
    <tr>
      <td align="center">superint1 = SuperInt(17)<br>
                          superint2 = SuperInt(-17)<br>
                          print(superint1.repeat())<br>
                          print(superint2.repeat(3))<br></td>
      <td align="center">superint1 = SuperInt(17)<br>
                          superint2 = SuperInt(-17)<br>
                          print(superint1.to_bin())<br>
                          print(superint2.to_bin())<br></td>
      <td align="center">superint = SuperInt(17)<br>
                          print(superint.prev())<br>
                          print(superint.next())<br></td>
      <td align="center">superint1 = SuperInt(1337)<br>
                          superint2 = SuperInt(-2077)<br>
                          print(*superint1)<br>
                          print(*superint2)<br></td>
    </tr>
    <tr>
      <td>Sample Output 1:</td>
      <td>Sample Output 2:</td>
      <td>Sample Output 3:</td>
      <td>Sample Output 4:</td>
      </tr>
    <tr>
      <td align="center">
                        1717<br>
                        -171717<br>
      </td>
      <td align="center">
                        10001<br>
                        -10001<br>
      </td>
      <td align="center">
                        16<br>
                        18<br>
      </td>
      <td align="center">
                        1 3 3 7<br>
                        2 0 7 7<br>
      </td>
    </tr>
  </tbody>
</table>



## Примеры решений:
* Первый вариант решения
```python
class SuperInt(int):
    def repeat(self, n=2):
        if self > 0:
            return SuperInt(str(self) * n)
        return -SuperInt(str(self)[1:] * n)

    def to_bin(self):
        if self > 0:
            return SuperInt(str(bin(self))[2:])
        return -SuperInt(str(bin(int(str(self)[1:])))[2:])

    def __iter__(self):
        if self > 0:
            yield from [SuperInt(i) for i in str(self)]
        else:
            yield from [SuperInt(i) for i in str(self)[1:]]

    def next(self):
        return SuperInt(self+1)

    def prev(self):
        return SuperInt(self-1)
```
* Второй вариант решения

```python
class SuperInt(int):

    def repeat(self, n=2):
        return SuperInt(str(self) * n)

    def to_bin(self):
        return format(self, 'b')

    def next(self):
        return SuperInt(self + 1)

    def prev(self):
        return SuperInt(self - 1)

    def __iter__(self):
        yield from map(SuperInt, str(self).lstrip('-'))
```


