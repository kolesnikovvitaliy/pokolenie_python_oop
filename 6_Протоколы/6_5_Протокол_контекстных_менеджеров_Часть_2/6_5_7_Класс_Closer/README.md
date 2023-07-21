<h2 style="text-align:center">Класс Closer</h2>

### Реализуйте класс Closer. При создании экземпляра класс должен принимать один аргумент:
* obj — произвольный объект
#### Экземпляр класса Closer должен являться контекстным менеджером, который закрывает используемый объект obj с помощью метода close() после выполнения кода внутри блока with. Если объект не поддерживает операцию закрытия, контекстный менеджер должен вывести:
> Незакрываемый объект
##### Примечание 1. Наглядные примеры использования класса Closer продемонстрированы в тестовых данных.
##### Примечание 2. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.
##### Примечание 3. Класс Closer должен удовлетворять протоколу контекстного менеджера, то есть иметь методы __enter__() и __exit__(). Реализация же протокола может быть произвольной.

<table align="center">
  <tbody>
    <tr>
      <th>Sample Input 1: </th>
      <th>Sample Input 2: </th>
    </tr>
    <tr>
      <td align="center">output = open('output.txt', 'w', encoding='utf-8')<br>
                          with Closer(output) as file:<br>
                              print(file.closed)<br>
                          print(file.closed)<br></td>
      <td align="center">with Closer(5) as i:<br>
                              i += 1<br>
                          print(i)<br></td>
    </tr>
    <tr>
      <td>Sample Output 1:</td>
      <td>Sample Output 2:</td>
      </tr>
    <tr>
      <td align="center">
                        False<br>
                        True<br>
      </td>
      <td align="center">
                        Незакрываемый объект<br>
                        6<br>
      </td>
    </tr>
  </tbody>
</table>



## Примеры решений:
* Первый вариант решения
```python
class Closer:
    def __init__(self, obj):
        self.obj = obj

    def __enter__(self):
        return self.obj
    
    def __exit__(self, exc_type, exc_value, traceback):
        try:
            self.obj.close()
        except:
            print("Незакрываемый объект")
        return True
```
* Второй вариант решения

```python
class Closer:
    def __init__(self, obj):
        self.obj = obj

    def __enter__(self):
        return self.obj

    def __exit__(self, *args, **kwargs):
        try:
            self.obj.close()
            return False
        except AttributeError:
            print('Незакрываемый объект')
            return True
```


