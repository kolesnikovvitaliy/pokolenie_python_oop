<h2 style="text-align:center">Класс UpperPrint</h2>

### Реализуйте класс UpperPrint. При создании экземпляра класс не должен принимать никаких аргументов.
#### Экземпляр класса UpperPrint должен являться контекстным менеджером, который внутри блока with позволяет выполнять все операции записи в стандартный поток вывода sys.stdout в верхнем регистре.


##### Примечание 1. Наглядные примеры использования класса UpperPrint продемонстрированы в тестовых данных.
##### Примечание 2. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.
##### Примечание 3. Класс UpperPrint должен удовлетворять протоколу контекстного менеджера, то есть иметь методы __enter__() и __exit__(). Реализация же протокола может быть произвольной.

<table align="center">
  <tbody>
    <tr>
      <th>Sample Input 1: </th>
      <th>Sample Input 2: </th>
    </tr>
    <tr>
      <td align="center">print('Если жизнь одаривает вас лимонами — не делайте лимонад')<br>
                          print('Заставьте жизнь забрать их обратно!')<br>
                          with UpperPrint():<br>
                              print('Мне не нужны твои проклятые лимоны!')<br>
                              print('Что мне с ними делать?')<br>
                          print('Требуйте встречи с менеджером, отвечающим за жизнь!')<br></td>
      <td align="center">with UpperPrint():<br>
                        print('Bee', 'Geek', 'Love', sep=' one ', end=' end')<br></td>
    </tr>
    <tr>
      <td>Sample Output 1:</td>
      <td>Sample Output 2:</td>
      </tr>
    <tr>
      <td align="center">
                        Если жизнь одаривает вас лимонами — не делайте лимонад<br>
                        Заставьте жизнь забрать их обратно!<br>
                        МНЕ НЕ НУЖНЫ ТВОИ ПРОКЛЯТЫЕ ЛИМОНЫ!<br>
                        ЧТО МНЕ С НИМИ ДЕЛАТЬ?<br>
                        Требуйте встречи с менеджером, отвечающим за жизнь!<br>
      </td>
      <td align="center">
                        BEE ONE GEEK ONE LOVE END<br>
      </td>
    </tr>
  </tbody>
</table>



## Примеры решений:
* Первый вариант решения
```python
import sys
class UpperPrint:
    def __enter__(self):
        self.output = sys.stdout
        sys.stdout = open('output.txt', 'w')        
    def __exit__(self, exc_type, exc_value, traceback):
        sys.stdout.close()
        sys.stdout = self.output
        with open('output.txt', mode='r') as text:
            print(text.read().strip().upper())
```
* Второй вариант решения

```python
import sys

class UpperPrint:
    def __enter__(self):
        self.w = sys.stdout.write
        sys.stdout.write = lambda t: self.w(t.upper())

    def __exit__(self, exc_type, exc_val, exc_tb):
        sys.stdout.write = self.w
```


