<h2 style="text-align:center">Класс Book</h2>

### Требовалось реализовать класс Book, описывающий книгу. При создании экземпляра класс должен был принимать три аргумента в следующем порядке:
* title — название книги
* author — автор книги
* year — год выпуска книги
#### Предполагалось, что экземпляры класса Book будут иметь следующее формальное строковое представление:
> Book('<название книги>', '<автор книги>', <год выпуска книги>)
#### И следующее неформальное строковое представление:
> <название книги> (<автор книги>, <год выпуска книги>)
#### Программист торопился и решил задачу неправильно. Исправьте приведенный ниже код и реализуйте класс Book правильно.
```python
class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f"Book('{title}', '{author}', {year})"

    def __repr__():
        return f'{title} ({author}, {year})'
```
##### Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.
##### Примечание 2. Никаких ограничений касательно реализации класса Book нет, она может быть произвольной.

<table align="center">
  <tbody>
    <tr>
      <th>Sample Input 1: </th>
      <th>Sample Input 2: </th>
    </tr>
    <tr>
      <td align="center">book = Book('Изучаем Python', 'Марк Лутц', 2021)<br>
                          print(book)<br>
                          print(repr(book))<br></td>
      <td align="center">book = Book('Программируем на Python', 'Майкл Доусон', 2023)<br>
                          print(str(book))<br>
                          print(repr(book))<br></td>
    </tr>
    <tr>
      <td>Sample Output 1:</td>
      <td>Sample Output 2:</td>
      </tr>
    <tr>
      <td align="center">
                        Изучаем Python (Марк Лутц, 2021)<br>
                        Book('Изучаем Python', 'Марк Лутц', 2021)<br>
      </td>
      <td align="center">
                        Программируем на Python (Майкл Доусон, 2023)<br>
                        Book('Программируем на Python', 'Майкл Доусон', 2023)<br>
      </td>
    </tr>
  </tbody>
</table>



## Примеры решений:
* Первый вариант решения
```python
class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
    
    def __str__(self):
        return f'{self.title} ({self.author}, {self.year})'
    
    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.year})"
```


