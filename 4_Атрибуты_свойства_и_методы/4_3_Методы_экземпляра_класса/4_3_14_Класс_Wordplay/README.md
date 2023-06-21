<h2 style="text-align:center">Класс Wordplay</h2>

### Будем называть словом любую последовательность из одной или более латинских букв.
### Реализуйте класс Wordplay, описывающий расширяемый набор слов. При создании экземпляра класс должен принимать один аргумент:
* words — список, определяющий начальный набор слов. Если не передан, начальный набор слов считается пустым

#### Экземпляр класса Wordplay должен иметь один атрибут:
* words — список, содержащий набор слов
#### Класс Wordplay должен иметь четыре метода экземпляра:
* add_word() — метод, принимающий в качестве аргумента слово и добавляющий его в набор. Если слово уже есть в наборе, метод ничего не должен делать
* words_with_length() — метод, принимающий в качестве аргумента натуральное число n и возвращающий список слов из набора, длина которых равна n
* only() — метод, принимающий произвольное количество аргументов — букв, и возвращающий все слова из набора, которые включают в себя только переданные буквы
* avoid() — метод, принимающий произвольное количество аргументов — букв, и возвращающий все слова из списка words, которые не содержат ни одну из этих букв
##### Примечание 1. Слова в списках, возвращаемых методами words_with_length(), only() и avoid(), должны располагаться в том порядке, в котором они были добавлены.
#####  Примечание 2. Экземпляр класса Wordplay не должен зависеть от списка, на основе которого он был создан. Другими словами, если исходный список изменится, то экземпляр класса Wordplay измениться не должен.
##### Примечание 3. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.

<table align="center">
  <tbody>
    <tr>
      <th>Sample Input 1: </th>
      <th>Sample Input 2: </th>
      <th>Sample Input 3: </th>
      <th>Sample Input 4: </th>
    </tr>
    <tr>
      <td align="center">wordplay = Wordplay()<br>
                          print(wordplay.words_with_length(1))<br>
                          print(wordplay.only('a', 'b', 'c'))<br>
                          print(wordplay.avoid('a', 'b', 'c'))<br></td>
      <td align="center">wordplay = Wordplay()<br>
                          print(wordplay.words)<br>
                          wordplay.add_word('bee')<br>
                          wordplay.add_word('geek')<br>
                          print(wordplay.words)<br></td>
      <td align="center">wordplay = Wordplay(['bee', 'geek', 'cool', 'stepik'])<br>
                          wordplay.add_word('python')<br>
                          print(wordplay.words_with_length(4))<br></td>
      <td align="center">wordplay = Wordplay(['o', 'to', 'otto', 'top', 't'])<br>
                          print(wordplay.only('o', 't'))<br></td>
    </tr>
    <tr>
      <td>Sample Output 1:</td>
      <td>Sample Output 2:</td>
      <td>Sample Output 3:</td>
      <td>Sample Output 4:</td>
      </tr>
    <tr>
      <td align="center">
      []<br>
      []<br>
      []<br>
      </td>
      <td align="center">
                       []<br>
                       ['bee', 'geek']<br>
      </td>
      <td align="center">
                       ['geek', 'cool']<br>
      </td>
      <td align="center">
                       ['o', 'to', 'otto', 't']<br>
      </td>
    </tr>
  </tbody>
</table>



## Примеры решений:
* Первый вариант решения
```python
class Wordplay:
    def __init__(self, word=[]):
        self.word = word
        self.words = [i for i in self.word if len(self.word)]
   
    def add_word(self, text):
        if text not in self.words:
            self.words.append(text)

    def words_with_length(self, n):
         return list(filter(lambda x: len(x) == n, self.words))
    def only(self, *args):
         return list(filter(lambda x:  x not in [x for i in x if i not in args], self.words))
    def avoid(self, *args):
         return list(filter(lambda x: x not in [x for i in args if i in x], self.words))
```
* Второй вариант решения
```python
class Wordplay:
    def __init__(self, words=()):
        self.words = []
        self.words.extend(words)
        
    def add_word(self, word):
        self.words.append(word)
        
    def words_with_length(self, n):
        return [w for w in self.words if len(w) == n]
    
    def only(self, *args):
        return [w for w in self.words if set(w) <= set(args)]

    def avoid(self, *args):
        return [w for w in self.words if len(set(w) & set(args)) == 0]
```


