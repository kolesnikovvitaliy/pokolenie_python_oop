<h2 style="text-align:center">Скобочная последовательность</h2>

#### Назовем скобочной последовательностью строку, состоящую из символов ( и ). Будем считать скобочную последовательность правильной, если:
* для каждой открывающей скобки есть закрывающая скобка 
* скобки закрываются в правильном порядке, то есть в каждой паре из открывающей и закрывающей скобок открывающая находится левее
#### Напишите программу, которая определяет, является ли скобочная последовательность правильной.

### Формат входных данных
#### На вход программе подается строка, представляющая собой скобочную последовательность.

### Формат выходных данных
#### Программа должна вывести True, если введенная скобочная последовательность является правильной, или False в противном случае.



<table align="center">
  <tbody>
    <tr>
      <th>Sample Input 3: </th>
      <th>Sample Input 4: </th>
      <th>Sample Input 5:</th>
    </tr>
    <tr>
      <td align="center">()()()</td>
      <td align="center">(())</td>
      <td align="center">(()))</td>
    </tr>
    <tr>
      <td>Sample Output 3:</td>
      <td>Sample Output 4:</td>
      <td>Sample Output 5:</td>
    </tr>
    <tr>
      <td align="center">
      True<br>
      </td>
      <td align="center">
      True<br>
      </td>
      <td align="center">
      False<br>
      </td>
    </tr>
  </tbody>
</table>

## Примеры решений:
* Первый вариант решения
```python
def is_correct_bracket(text):
    while '()' in text:
        text = text.replace('()', '')
    return not text

# считываем данные
txt = input()

# вызываем функцию
print(is_correct_bracket(txt))
```
* Второй вариант решения
```python
def is_correct_bracket_sequence(sequence):
    count = 0
    for char in sequence:
        count = count + 1 if char == '(' else count - 1
        if count < 0:
            return False
    return count == 0

print(is_correct_bracket_sequence(input()))
```


