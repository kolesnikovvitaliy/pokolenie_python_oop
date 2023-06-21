<h2 style="text-align:center">Класс TextHandler</h2>

### Будем называть словом любую последовательность из одной или более букв. Текстом будем считать набор слов, разделенных пробелами.
### Реализуйте класс TextHandler, описывающий изначально пустой расширяемый набор слов. При создании экземпляра класс не должен принимать никаких аргументов.

#### Экземпляр класса TextHandler должен иметь три метода:
* add_words() — метод, принимающий в качестве аргумента текст и добавляющий слова из данного текста в набор
* get_shortest_words() — метод, возвращающий актуальный список самых коротких слов в наборе
* get_longest_words() — метод, возвращающий актуальный список самых длинных слов в наборе
##### Примечание 1. Слова в списках, возвращаемых методами get_shortest_words() и get_longest_words(), должны располагаться в том порядке, в котором они были добавлены в набор.
##### Примечание 2. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.

<table align="center">
  <tbody>
    <tr>
      <th>Sample Input 1: </th>
      <th>Sample Input 2: </th>
      <th>Sample Input 3: </th>
    </tr>
    <tr>
      <td align="center">texthandler = TextHandler()<br>
                        print(texthandler.get_shortest_words())<br>
                        print(texthandler.get_longest_words())<br></td>
      <td align="center">texthandler = TextHandler()<br>
                        texthandler.add_words('do not be sorry')<br>
                        texthandler.add_words('be')<br>
                        texthandler.add_words('better')<br>
                        print(texthandler.get_shortest_words())<br>
                        print(texthandler.get_longest_words())<br></td>
      <td align="center">texthandler = TextHandler()<br>
                          texthandler.add_words('The world will hold my trial for your sins')<br>
                          texthandler.add_words('Never meant to see the sky, never meant to live')<br>
                          print(texthandler.get_shortest_words())<br>
                          print(texthandler.get_longest_words())<br></td>
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
      </td>
      <td align="center">
                       ['do', 'be', 'be']<br>
                       ['better']<br>
      </td>
      <td align="center">
                       ['my', 'to', 'to']<br>
                       ['world', 'trial', 'Never', 'meant', 'never', 'meant']<br>
      </td>
    </tr>
  </tbody>
</table>



## Примеры решений:
* Первый вариант решения
```python
class TextHandler:
    def __init__(self):
        self.words = list()

    def add_words(self, text):
        [self.words.append(i) for i in text.split()]

    def get_shortest_words(self):
        if len(self.words) > 0:
            min_len_text = min(map(len, self.words))
            return list(filter(lambda x: len(x) <= min_len_text, self.words))
        return self.words

    def get_longest_words(self):
        if len(self.words) > 0:
            max_len_text = max(map(len, self.words))
            return list(filter(lambda x: len(x) == max_len_text, self.words))
        return self.words
```
* Второй вариант решения
```python
class TextHandler:
    def __init__(self):
        self.words = []
        
    def add_words(self, text):
        self.words += text.split()
        
    def get_shortest_words(self):
        return [w for w in self.words if len(w) == min(map(len, self.words))]
      
    def get_longest_words(self):
        return [w for w in self.words if len(w) == max(map(len, self.words))]


```


