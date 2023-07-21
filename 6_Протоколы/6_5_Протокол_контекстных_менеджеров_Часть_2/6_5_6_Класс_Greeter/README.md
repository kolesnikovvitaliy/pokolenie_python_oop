<h2 style="text-align:center">Класс Greeter</h2>

### Реализуйте класс Greeter. При создании экземпляра класс должен принимать один аргумент:
* name — имя пользователя
#### Экземпляр класса Greeter должен иметь один атрибут:
* name — имя пользователя
#### Экземпляр класса Greeter должен являться контекстным менеджером, который приветствует пользователя с именем name перед выполнением блока with и выводит текст:
> Приветствую, <имя пользователя>!
#### а также прощается с ним после выполнения блока with и выводит текст:
> До встречи, <имя пользователя>!
##### Примечание 1. Наглядные примеры использования класса Greeter продемонстрированы в тестовых данных.
##### Примечание 2. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.
##### Примечание 3. Класс Greeter должен удовлетворять протоколу контекстного менеджера, то есть иметь методы __enter__() и __exit__(). Реализация же протокола может быть произвольной.

<table align="center">
  <tbody>
    <tr>
      <th>Sample Input 1: </th>
      <th>Sample Input 2: </th>
      <th>Sample Input 3: </th>
      <th>Sample Input 4: </th>
    </tr>
    <tr>
      <td align="center">with Greeter('Кейв'):<br>
                          print('...')<br></td>
      <td align="center">with Greeter('Кейв') as greeter:<br>
                            print(greeter.name)<br></td>
      <td align="center">with Greeter('Матильда') as greeter:<br>
                                  pass<br></td>
      <td align="center">with Greeter('Михаил Г.') as greeter:<br>
                          print(<br>
                              '\nКак бессонница в час ночной\n'<br>
                              'Меняет, нелюдимая, облик твой,\n'<br>
                              'Чьих невольница ты идей?\n'<br>
                              'Зачем тебе охотиться на людей?\n'<br>
    )<br></td>
    </tr>
    <tr>
      <td>Sample Output 1:</td>
      <td>Sample Output 2:</td>
      <td>Sample Output 3:</td>
      <td>Sample Output 4:</td>
      </tr>
    <tr>
      <td align="center">
                        Приветствую, Кейв!<br>
                        ...<br>
                        До встречи, Кейв!<br>
      </td>
      <td align="center">
                        Приветствую, Кейв!<br>
                        Кейв<br>
                        До встречи, Кейв!<br>
      </td>
      <td align="center">
                        Приветствую, Матильда!<br>
                        До встречи, Матильда!<br>
      </td>
      <td align="center">
                        Приветствую, Михаил Г.!<br>
<br>
                        Как бессонница в час ночной<br>
                        Меняет, нелюдимая, облик твой,<br>
                        Чьих невольница ты идей?<br>
                        Зачем тебе охотиться на людей?<br>
<br>
                        До встречи, Михаил Г.!<br>
      </td>
    </tr>
  </tbody>
</table>



## Примеры решений:
* Первый вариант решения
```python
class Greeter:
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        print(f"Приветствую, {self.name}!")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print(f"До встречи, {self.name}!")
        return True
```
* Второй вариант решения

```python
class Greeter:
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        print(f'Приветствую, {self.name}!')
        return self

    def __exit__(self, *args, **kwargs):
        print(f'До встречи, {self.name}!')
```


