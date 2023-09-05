<h2 style="text-align:center">Класс Pagination</h2>

### Реализуйте класс Pagination для обработки данных с разбивкой по страницам. Разбивка по страницам используется для разделения большого количества данных на части. Экземпляр класса Pagination должен создаваться на основе двух значений:

* исходные данные, представленные в виде списка с произвольными элементами
* размер страницы, то есть количество элементов, отображаемых на каждой странице
```python
alphabet = list('abcdefghijklmnopqrstuvwxyz')
pagination = Pagination(alphabet, 4)
```
#### Для получения содержимого страницы должен использоваться метод get_visible_items():
```python 
print(pagination.get_visible_items())    # ['a', 'b', 'c', 'd']
```
#### Обратите внимание, содержимое страницы должно быть представлено в виде списка. Перемещение по страницам должно происходить с помощью следующих методов:

* prev_page() — вернуться к предыдущей странице
* next_page() — перейти к следующей странице
* first_page() — вернуться к первой странице
* last_page() — перейти к последней странице
* go_to_page() — перейти к странице с указанным номером (1 — первая страница, 2 — вторая страница, и так далее)
```python 
pagination.next_page()
print(pagination.get_visible_items())    # ['e', 'f', 'g', 'h']

pagination.last_page()
print(pagination.get_visible_items())    # ['y', 'z']
```
#### Методы для перемещения по страницам должны быть применимы друг за другом:
```python
pagination.first_page()
pagination.next_page().next_page()   
print(pagination.get_visible_items())    # ['i', 'j', 'k', 'l']
```
#### С помощью атрибутов total_pages и current_page должна быть возможность получить общее количество страниц и текущую страницу соответственно:
```python
print(pagination.total_pages)            # 7
print(pagination.current_page)           # 3
```
### При нахождении на первой странице и перемещении к предыдущей странице, текущей страницей должна остаться первая страница. Аналогично при нахождении на последней странице и перемещении к следующей странице, текущей страницей должна остаться последняя страница:
```python
pagination.first_page()
pagination.prev_page()
print(pagination.get_visible_items())    # ['a', 'b', 'c', 'd']

pagination.last_page()
pagination.next_page()
print(pagination.get_visible_items())    # ['y', 'z']
```
#### При перемещении к нулевой или менее странице, текущей страницей должна стать первая страница. Аналогично при перемещении к странице, номер которой превышает общее количество страниц, текущей страницей должна стать последняя страница:
```python
pagination.go_to_page(-100)
print(pagination.get_visible_items())    # ['a', 'b', 'c', 'd']

pagination.go_to_page(100)
print(pagination.get_visible_items())    # ['y', 'z']
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
      <td align="center">alphabet = list('abcdefghijklmnopqrstuvwxyz')<br>
                          pagination = Pagination(alphabet, 4)<br>
                          print(pagination.get_visible_items())<br></td>
      <td align="center">alphabet = list('abcdefghijklmnopqrstuvwxyz')<br>
                          pagination = Pagination(alphabet, 4)<br>
                          pagination.next_page()<br>
                          print(pagination.get_visible_items())<br>
                          pagination.last_page()<br>
                          print(pagination.get_visible_items())<br></td>
      <td align="center">alphabet = list('abcdefghijklmnopqrstuvwxyz')<br>
                          pagination = Pagination(alphabet, 4)<br>
                          pagination.next_page().next_page()<br>
                          print(pagination.get_visible_items())<br>
                          print(pagination.total_pages)<br>
                          print(pagination.current_page)<br></td>
      <td align="center">alphabet = list('abcdefghijklmnopqrstuvwxyz')<br>
                          pagination = Pagination(alphabet, 4)<br>
                          pagination.prev_page()<br>
                          print(pagination.get_visible_items())<br>
                          pagination.last_page()<br>
                          pagination.next_page()<br>
                          print(pagination.get_visible_items())<br></td>
    </tr>
    <tr>
      <td>Sample Output 1:</td>
      <td>Sample Output 2:</td>
      <td>Sample Output 3:</td>
      <td>Sample Output 4:</td>
      </tr>
    <tr>
      <td align="center">
                        ['a', 'b', 'c', 'd']<br>
      </td>
      <td align="center">
                        ['e', 'f', 'g', 'h']<br>
                        ['y', 'z']<br>
      </td>
      <td align="center">
                        ['i', 'j', 'k', 'l']<br>
                        7<br>
                        3<br>
      </td>
      <td align="center">
                        ['a', 'b', 'c', 'd']<br>
                        ['y', 'z']<br>
      </td>
    </tr>
  </tbody>
</table>



## Примеры решений:
* Первый вариант решения
```python
class Pagination:
    def __init__(self, text: list[str], num: int):
        self.num = num
        self.pages = text

    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self, text):
        k = 1
        self._pages = dict()
        while text:
            self._pages.setdefault(k, []).extend(text[:self.num])
            k += 1
            text = text[self.num:]
        self.total_pages = max(self.pages.keys())
        self.current_page = 1

    def get_visible_items(self):
        '''Отображение текущей страницы'''
        return self.pages[self.current_page]

    def prev_page(self):
        '''вернуться к предыдущей странице'''
        num = self.current_page - 1
        self.go_to_page(num)
        return self

    def next_page(self):
        '''перейти к следующей странице'''
        num = self.current_page + 1
        self.go_to_page(num)
        return self

    def first_page(self):
        '''вернуться к первой странице'''
        self.current_page = 1

    def last_page(self):
        '''перейти к последней странице'''
        self.current_page = self.total_pages

    def go_to_page(self, num: int):
        '''перейти к странице с указанным номером (
            1 — первая страница,
            2 — вторая страница, и так далее)'''
        if num > self.total_pages:
            return self.last_page()
        elif num < 1:
            return self.first_page()
        else:
            self.current_page = num
```
* Второй вариант решения

```python
class Pagination:
    def __init__(self, data, size):
        self.pages = [data[i: i+size] for i in range(0, len(data), size)]
        self.total_pages = len(self.pages)
        self.current_page = 1

    def prev_page(self):
        self.current_page = max(1, self.current_page - 1)
        return self

    def next_page(self):
        self.current_page = min(self.total_pages, self.current_page + 1)
        return self

    def first_page(self):
        self.current_page = 1

    def last_page(self):
        self.current_page = self.total_pages

    def go_to_page(self, page):
        self.current_page = max(1, min(page, self.total_pages))

    def get_visible_items(self):
        return self.pages[self.current_page - 1]
```


