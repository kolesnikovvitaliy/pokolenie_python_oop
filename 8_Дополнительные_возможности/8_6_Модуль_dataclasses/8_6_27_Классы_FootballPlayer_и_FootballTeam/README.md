<h2 style="text-align:center">Классы FootballPlayer и FootballTeam</h2>

### 1. Реализуйте класс данных FootballPlayer, описывающий футбольного игрока. При создании экземпляра класса должен принимать три аргумента в следующем порядке:

* name — имя футболиста (тип str)
* surname — фамилия футболиста (тип str)
* value — рыночная стоимость футболиста в евро (тип int)
#### Экземпляр класса FootballPlayer должен иметь три атрибута:

* name — имя футболиста
* surname — фамилия футболиста
* value — рыночная стоимость футболиста в евро
#### Также экземпляр класса FootballPlayer должен иметь следующее формальное строковое представление:

> FootballPlayer(name='<имя футболиста>', surname='<фамилия футболиста>')
#### Наконец, экземпляры класса FootballPlayer должны поддерживать между собой все операции сравнения с помощью операторов ==, !=, >, <, >=, <=. Два футболиста считаются равными, если их рыночные стоимости совпадают. Футболист считается больше другого футболиста, если его рыночная стоимость больше.

### 2. Реализуйте класс данных FootballTeam, описывающий футбольную команду. При создании экземпляра класса должен принимать один аргумент:

* name — название команды (тип str)
#### Экземпляр класса FootballTeam должен иметь два атрибута:

* name — название команды (тип str)
* players — изначально пустой список, содержащий игроков команды (тип list)
#### Класс FootballTeam должен иметь один метод экземпляра:

* add_players() — метод, принимающий произвольное количество позиционных аргументов, каждый из которых представляет футболиста, и добавляющий их в команду
#### Также экземпляр класса FootballTeam должен иметь следующее формальное строковое представление:

> FootballTeam(name='<название футбольной команды>')
#### Наконец, экземпляры класса FootballTeam должны поддерживать между собой операции сравнения с помощью операторов == и !=. Две футбольные команды считаются равными, если их названия совпадают.

##### Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованные классы используются только с корректными данными.

##### Примечание 2. Никаких ограничений касательно реализаций классов нет, они могут быть произвольными.

<table align="center">
  <tbody>
    <tr>
      <th>Sample Input 1: </th>
      <th>Sample Input 2: </th>
      <th>Sample Input 3: </th>
      <th>Sample Input 4: </th>
    </tr>
    <tr>
      <td align="center">player = FootballPlayer('Kylian', 'Mbappe', 180000000)<br>
                          print(player)<br>
                          print(player.name)<br>
                          print(player.surname)<br>
                          print(player.value)<br></td>
      <td align="center">player1 = FootballPlayer('Jude', 'Bellingham', 120000000)<br>
                          player2 = FootballPlayer('Vinicius', 'Junior', 120000000)<br>
                          player3 = FootballPlayer('Kylian', 'Mbappe', 180000000)<br>
                          print(player1 == player2)<br>
                          print(player1 == player3)<br>
                          print(player1 > player3)<br>
                          print(player1 < player3)<br></td>
      <td align="center">team = FootballTeam('PSG')<br>
                          print(team)<br>
                          print(team.name)<br>
                          print(team.players)<br>
                          team.add_players(FootballPlayer('Kylian', 'Mbappe', 180000000))<br>
                          print(team.players)<br></td>
      <td align="center">team1 = FootballTeam('PSG')<br>
                          team2 = FootballTeam('PSG')<br>
                          team3 = FootballTeam('Arsenal')<br>
                          print(team1 == team2)<br>
                          print(team1 != team2)<br>
                          print(team1 == team3)<br>
                          print(team1 != team3)<br></td>
    </tr>
    <tr>
      <td>Sample Output 1:</td>
      <td>Sample Output 2:</td>
      <td>Sample Output 3:</td>
      <td>Sample Output 4:</td>
      </tr>
    <tr>
      <td align="center">
                        FootballPlayer(name='Kylian', surname='Mbappe')<br>
                        Kylian<br>
                        Mbappe<br>
                        180000000<br>
      </td>
      <td align="center">
                        True<br>
                        False<br>
                        False<br>
                        True<br>
      </td>
      <td align="center">
                        FootballTeam(name='PSG')<br>
                        PSG<br>
                        []<br>
                        [FootballPlayer(name='Kylian', surname='Mbappe')]<br>
      </td>
      <td align="center">
                        True<br>
                        False<br>
                        False<br>
                        True<br>
      </td>
    </tr>
  </tbody>
</table>



## Примеры решений:
* Первый вариант решения
```python
from dataclasses import dataclass, field


@dataclass(order=True)
class FootballPlayer:
    name: str = field(compare=False, default='')
    surname: str = field(compare=False, default='')
    value: int = field(repr=False, default=0)


@dataclass
class FootballTeam:
    name: str = field(default='')
    players: list = field(default_factory=list, repr=False)

    def add_players(self, *args):
        for i in args:
            self.players.append(i)
```
* Второй вариант решения

```python
from dataclasses import dataclass, field


@dataclass(order=True)
class FootballPlayer:
    name: str = field(compare=False)
    surname: str = field(compare=False)
    value: int = field(repr=False)


@dataclass
class FootballTeam:
    name: str
    players: list = field(default_factory=list, repr=False, compare=False)

    def add_players(self, *args):
        self.players.extend(args)
```


