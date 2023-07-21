<h2 style="text-align:center">Класс SuppressAll</h2>

### Требовалось реализовать класс SuppressAll. При создании экземпляра класс не должен был принимать никаких аргументов.
#### Предполагалось, что экземпляр класса SuppressAll будет являться контекстным менеджером, подавляющим любое исключение, которое возбуждается во время выполнения кода внутри блока with.
#### Программист торопился и решил задачу неправильно. Дополните приведенный ниже код и реализуйте класс SuppressAll правильно.
```python
class SuppressAll:
    def __enter__(self):
        return self

    def __exit__(self, exc_type):
        return False
```
##### Примечание 1. Наглядные примеры использования класса SuppressAll продемонстрированы в тестовых данных.
##### Примечание 2. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.
##### Примечание 3. Класс SuppressAll должен удовлетворять протоколу контекстного менеджера, то есть иметь методы __enter__() и __exit__(). Реализация же протокола может быть произвольной.

<table align="center">
  <tbody>
    <tr>
      <th>Sample Input 1: </th>
      <th>Sample Input 2: </th>
    </tr>
    <tr>
      <td align="center">print('start')<br>
                          with SuppressAll():<br>
                              print('Python generation!')<br>
                              raise ValueError<br>
                          print('end')<br></td>
      <td align="center">print('start')<br>
                        with SuppressAll():<br>
                            print('Python generation!')<br>
                        print('end')<br></td>
    </tr>
    <tr>
      <td>Sample Output 1:</td>
      <td>Sample Output 2:</td>
      </tr>
    <tr>
      <td align="center">
                        start<br>
                        Python generation!<br>
                        end<br>
      </td>
      <td align="center">
                        start<br>
                        Python generation!<br>
                        end<br>
      </td>
    </tr>
  </tbody>
</table>



## Примеры решений:
* Первый вариант решения
```python
class SuppressAll:
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        return True
```
* Второй вариант решения

```python
class SuppressAll:
    def __enter__(self):
        return self

    def __exit__(self, *args, **kwargs):
        return True
```


