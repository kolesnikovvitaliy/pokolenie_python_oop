<h2 style="text-align:center">Класс MutableString</h2>


### Реализуйте класс MutableString, описывающий изменяемую строку. При создании экземпляра класс должен принимать один аргумент:
* string — строка, определяющая начальное значение изменяемой строки. Если не передана, строка считается пустой
#### Класс MutableString должен иметь два метода экземпляра:
* lower() — метод, переводящий все символы изменяемой строки в нижний регистр
* upper() — метод, переводящий все символы изменяемой строки в верхний регистр
#### Экземпляр класса MutableString должен иметь неформальное строковое представление в следующем виде:
> <текущее значение изменяемой строки>
#### Также экземпляр класса MutableString должен иметь формальное строковое представление в следующем виде:
> MutableString('<текущее значение изменяемой строки>')
#### При передаче экземпляра класса MutableString в функцию len() должно возвращаться количество символов в нем.
#### Помимо этого, экземпляр класса MutableString должен быть итерируемым объектом, то есть позволять перебирать свои символы, например, с помощью цикла for.
#### Также экземпляр класса MutableString должен позволять получать, изменять и удалять значения своих элементов с помощью индексов, причем как положительных, так и отрицательных. Экземпляр класса MutableString должен поддерживать полноценные срезы, результатами которых должны быть новые изменяемые строки.
#### Наконец, экземпляры класса MutableString должны поддерживать между собой операцию сложения с помощью оператора +, результатом которой должен являться новый экземпляр класса MutableString, представляющий конкатенацию исходных.

##### Примечание 1. Реализация класса MutableString может быть произвольной, то есть требований к наличию определенных атрибутов нет.
##### Примечание 2. Дополнительная проверка данных на корректность в методах не требуется. Гарантируется, что реализованный класс используется только с корректными данными.

<table align="center">
  <tbody>
    <tr>
      <th>Sample Input 1: </th>
      <th>Sample Input 2: </th>
      <th>Sample Input 3: </th>
      <th>Sample Input 4: </th>
    </tr>
    <tr>
      <td align="center">mutablestring = MutableString('beegeek')<br>
                        print(*mutablestring)<br>
                        print(str(mutablestring))<br>
                        print(repr(mutablestring))<br></td>
      <td align="center">mutablestring = MutableString('Beegeek')<br>
                          mutablestring.lower()<br>
                          print(mutablestring)<br>
                          mutablestring.upper()<br>
                          print(mutablestring)<br></td>
      <td align="center">mutablestring1 = MutableString('bee')<br>
                        mutablestring2 = MutableString('geek')<br>
                        print(mutablestring1 + mutablestring2)<br>
                        print(mutablestring2 + mutablestring1)<br></td>
      <td align="center">mutablestring = MutableString('beegeek')<br>
                        print(mutablestring)<br>
                        mutablestring[0] = 'B'<br>
                        mutablestring[-4] = 'G'<br>
                        print(mutablestring)<br></td>
    </tr>
    <tr>
      <td>Sample Output 1:</td>
      <td>Sample Output 2:</td>
      <td>Sample Output 3:</td>
      <td>Sample Output 4:</td>
      </tr>
    <tr>
      <td align="center">
                        b e e g e e k<br>
                        beegeek<br>
                        MutableString('beegeek')<br>
      </td>
      <td align="center">
                        beegeek<br>
                        BEEGEEK<br>
      </td>
      <td align="center">
                        beegeek<br>
                        geekbee<br>
      </td>
      <td align="center">
                        beegeek<br>
                        BeeGeek<br>
      </td>
    </tr>
  </tbody>
</table>



## Примеры решений:
* Первый вариант решения
```python
class MutableString:
    def __init__(self, string=''):
        self._string = string or ''

    
    def lower(self):
        self._string = self._string.lower()

    def upper(self):
        self._string = self._string.upper()

    def __str__(self):
        return f"{self._string}"
    
    def __repr__(self):
        return f"{__class__.__name__}('{self._string}')"
    
    def __len__(self):
        return len(self._string)
    
    def __iter__(self):
        yield from self._string

    def __setitem__(self, key, value):
            __str = [*self._string]
            __str[key] = value
            self._string = ''.join(__str)

    def __getitem__(self, key):
        if isinstance(key, slice):
            return __class__(self._string[key])
        return self._string[key]
    
    def __delitem__(self, key):
        __str = [*self._string]
        del __str[key]
        self._string = ''.join(__str)

    def __add__(self, other):
        return __class__(self._string + other._string)
```
* Второй вариант решения

```python
class MutableString:
    def __init__(self, string=''):
        self.string = string
        
    def __str__(self):
        return self.string
    
    def __repr__(self):
        return f"MutableString('{self.string}')"
    
    def __len__(self):
        return len(self.string)
    
    def __iter__(self):
        yield from self.string
        
    def __add__(self, other):
        return MutableString(self.string+other.string)
    
    def lower(self):
        self.string = self.string.lower()

    def upper(self):
        self.string = self.string.upper()
        
    def __getitem__(self, key):
        if isinstance(key, slice):
            return MutableString(self.string[key])
        return self.string[key]
        
    def __setitem__(self, key, value):
        self.string = self.string.replace(self.string[key], value)
        
    def __delitem__(self, key):
        self.string = self.string.replace(self.string[key], '') 
```


