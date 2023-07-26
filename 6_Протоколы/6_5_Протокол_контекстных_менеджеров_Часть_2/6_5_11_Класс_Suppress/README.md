<h2 style="text-align:center">Класс Suppress</h2>

### Реализуйте класс Suppress. При создании экземпляра класс должен принимать произвольное количество позиционных аргументов, каждый из которых представляет собой тип исключения.
#### Экземпляр класса Suppress должен являться контекстным менеджером, подавляющим исключение, если оно возбуждается во время выполнения кода внутри блока with. Подавляться должны исключения тех типов, которые были перечислены при создании контекстного менеджера.
#### Также экземпляр класса Suppress должен иметь один атрибут:
* exception — исключение, которое было подавлено контекстным менеджером. Если исключение не было подавлено или код был выполнен без исключений, атрибут должен иметь значение None

##### Примечание 1. Наглядные примеры использования класса Suppress продемонстрированы в тестовых данных.
##### Примечание 2. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.
##### Примечание 3. Класс Suppress должен удовлетворять протоколу контекстного менеджера, то есть иметь методы __enter__() и __exit__(). Реализация же протокола может быть произвольной.

<table align="center">
  <tbody>
    <tr>
      <th>Sample Input 1: </th>
      <th>Sample Input 2: </th>
      <th>Sample Input 2: </th>
    </tr>
    <tr>
      <td align="center">with Suppress(NameError):<br>
                            print('Этой переменной не существует -->', variable)<br>
                        print('Завершение программы')<br></td>
      <td align="center">with Suppress(TypeError, ValueError) as context:<br>
                                number = int('я число')<br>
                            print(context.exception)<br>
                            print(type(context.exception))<br></td>
      <td align="center">with Suppress() as context:<br>
                              print('All success!')<br>
                          print(context.exception)<br></td>
    </tr>
    <tr>
      <td>Sample Output 1:</td>
      <td>Sample Output 2:</td>
      <td>Sample Output 2:</td>
      </tr>
    <tr>
      <td align="center">
                        Завершение программы<br>
      </td>
      <td align="center">
                        invalid literal for int() with base 10: 'я число'<br>
                          <class 'ValueError'><br>
      </td>
      <td align="center">
                        All success!<br>
                        None<br>
      </td>
    </tr>
  </tbody>
</table>



## Примеры решений:
* Первый вариант решения
```python
class Suppress:
    def __init__(self, *args):
        self.args = args
        self.exception = None
    
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_value and exc_type  in self.args:
            self.exception = exc_value
        return True
```
* Второй вариант решения

```python
class Suppress:
    def __init__(self, *exceptions):
        self.exceptions = exceptions

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type in self.exceptions:
            self.exception = exc_val
            return True
        self.exception = None
        return False
```


