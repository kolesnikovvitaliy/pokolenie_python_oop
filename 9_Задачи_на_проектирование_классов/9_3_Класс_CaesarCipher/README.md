<h2 style="text-align:center">Класс CaesarCipher</h2>

### Реализуйте класс CaesarCipher для шифровки и дешифровки текста с помощью шифра Цезаря. При создании экземпляра класса CaesarCipher должен указываться сдвиг, который будет использоваться при шифровке и дешифровке. За операцию шифрования должен отвечать метод encode(), за операцию дешифрования — decode():

```python
cipher = CaesarCipher(5)

print(cipher.encode('Beegeek'))      # Gjjljjp
print(cipher.decode('Gjjljjp'))      # Beegeek
```
#### Обратите внимание, что при шифровке сдвиг должен происходить вправо, также заметьте, что регистр букв при шифровке и дешифровке должен сохраняться.

#### Шифровке и дешифровке должны подвергаться только буквы латинского алфавита, все остальные символы, если они присутствуют, должны оставаться неизменными:
```python 
print(cipher.encode('Биgeek123'))    # Биljjp123
print(cipher.decode('Биljjp123'))    # Биgeek123
```
##### Примечание 1. Гарантируется, что сдвигом является число из диапазона [1; 26].

<table align="center">
  <tbody>
    <tr>
      <th>Sample Input 1: </th>
      <th>Sample Input 2: </th>
    </tr>
    <tr>
      <td align="center">cipher = CaesarCipher(10)<br>
                          print(cipher.encode('Beegeek'))<br>
                          print(cipher.decode('Gjjljjp'))<br></td>
      <td align="center">cipher = CaesarCipher(5)<br>
                          print(cipher.encode('Биgeek123'))<br>
                          print(cipher.decode('Биljjp123'))<br></td>
    </tr>
    <tr>
      <td>Sample Output 1:</td>
      <td>Sample Output 2:</td>
      </tr>
    <tr>
      <td align="center">
                        Looqoou<br>
                        Wzzbzzf<br>
      </td>
      <td align="center">
                        Биljjp123<br>
                        Биgeek123<br>
      </td>
    </tr>
  </tbody>
</table>



## Примеры решений:
* Первый вариант решения
```python
class CaesarCipher:
    def __init__(self, shift):
        self.shift = shift

    def encode(self, letter, code=1):
        _text = ''
        __ex = self.shift * code
        for i in letter:
            a, b = (97, 122) if i.isalpha() and i.lower() == i else (65, 90)
            if ord(i) in range(a, b+1):
                if (ord(i) + __ex) > b:
                    i = chr(((ord(i) + __ex) - b) + a - 1)
                    _text += i
                elif (ord(i) + __ex) < a:
                    i = chr(b - (a - (ord(i) + __ex + 1)))
                    _text += i
                else:
                    i = chr(ord(i) + __ex)
                    _text += i
            else:
                _text += i
        return _text

    def decode(self, letter):
        return self.encode(letter, -1)
```
* Второй вариант решения

```python
from re import search, I

class CaesarCipher:
    def __init__(self: object, n: int) -> None:
        self.n = n
        
    def encode(self: object, string: str, code: int|bool = True) -> str:
        new_str, n = '', code * self.n
        for i in string:
            if search(r'[a-z]', i, I):
                x = [65, 97][i.lower() == i]
                i = chr((ord(i) + n - x) % 26 + x)
            new_str += i
        return new_str
    
    def decode(self: object, string: str) -> str:
        return self.encode(string, -1)

```


