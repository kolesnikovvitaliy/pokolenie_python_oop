<h2 style="text-align:center">Классы LeftParagraph и RightParagraph</h2>

### Будем называть словом любую последовательность из одной или более латинских букв.

### 1. Реализуйте класс LeftParagraph, описывающий абзац, выровненный по левому краю. При создании экземпляра класс должен принимать один аргумент:

* length — длина строки абзаца
#### Класс LeftParagraph должен иметь два метода экземпляра:

* add() — метод, принимающий в качестве аргумента слово или несколько слов, разделенных пробелом, и добавляющий их в текущий абзац. Если слово не помещается на текущей строке, оно переносится на следующую. Также метод должен автоматически добавлять один пробел после каждого добавленного слова (кроме последнего)
* end() — метод, печатающий текущий абзац, выровненный по левому краю. После вызова метода текущий абзац считается пустым, то есть начинается формирование нового
### 2. Также реализуйте класс RightParagraph, описывающий абзац, выровненный по правому краю. При создании экземпляра класс должен принимать один аргумент:

* length — длина строки абзаца
#### Класс RightParagraph должен иметь два метода экземпляра:

* add() — метод, принимающий в качестве аргумента слово или несколько слов, разделенных пробелом, и добавляющий их в текущий абзац. Если слово не помещается на текущей строке, оно переносится на следующую. Также метод должен автоматически добавлять один пробел после каждого добавленного слова (кроме последнего)
* end() — метод, печатающий текущий абзац, выровненный по правому краю с учетом длины строки. После вызова метода текущий абзац считается пустым, то есть начинается формирование нового

#### Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованные классы используются только с корректными данными.

#### Примечание 2. Никаких ограничений касательно реализаций классов нет, они могут быть произвольными.

<table align="center">
  <tbody>
    <tr>
      <th>Sample Input 1: </th>
      <th>Sample Input 2: </th>
    </tr>
    <tr>
      <td align="center">leftparagraph = LeftParagraph(10)<br>
                          leftparagraph.add('death')<br>
                          leftparagraph.add('can have me')<br>
                          leftparagraph.add('when it earns me')<br>
                          leftparagraph.end()<br></td>
      <td align="center">rightparagraph = RightParagraph(10)<br>
                          rightparagraph.add('death')<br>
                          rightparagraph.add('can have me')<br>
                          rightparagraph.add('when it earns me')<br>
                          rightparagraph.end()<br></td>
    </tr>
    <tr>
      <td>Sample Output 1:</td>
      <td>Sample Output 2:</td>
      </tr>
    <tr>
      <td align="center">
                        death can<br>
                        have me<br>
                        when it<br>
                        earns me<br>
      </td>
      <td align="center">
                        death can<br>
                        have me<br>
                        when it<br>
                        earns me<br>
      </td>
    </tr>
  </tbody>
</table>



## Примеры решений:
* Первый вариант решения
```python
from abc import abstractmethod


class LeftParagraph:
    def __init__(self, length):
        self.length = length
        self.string = []

    def add(self, text):
        self.string.extend(text.split())

    def end(self):
        _lst = ['']
        while len(self.string) > 0:
            if len(_lst[-1] + self.string[0] + '\n') <= self.length:
                _lst.append(_lst[-1].strip() + ' ' + self.string[0])
                del _lst[-2]
                self.string = self.string[1:]
            else:
                _lst.append('\n')
        return self.print_text(_lst)

    @abstractmethod
    def print_text(self, data):
        for i in data:
            print(''.join(i).strip())


class RightParagraph(LeftParagraph):
    def print_text(self, data):
        for i in data:
            i = ' '*(self.length - len(i)) + i
            print(''.join(i))
```
* Второй вариант решения

```python
from abc import ABC, abstractmethod


class Paragraph(ABC):
    def __init__(self, length):
        self._size = length
        self._paragraph = ['']

    def add(self, words):
        words = words.split()
        for word in words:
            if len(self._paragraph[-1] + f' {word}') > self._size:
                self._paragraph.append('')
            self._paragraph[-1] = (self._paragraph[-1] + f' {word}').lstrip()

    @abstractmethod
    def end(self):
        pass


class LeftParagraph(Paragraph):
    def end(self):
        for line in self._paragraph:
            print(line)
        self._paragraph = ['']


class RightParagraph(Paragraph):
    def end(self):
        for line in self._paragraph:
            print(line.rjust(self._size))
        self._paragraph = ['']
```


