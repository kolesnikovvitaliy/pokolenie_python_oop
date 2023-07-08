<h2 style="text-align:center">Класс SuperString</h2>

### Реализуйте класс SuperString, описывающий строку. При создании экземпляра класс должен принимать один аргумент:
* string — значение строки
#### Экземпляр класса SuperString должен иметь следующее неформальное строковое представление:
> <значение строки>
#### Помимо этого, экземпляры класса SuperString должны поддерживать между собой операцию сложения с помощью оператора +, результатом которой должен являться новый экземпляр класса SuperString, представляющий конкатенацию исходных.
#### Также экземпляр класса SuperString должен поддерживать операции умножения, деления, побитового сдвига влево и побитового сдвига вправо на целое число n с помощью операторов *, /, << и >> соответственно:
* результатом умножения должен являться новый экземпляр класса SuperString, представляющий исходную строку, умноженную на n
* результатом деления должен являться новый экземпляр класса SuperString, представляющий строку из первых m символов исходной строки, где m — длина исходной строки, поделенная нацело на n
* результатом побитового сдвига влево должен являться новый экземпляр класса SuperString, представляющий исходную строку без последних n символов. Если n больше или равно длине исходной строки, результатом должен являться экземпляр класса SuperString, представляющий пустую строку
* результатом побитового сдвига вправо должен являться новый экземпляр класса SuperString, представляющий исходную строку без первых n символов. Если n больше или равно длине исходной строки, результатом должен являться экземпляр класса SuperString, представляющий пустую строку
#### Операция умножения должна быть выполнима независимо от порядка операндов, то есть должна быть возможность умножить как строку на число, так и число на строку.
##### Примечание 1. Будем гарантировать, что экземпляр класса SuperString всегда делится на ненулевое число.
##### Примечание 2. Если объект, с которым выполняется арифметическая операция, некорректен, метод, реализующий эту операцию, должен вернуть константу NotImplemented.
##### Примечание 3. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.
##### Примечание 4. Никаких ограничений касательно реализации класса SuperString нет, она может быть произвольной.

<table align="center">
  <tbody>
    <tr>
      <th>Sample Input 1: </th>
      <th>Sample Input 2: </th>
      <th>Sample Input 3: </th>
    </tr>
    <tr>
      <td align="center">s1 = SuperString('bee')<br>
                        s2 = SuperString('geek')<br>
                        print(s1 + s2)<br>
                        print(s2 + s1)<br></td>
      <td align="center">s = SuperString('beegeek')<br>
                          print(s * 2)<br>
                          print(3 * s)<br>
                          print(s / 3)<br></td>
      <td align="center">s = SuperString('beegeek')<br>
                          print(s << 4)<br>
                          print(s >> 3)<br></td>
    </tr>
    <tr>
      <td>Sample Output 1:</td>
      <td>Sample Output 2:</td>
      <td>Sample Output 3:</td>
      </tr>
    <tr>
      <td align="center">
                        beegeek<br>
                        geekbee<br>
      </td>
      <td align="center">
                        beegeekbeegeek<br>
                        beegeekbeegeekbeegeek<br>
                        be<br>
      </td>
      <td align="center">
                        bee<br>
                        geek<br>
      </td>
    </tr>
  </tbody>
</table>



## Примеры решений:
* Первый вариант решения
```python
class SuperString:
    def __init__(self, string: str):
        self.string = string

    def __str__(self) -> str:
        return f'{self.string}'
    
    def __add__(self, other):
        if isinstance(other, __class__):
            return __class__(self.string + other.string)
        return NotImplemented
    
    def __mul__(self, n):
        if isinstance(n, (int, float)):
            return __class__(self.string * n)
        return NotImplemented
    
    def __rmul__(self, n):
        return self.__mul__(n)
    
    def __truediv__(self, n):
        if isinstance(n, (int, float)):
            return __class__(self.string[:len(self.string) // n])
        return NotImplemented
    
    def __lshift__(self, n):
        if isinstance(n, (int, float)):
           if n >= len(self.string):
                return __class__('')
           elif n == 0:
               return __class__(self.string)
           return __class__(self.string[:-n])
        return NotImplemented
    
    def __rshift__(self, n):
        if isinstance(n, (int, float)):
           if n >= len(self.string):
                return __class__('')
           return __class__(self.string[n:])
        return NotImplemented
```
* Второй вариант решения

```python
class SuperString:
    def __init__(self, string):
        self.string = string

    def __str__(self):
        return self.string

    def __add__(self, other):
        if isinstance(other, SuperString):
            return SuperString(self.string + other.string)
        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, int):
            return SuperString(self.string * other)
        return NotImplemented

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        if isinstance(other, int):
            return SuperString(self.string[:len(self.string) // other])
        return NotImplemented

    def __lshift__(self, other):
        if isinstance(other, int):
            if (length := len(self.string)) <= other:
                return SuperString('')
            else:
                return SuperString(self.string[0:length - other])
        return NotImplemented

    def __rshift__(self, other):
        if isinstance(other, int):
            if len(self.string) <= other:
                return SuperString('')
            else:
                return SuperString(self.string[other:])
        return NotImplemented
```


