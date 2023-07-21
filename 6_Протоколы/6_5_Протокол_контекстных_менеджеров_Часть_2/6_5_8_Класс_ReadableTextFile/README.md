<h2 style="text-align:center">Класс ReadableTextFile</h2>

### Реализуйте класс ReadableTextFile. При создании экземпляра класс должен принимать один аргумент:
* filename — имя текстового файла
#### Экземпляр класса ReadableTextFile должен являться контекстным менеджером, который открывает файл с именем filename на чтение в кодировке UTF-8 и позволяет получать его строки без символа переноса строки \n на конце. Также контекстный менеджер должен закрывать открытый им файл после выполнения кода внутри блока with.

##### Примечание 1. Наглядные примеры использования класса ReadableTextFile продемонстрированы в тестовых данных.
##### Примечание 2. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.
##### Примечание 3. Класс ReadableTextFile должен удовлетворять протоколу контекстного менеджера, то есть иметь методы __enter__() и __exit__(). Реализация же протокола может быть произвольной.

<table align="center">
  <tbody>
    <tr>
      <th>Sample Input 1: </th>
      <th>Sample Input 2: </th>
    </tr>
    <tr>
      <td align="center">with open('glados_quotes.txt', 'w', encoding='utf-8') as file:<br>
                          print('Только посмотрите!', file=file)<br>
                          print('Как величаво она парит в воздухе', file=file)<br>
                          print('Как орел', file=file)<br>
                          print('На воздушном шаре', file=file)<br>
                      with ReadableTextFile('glados_quotes.txt') as file:<br>
                          for line in file:<br>
                              print(line)<br></td>
      <td align="center">with open('poem.txt', 'w', encoding='utf-8') as file:<br>
                          print('Я кашлянул в звенящей тишине,', file=file)<br>
                          print('И от шального эха стало жутко…', file=file)<br>
                          print('Расскажет ли утятам обо мне', file=file)<br>
                          print('под утро мной испуганная утка?', file=file)<br>
                      with ReadableTextFile('poem.txt') as file:<br>
                          for line in file:<br>
                              print(line)<br></td>
    </tr>
    <tr>
      <td>Sample Output 1:</td>
      <td>Sample Output 2:</td>
      </tr>
    <tr>
      <td align="center">
                        Только посмотрите!<br>
                        Как величаво она парит в воздухе<br>
                        Как орел<br>
                        На воздушном шаре<br>
      </td>
      <td align="center">
                        Я кашлянул в звенящей тишине,<br>
                        И от шального эха стало жутко…<br>
                        Расскажет ли утятам обо мне<br>
                        под утро мной испуганная утка?<br>
      </td>
    </tr>
  </tbody>
</table>



## Примеры решений:
* Первый вариант решения
```python
class ReadableTextFile:
    def __init__(self, filename):
        self.filename = filename
    
    def __enter__(self):
        self.file = open(self.filename, mode='r', encoding='utf-8')
        yield self.file.read().strip()
    
    def __exit__(self, exc_type, exc_value, traceback):
        self.file.close()
        return True
```
* Второй вариант решения

```python
class ReadableTextFile:
    def __init__(self, filename):
        self.file = open(filename, encoding='UTF-8')

    def __enter__(self):
        return map(str.strip, self.file)

    def __exit__(self, *args, **kwargs):
        self.file.close()
```


