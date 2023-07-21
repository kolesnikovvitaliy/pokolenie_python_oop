<h2 style="text-align:center">Класс Reloopable</h2>


### Реализуйте класс Reloopable. При создании экземпляра класс должен принимать один аргумент:
* file — открытый на чтение файловый объект
#### Экземпляр класса Reloopable должен являться контекстным менеджером, который позволяет многократно итерироваться по файловому объекту file внутри блока with. Также контекстный менеджер должен закрывать используемый им файловый объект после выполнения кода внутри блока with.

##### Примечание 1. Наглядные примеры использования класса Reloopable продемонстрированы в тестовых данных.
##### Примечание 2. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.
##### Примечание 3. Класс Reloopable должен удовлетворять протоколу контекстного менеджера, то есть иметь методы __enter__() и __exit__(). Реализация же протокола может быть произвольной.

<table align="center">
  <tbody>
    <tr>
      <th>Sample Input 1: </th>
      <th>Sample Input 2: </th>
    </tr>
    <tr>
      <td align="center">with open('file.txt', 'w') as file:<br>
                            file.write('Evil is evil\n')<br>
                            file.write('Lesser, greater, middling\n')<br>
                            file.write('Makes no difference\n')<br>
                        with Reloopable(open('file.txt')) as reloopable:<br>
                            for line in reloopable:<br>
                                print(line.strip())<br>
                            for line in reloopable:<br>
                                print(line.strip())<br></td>
      <td align="center">with open('file.txt', 'w') as file:<br>
                              pass<br>
                          file = open('file.txt')<br><br>
                          print(file.closed)<br>
                          with Reloopable(file) as reloopable:<br>
                              pass<br>
                          print(file.closed)<br></td>
    </tr>
    <tr>
      <td>Sample Output 1:</td>
      <td>Sample Output 2:</td>
      </tr>
    <tr>
      <td align="center">
                        Evil is evil<br>
                        Lesser, greater, middling<br>
                        Makes no difference<br>
                        Evil is evil<br>
                        Lesser, greater, middling<br>
                        Makes no difference<br>
      </td>
      <td align="center">
                        False<br>
                        True<br>
      </td>
    </tr>
  </tbody>
</table>



## Примеры решений:
* Первый вариант решения
```python
class Reloopable:
    def __init__(self, file):
        self.file = file

    def __enter__(self):
        return [self.file.read()]
    
    def __exit__(self, exc_type, exc_value, traceback):
        self.file.close()
```
* Второй вариант решения

```python
class Reloopable:
    def __init__(self, file):
        self.file = file 
        
    def __enter__(self):
        return list(self.file)
    
    def __exit__(self, *args, **kwargs):
        self.file.close()
```


