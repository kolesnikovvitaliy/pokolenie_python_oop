<h2 style="text-align:center">Класс_ReversedSequence</h2>


### Реализуйте класс ReversedSequence, описывающий объект, который реализует доступ к элементам некоторой последовательности в обратном порядке. При создании экземпляра класс должен принимать один аргумент:
* sequence — последовательность
#### При передаче экземпляра класса ReversedSequence в функцию len() должна возвращаться его длина, представленная количеством элементов в исходной последовательности.
#### Также экземпляр класса ReversedSequence должен быть итерируемым объектом, элементами которого являются элементы исходной последовательности в обратном порядке.
#### Наконец, экземпляр класса ReversedSequence должен позволять получать значения элементов исходной последовательности с помощью индексов, при этом индексация должна производиться в обратном порядке, то есть по индексу 0 должен быть доступен последний элемент исходной последовательности, по индексу 1 — предпоследний элемент, по индексу 2 — предпредпоследний элемент, и так далее.

##### Примечание 1. Гарантируется, что при доступе к элементам используются только неотрицательные индексы.
##### Примечание 2. Экземпляр класса ReversedSequence должен зависеть от последовательности, на основе которой он был создан. Другими словами, если исходная последовательность изменится, то должен измениться и экземпляр класса ReversedSequence.
##### Примечание 3. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.
##### Примечание 4. Никаких ограничений касательно реализации класса ReversedSequence нет, она может быть произвольной.

<table align="center">
  <tbody>
    <tr>
      <th>Sample Input 1: </th>
      <th>Sample Input 2: </th>
      <th>Sample Input 3: </th>
    </tr>
    <tr>
      <td align="center">reversed_list = ReversedSequence([1, 2, 3, 4, 5])<br>
                          print(reversed_list[0])<br>
                          print(reversed_list[1])<br>
                          print(reversed_list[2])<br></td>
      <td align="center">numbers = [1, 2, 3, 4, 5]<br>
                          reversed_numbers = ReversedSequence(numbers)<br>
                          print(reversed_numbers[0])<br>
                          numbers.append(6)<br>
                          print(reversed_numbers[0])<br></td>
      <td align="center">numbers = [1, 2, 3, 4, 5]<br>
                          reversed_numbers = ReversedSequence(numbers)<br>
                          print(len(reversed_numbers))<br>
                          numbers.append(6)<br>
                          numbers.append(7)<br>
                          print(len(reversed_numbers))<br></td>
    </tr>
    <tr>
      <td>Sample Output 1:</td>
      <td>Sample Output 2:</td>
      <td>Sample Output 3:</td>
      </tr>
    <tr>
      <td align="center">
                        5<br>
                        4<br>
                        3<br>
      </td>
      <td align="center">
                        5<br>
                        6<br>
      </td>
      <td align="center">
                        5<br>
                        7<br>
      </td>
    </tr>
  </tbody>
</table>



## Примеры решений:
* Первый вариант решения
```python
class ReversedSequence:
    def __init__(self, sequence):
        self.sequence = sequence

    def __getitem__(self, key):
        return list(reversed(self.sequence))[key]     

    def __iter__(self):
        yield from reversed(self.sequence)

    def __len__(self):
        return len(self.sequence)
    
    def __reversed__(self):
        return self.sequence
```
* Второй вариант решения

```python
class ReversedSequence:
    def __init__(self, sequence):
        self.sequence = sequence

    def __len__(self):
        return len(self.sequence)

    def __getitem__(self, key):
        return self.sequence[~key]

    def __iter__(self):
        yield from reversed(self.sequence)
```


