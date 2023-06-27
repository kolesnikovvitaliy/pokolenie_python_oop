<h2 style="text-align:center">Класс Color</h2>

### Для кодирования цвета часто используется шестнадцатеричное значение цвета. Оно записывается в формате #RRGGBB, где RR (красный), GG (зеленый) и BB (синий) являются шестнадцатеричными целыми числами в диапазоне [00; FF] (или [0; 255] в десятичной системе счисления), которые указывают интенсивность соответствующих цветов. Например, #0000FF представляет чистый синий цвет, так как синий компонент имеет наивысшее значение (FF), а остальные — 00.
### Реализуйте класс Color, описывающий цвет. При создании экземпляра класс должен принимать один аргумент:
* hexcode — шестнадцатеричное значение цвета 
#### Экземпляр класса Color должен иметь три атрибута:
* r — интенсивность красного компонента цвета в виде десятичного числа
* g — интенсивность зеленого компонента цвета в виде десятичного числа
* b — интенсивность синего компонента цвета в виде десятичного числа
#### Класс Color должен иметь одно свойство:
* hexcode — свойство, доступное для чтения и записи, возвращающее шестнадцатеричное значение цвета

##### Примечание 1. При изменении шестнадцатеричного значения цвета значения атрибутов r, g и b также должны изменяться.
##### Примечание 2. Гарантируется, что для записи шестнадцатеричных чисел используются только заглавные латинские буквы.
##### Примечание 3. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.
##### Примечание 4. Никаких ограничений касательно реализации класса Color нет, она может быть произвольной.

<table align="center">
  <tbody>
    <tr>
      <th>Sample Input 1: </th>
      <th>Sample Input 2: </th>
    </tr>
    <tr>
      <td align="center">color = Color('0000FF')<br>
                        print(color.hexcode)<br>
                        print(color.r)<br>
                        print(color.g)<br>
                        print(color.b)<br></td>
      <td align="center">color = Color('0000FF')<br>
                          color.hexcode = 'A782E3'<br>
                          print(color.hexcode)<br>
                          print(color.r)<br>
                          print(color.g)<br>
                          print(color.b)<br></td>
    </tr>
    <tr>
      <td>Sample Output 1:</td>
      <td>Sample Output 2:</td>
      </tr>
    <tr>
      <td align="center">
                        0000FF<br>
                        0<br>
                        0<br>
                        255<br>
      </td>
      <td align="center">
                        A782E3<br>
                        167<br>
                        130<br>
                        227<br>
      </td>
    </tr>
  </tbody>
</table>



## Примеры решений:
* Первый вариант решения
```python
class Color:
    def __init__(self, hexcode):
        self.hexcode = hexcode
        
    @property    
    def hexcode(self):
        return self._hexcode
    
    @hexcode.setter
    def hexcode(self, hexcode):
        self._hexcode = hexcode
        self.r, self.g, self.b = int(hexcode[:2], 16),  int(hexcode[2:4], 16),  int(hexcode[4:], 16)
```
* Второй вариант решения

```python
class Color:
    def __init__(self, hexcode: str) -> None:
        self.hexcode = hexcode

    @property
    def hexcode(self) -> str:
        return self._hexcode
    
    @hexcode.setter
    def hexcode(self, stroke: str) -> None:
        self._hexcode = stroke
        self.r, self.g, self.b = (int(stroke[i:i+2], base=16) 
                                  for i in range(0,6,2))
```


