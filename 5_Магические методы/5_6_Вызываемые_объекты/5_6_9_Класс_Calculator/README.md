<h2 style="text-align:center">Класс Calculator</h2>

### Реализуйте класс Calculator, экземпляры которого позволяют выполнять различные арифметические операции с двумя числами. При создании экземпляра класс не должен принимать никаких аргументов.

#### Экземпляр класса Calculator должен являться вызываемым объектом и принимать три аргумента:
* a — число
* b — число
* operation — один из символов +, -, * и /
  
#### Если operation равняется +, экземпляр класса Calculator должен вернуть сумму a и b, если - — разность a и b, если * — произведение a и b, если / — частное a и b. При попытке выполнить деление на ноль должно быть возбуждено исключение ValueError с текстом:
> Деление на ноль невозможно
#### Примечание 1. Числами будем считать экземпляры классов int и float.
##### Примечание 2. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.
##### Примечание 3. Никаких ограничений касательно реализации класса Calculator нет, она может быть произвольной.

<table align="center">
  <tbody>
    <tr>
      <th>Sample Input 1: </th>
      <th>Sample Input 2: </th>
    </tr>
    <tr>
      <td align="center">calculator = Calculator()<br>
                        print(calculator(10, 5, '+'))<br>
                        print(calculator(10, 5, '-'))<br>
                        print(calculator(10, 5, '*'))<br>
                        print(calculator(10, 5, '/'))<br></td>
      <td align="center">calculator = Calculator()<br>
                        try:<br>
                            print(calculator(10, 0, '/'))<br>
                        except ValueError as e:<br>
                            print(e)<br></td>
    </tr>
    <tr>
      <td>Sample Output 1:</td>
      <td>Sample Output 2:</td>
      </tr>
    <tr>
      <td align="center">
                        15<br>
                        5<br>
                        50<br>
                        2.0<br>
      </td>
      <td align="center">
                        Деление на ноль невозможно<br>
      </td>
    </tr>
  </tbody>
</table>



## Примеры решений:
* Первый вариант решения
```python
class Calculator:
   def __call__(self, a: int, b: int, operation: str):
        if operation == '/' and b == 0:
            raise ValueError('Деление на ноль невозможно')
        return eval(f'{a}{operation}{b}')
```
* Второй вариант решения

```python
class Calculator:

    def __call__(self, a, b, operation):
        match operation:
            case '+': return a + b
            case '-': return a - b
            case '*': return a * b
            case '/':
                try:
                    return a / b
                except:
                    raise ValueError('Деление на ноль невозможно')
```


