<h2 style="text-align:center">Класс WriteSpy</h2>

### Реализуйте класс WriteSpy. При создании экземпляра класс должен принимать три аргумента в следующем порядке:
* file1 — файловый объект
* file2 — файловый объект
* to_close — булево значение, по умолчанию равняется False
#### Экземпляр класса WriteSpy должен являться контекстным менеджером, который выполняет операцию записи сразу в оба файловых объекта file1 и file2. Параметр to_close должен определять состояние файловых объектов file1 и file2 после завершения блока with. Если он имеет значение True, после завершения блока with контекстный менеджер должен закрыть оба файловых объекта, если False — оставить открытыми.
#### Класс WriteSpy должен иметь четыре метода экземпляра:
* write() — метод, принимающий в качестве аргумента текст и записывающий его в оба файловых объекта. Если хотя бы один из файловых объектов закрыт или недоступен для записи, должно быть возбуждено исключение ValueError с текстом:
> Файл закрыт или недоступен для записи
* close() — метод, немедленно закрывающий оба файловых объекта
* writable() — метод, возвращающий True, если оба файловых объекта доступны для записи, или False в противном случае
* closed() — метод, возвращающий True, если оба файловых объекта закрыты, или False в противном случае

##### Примечание 1. Наглядные примеры использования класса WriteSpy продемонстрированы в тестовых данных.
##### Примечание 2. Для проверки того, является ли файловый объект доступным для записи, используйте метод writable(). Данный метод возвращает True, если файловый объект доступен для записи, или False в противном случае. При попытке применить метод на закрытом файловом объекте будет возбуждено исключение.
##### Примечание 3. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.
##### Примечание 4. Класс WriteSpy должен удовлетворять протоколу контекстного менеджера, то есть иметь методы __enter__() и __exit__(). Реализация же протокола может быть произвольной.

<table align="center">
  <tbody>
    <tr>
      <th>Sample Input 1: </th>
      <th>Sample Input 2: </th>
      <th>Sample Input 2: </th>
    </tr>
    <tr>
      <td align="center">f1 = open('file1.txt', mode='w')<br>
                          f2 = open('file2.txt', mode='w')<br>
                          with WriteSpy(f1, f2, to_close=True) as combined:<br>
                              combined.write('You shall seal the blinding light that plagues their dreams\n')<br>
                              combined.write('You are the Vessel\n')<br>
                              combined.write('You are the Hollow Knight')<br>
                          print(f1.closed, f2.closed)<br>
                          with open('file1.txt') as file1, open('file2.txt') as file2:<br>
                              print(file1.read())<br>
                              print(file2.read())<br>
<br></td>
      <td align="center">f1 = open('file1.txt', mode='w')<br>
                          f2 = open('file2.txt', mode='w')<br>
                          with WriteSpy(f1, f2, to_close=True) as combined:<br>
                              print(combined.writable())<br>
                          f1 = open('file1.txt')<br>
                          f2 = open('file2.txt')<br>
                          with WriteSpy(f1, f2, to_close=True) as combined:<br>
                              print(combined.writable())<br></td>
      <td align="center">f1 = open('file1.txt', mode='w')<br>
                          f2 = open('file2.txt', mode='w')<br>
                          with WriteSpy(f1, f2, to_close=True) as combined:<br>
                              print(combined.closed())<br>
                              f1.close()<br>
                              print(combined.closed())<br>
                              f2.close()<br>
                              print(combined.closed())<br></td>
    </tr>
    <tr>
      <td>Sample Output 1:</td>
      <td>Sample Output 2:</td>
      </tr>
    <tr>
      <td align="center">
                        True True<br>
                          You shall seal the blinding light that plagues their dreams<br>
                          You are the Vessel<br>
                          You are the Hollow Knight<br>
                          You shall seal the blinding light that plagues their dreams<br>
                          You are the Vessel<br>
                          You are the Hollow Knight<br>
      </td>
      <td align="center">
                        True<br>
                        False<br>
      </td>
      <td align="center">
                        False<br>
                        False<br>
                        True<br>
      </td>
    </tr>
  </tbody>
</table>



## Примеры решений:
* Первый вариант решения
```python
class WriteSpy:
    def __init__(self, file_1, file_2, to_close=False):
        self.file_1 = file_1
        self.file_2 = file_2
        self.to_close = to_close
    
    def write(self, text):
        if self.writable():
            self.file_1.write(text)
            self.file_2.write(text)
        else:
            raise ValueError('Файл закрыт или недоступен для записи')
    
    def close(self):
        self.file_1.close()
        self.file_2.close()

    def writable(self):
        if self.file_1.closed or self.file_2.closed:
            return False
        else:
            if self.file_1.__dict__['mode'] == 'w' and self.file_2.__dict__['mode'] == 'w':
                return True
            return False
        
    def closed(self):
        if self.file_1.closed and self.file_2.closed:
            return True
        return False

    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        if self.to_close:
            self.close()
```
* Второй вариант решения

```python
class WriteSpy:
    def __init__(self, file1, file2, to_close=False):
        self.file1 = file1
        self.file2 = file2
        self.to_close = to_close

    def __enter__(self):
        return self

    def __exit__(self, *args, **kwargs):
        if self.to_close:
            self.close()

    def write(self, text):
        try:
            self.file1.write(text)
            self.file2.write(text)
        except:
            raise ValueError("Файл закрыт или недоступен для записи")

    def writable(self):
        if self.file1.closed or self.file2.closed:
            return False
        return self.file1.writable() and self.file2.writable()

    def close(self):
        self.file1.close()
        self.file2.close()

    def closed(self):
        return self.file1.closed and self.file2.closed
```


