<h2 style="text-align:center">Класс City</h2>

### Вам доступен класс City, описывающий город. При создании экземпляра класс принимает три аргумента в следующем порядке:

* name — название города (тип str)
* population — население города (тип int)
* founded — год основания города (тип int)
#### Экземпляр класса City имеет три атрибута:

* name — название города
* population — население города
* founded — год основания города
#### Также экземпляр класса City имеет следующее формальное строковое представление:

> City(name='<название города>', population=<население города>, founded=<год основания города>)
#### Наконец, экземпляры класса City поддерживают между собой операцию сравнения с помощью операторов == и!=. Два города считаются равными, если их названия, население и годы основания совпадают.

#### Реализуйте класс City в виде класса данных.
```python 
class City:
    def __init__(self, name, population, founded):
        self.name = name
        self.population = population
        self.founded = founded

    def __repr__(self):
        return f"City(name='{self.name}', population={self.population}, founded={self.founded})"

    def __eq__(self, other):
        if isinstance(other, City):
            return (self.name, self.population, self.founded) == (other.name, other.population, other.founded)
        return NotImplemented
```

##### Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.

##### Примечание 2. Никаких ограничений касательно реализации класса City нет, она может быть произвольной.

<table align="center">
  <tbody>
    <tr>
      <th>Sample Input 1: </th>
      <th>Sample Input 2: </th>
    </tr>
    <tr>
      <td align="center">city = City('Tokyo', 14043239, 1457)<br>
                          print(city)<br>
                          print(city.name)<br>
                          print(city.population)<br>
                          print(city.founded)<br></td>
      <td align="center">city1 = City('Tokyo', 14043239, 1457)<br>
                          city2 = City('New York', 8467513, 1624)<br>
                          city3 = City('Tokyo', 14043239, 1457)<br>
                          print(city1 == city2)<br>
                          print(city1 != city2)<br>
                          print(city1 == city3)<br>
                          print(city1 != city3)<br></td>
    </tr>
    <tr>
      <td>Sample Output 1:</td>
      <td>Sample Output 2:</td>
      </tr>
    <tr>
      <td align="center">
                        City(name='Tokyo', population=14043239, founded=1457)<br>
                        Tokyo<br>
                        14043239<br>
                        1457<br>
      </td>
      <td align="center">
                        False<br>
                        True<br>
                        True<br>
                        False<br>
      </td>
    </tr>
  </tbody>
</table>



## Примеры решений:
* Первый вариант решения
```python
from dataclasses import dataclass


@dataclass
class City:
    name: str
    population: int
    founded: int
```
* Второй вариант решения

```python
from dataclasses import make_dataclass

City = make_dataclass('City', ('name', 'population', 'founded'))
```


