<h2 style="text-align:center">Покемоны</h2>


### Артур владеет небольшой коллекцией карточек с покемонами, среди которых встречаются дубликаты. Он хочет оставить по одной карточке каждого типа, а остальные продать.


#### Напишите программу, которая определяет, сколько дубликатов из своей коллекции Артур может продать.
#### Формат входных данных:
#####  На вход программе подается произвольное количество строк, которые представляют коллекцию карточек с покемонами. В каждой строке указывается имя покемона с карточки.
#### Формат выходных данных:
##### Программа должна вывести единственное число — количество карточек, которые из данной коллекции можно продать, чтобы оставить по одной карточке каждого типа.
##### Примечание 1. Рассмотрим первый тест. Чтобы оставить по одной карточке каждого типа, достаточно продать две карточки Pichu и одну карточку Tyrogue.
##### 




<table align="center">
  <tbody>
    <tr>
      <th>Sample Input 1: </th>
      <th>Sample Input 2: </th>
      <th>Sample Input 3:</th>
    </tr>
    <tr>
      <td align="center">Pichu<br>
            Pichu<br>
            Tyrogue<br>
            Pichu<br>
            Combee<br>
            Marill<br>
            Tyrogue<br></td>
      <td align="center">Tyrogue<br>
            Pichu<br>
            Combee<br></td>
      <td align="center">Combee<br>
            Combee<br>
            Marill<br>
            Marill<br>
            Pichu<br>
            Pichu<br>
            Tyrogue<br>
            Tyrogue<br>
            </td>
    </tr>
    <tr>
      <td>Sample Output 1:</td>
      <td>Sample Output 2:</td>
      <td>Sample Output 3:</td>
    </tr>
    <tr>
      <td align="center">
      3<br>
      </td>
      <td align="center">
      0<br>
      </td>
      <td align="center">
      4<br>
      </td>
    </tr>
  </tbody>
</table>

## Примеры решений:
* Первый вариант решения
```python
import sys 
pokemons = [pokemon.strip() for pokemon in sys.stdin]
print(len(pokemons) - len(set(pokemons)))
```
* Второй вариант решения
```python
p_list = [i.strip() for i in __import__('sys').stdin]
print(len(p_list) - len(set(p_list)))
```


