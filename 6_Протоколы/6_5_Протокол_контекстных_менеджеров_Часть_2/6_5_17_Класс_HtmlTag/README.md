<h2 style="text-align:center">Класс HtmlTag</h2>


### HTML — это язык разметки, используемый для определения структуры веб-страниц, посещаемых пользователями. HTML предоставляет средства для создания заголовков, абзацев, ссылок, цитат и других элементов. Каждый HTML-элемент обозначается открывающим и закрывающим тегами:
> <p>Если в ходе теста нет угрозы жизни, разве это вообще наука?</p>
### Теги заключаются в угловые скобки. Они определяют, где элемент начинается и где он заканчивается. Единственным различием между открывающим и закрывающим тегами является косая черта, которая предшествует имени тега.
### Открывающий и закрывающий теги, а также заключенное в них содержимое, могут располагаться как на одной строке (пример выше), так и на разных. Если теги и содержимое располагаются на разных строках, то сперва указывается открывающий тег, затем на следующий строке с отступом в два пробела указывается содержимое, а после на следующей строке указывается закрывающий тег, который располагается на том же уровне отступов, что и открывающий тег:
> <p>
> Наука не решает вопрос Почему?, она решает вопрос А почему бы и нет?
> </p>

### Реализуйте класс HtmlTag. При создании экземпляра класс должен принимать два аргумента в следующем порядке:
* tag — HTML тег
* inline — булево значение, по умолчанию равняется False
#### Экземпляр класса HtmlTag должен являться реентерабельным контекстным менеджером, который позволяет генерировать HTML-код с правильными отступами и глубиной вложенности тегов. Параметр inline должен определять положение тегов и их содержимого. Если он имеет значение True, теги и содержимое должны располагаться на одной строке, если False — на разных строках.

#### Класс HtmlTag должен иметь один метод экземпляра:
* print() — метод, принимающий в качестве аргумента содержимое тега и выводящий его в рамках этого тега

##### Примечание 1. Наглядные примеры использования класса HtmlTag продемонстрированы в тестовых данных.
##### Примечание 2. В качестве отступов для каждого уровня используйте два пробела.
##### Примечание 3. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.
##### Примечание 4. Класс HtmlTag должен удовлетворять протоколу контекстного менеджера, то есть иметь методы __enter__() и __exit__(). Реализация же протокола может быть произвольной.

<table align="center">
  <tbody>
    <tr>
      <th>Sample Input 1: </th>
      <th>Sample Input 2: </th>
      <th>Sample Input 2: </th>
    </tr>
    <tr>
      <td align="center">with HtmlTag('body') as _:<br>
                            with HtmlTag('h1') as header:<br>
                                header.print('Поколение Python')<br>
                            with HtmlTag('p') as section:<br>
                                section.print('Cерия курсов по языку программирования Python от команды BEEGEEK')<br></td>
      <td align="center">with HtmlTag('body') as _:<br>
                            with HtmlTag('h1', True) as header:<br>
                                header.print('Поколение Python')<br>
                            with HtmlTag('p', True) as section:<br>
                                section.print('Cерия курсов по языку программирования Python от команды BEEGEEK')<br></td>
      <td align="center">with HtmlTag('body') as _:<br>
                            with HtmlTag('h1', True) as header:<br>
                                header.print('Здесь есть что-то интересное')<br>
                            with HtmlTag('a', True) as section:<br>
                                section.print('https://stepik.org/media/attachments/course/98974/watch_me.mp4')<br></td>
    </tr>
    <tr>
      <td>Sample Output 1:</td>
      <td>Sample Output 2:</td>
      <td>Sample Output 2:</td>
      </tr>
    <tr>
      <td align="center">
                        <body><br>
                            <h1><br>
                              Поколение Python<br>
                            </h1><br>
                            <p><br>
                              Cерия курсов по языку программирования Python от команды BEEGEEK<br>
                            </p><br>
                          </body><br>
      </td>
      <td align="center">
                        <body><br>
                          <h1>Поколение Python</h1><br>
                          <p>Cерия курсов по языку программирования Python от команды BEEGEEK</p><br>
                        </body><br> 
      </td>
      <td align="center">
                        <body><br>
                          <h1>Здесь есть что-то интересное</h1><br>
                          <a>https://stepik.org/media/attachments/course/98974/watch_me.mp4</a><br>
                        </body><br>
      </td>
    </tr>
  </tbody>
</table>



## Примеры решений:
* Первый вариант решения
```python
class HtmlTag:
    level = -1
    def __init__(self, tag, inline=False):
        self.tag = tag
        self.inline = inline
    
    def __enter__(self):
        __class__.level += 1
        if self.inline:
            print('  ' * __class__.level + f'<{self.tag}>', end='')
        else:
            print('  ' * __class__.level + f'<{self.tag}>')
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        if self.inline:
            __class__.level -= 1
            print(f'</{self.tag}>')
        else:
            print('  ' * __class__.level + f'</{self.tag}>')
        __class__.level -= 1

    def print(self, text):
        __class__.level += 1
        if self.inline:
            print(text, end='')
        else:
            print('  ' * __class__.level + text)
            __class__.level -= 1
```
* Второй вариант решения

```python
class HtmlTag:
    '''Creating the right html body'''
    
    counter = 0
    
    def __init__(self, tag, inline=False):
        self.tag = tag
        self.inline = '' if inline else '\n'
        
    def __enter__(self):
        print(f'{"  " * HtmlTag.counter}<{self.tag}>', end = self.inline)
        HtmlTag.counter += 1
        return self
    
    def print(self, text):
        print(f'{"  " * HtmlTag.counter if self.inline else ""}{text}', end=self.inline)
        
    def __exit__(self, exc_type, exc_value, exc_traceback):
        HtmlTag.counter -= 1
        print(f'{"  " * HtmlTag.counter if self.inline else ""}</{self.tag}>')
```


