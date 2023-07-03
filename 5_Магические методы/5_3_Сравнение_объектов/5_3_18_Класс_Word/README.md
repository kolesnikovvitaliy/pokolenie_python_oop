<h2 style="text-align:center">Класс Word</h2>

### Будем называть словом любую последовательность из одной или более латинских букв.
### Реализуйте класс Word, описывающий слово. При создании экземпляра класс должен принимать один аргумент:
* word — слово
#### Экземпляр класса Word должен иметь следующее формальное строковое представление:
> Word('<слово в исходном виде>')
#### И следующее неформальное строковое представление:
> <слово, в котором первая буква заглавная, а все остальные строчные>
#### Также экземпляры класса Word должны поддерживать между собой все операции сравнения с помощью операторов ==, !=, >, <, >=, <=. Два слова считаются равными, если их длины совпадают. Слово считается больше другого слова, если его длина больше.
##### Примечание 1. Если объект, с которым выполняется операция сравнения, некорректен, метод, реализующий эту операцию, должен вернуть константу NotImplemented.
##### Примечание 3. Никаких ограничений касательно реализации класса Word нет, она может быть произвольной.

<table align="center">
  <tbody>
    <tr>
      <th>Sample Input 1: </th>
      <th>Sample Input 2: </th>
    </tr>
    <tr>
      <td align="center">print(Word('bee') == Word('hey'))<br>
                        print(Word('bee') < Word('geek'))<br>
                        print(Word('bee') > Word('geek'))<br>
                        print(Word('bee') <= Word('geek'))<br>
                        print(Word('bee') >= Word('gee'))<br></td>
      <td align="center">words = [Word('python'), Word('bee'), Word('geek')]<br>
                          print(sorted(words))<br>
                          print(min(words))<br>
                          print(max(words))<br></td>
    </tr>
    <tr>
      <td>Sample Output 1:</td>
      <td>Sample Output 2:</td>
      </tr>
    <tr>
      <td align="center">
                        True<br>
                        True<br>
                        False<br>
                        True<br>
                        True<br>
      </td>
      <td align="center">
                        [Word('bee'), Word('geek'), Word('python')]<br>
                        Bee<br>
                        Python<br>
      </td>
    </tr>
  </tbody>
</table>



## Примеры решений:
* Первый вариант решения
```python
from functools import total_ordering

@total_ordering
class Word:
    def __init__(self, text: str) -> None:
        self.words = text

    def __str__(self) -> str:
        return f'{self.words.capitalize()}'

    def __repr__(self) -> str:
        return f"{__class__.__name__}('{self.words}')"
    
    def __eq__(self, __value: object) -> bool:
        if isinstance(__value, Word):
            return len(self.words) == len(__value.words)
        return NotImplemented

    def __gt__(self, __value: object) -> bool:
        if isinstance(__value, Word):
            return len(self.words) > len(__value.words)
        return NotImplemented
```
* Второй вариант решения

```python
from functools import total_ordering
@total_ordering
class Word:
    def __init__(self, word: str):
        self.word = word

    def __repr__(self):
        return f"{type(self).__name__}('{self.word}')"

    def __str__(self):
        return self.word.title()

    def __eq__(self, other):
        if isinstance(other, Word):
            return len(self.word) == len(other.word)
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Word):
            return len(self.word) < len(other.word)
        return NotImplemented
```


