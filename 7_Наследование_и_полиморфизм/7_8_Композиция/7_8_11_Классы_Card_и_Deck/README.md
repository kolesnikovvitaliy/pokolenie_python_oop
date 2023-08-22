<h2 style="text-align:center">Классы Card и Deck</h2>


### 1. Реализуйте класс Card, описывающий игральную карту. При создании экземпляра класс должен принимать два аргумента в следующем порядке:

* suit — масть игральной карты, представленная одним из следующих символов:
♣, ♢, ♡, ♠
* rank — ранг игральной карты, представленный одним из следующих символов или парой символов:
2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K, A
#### Экземпляр класса Card должен иметь следующее неформальное строковое представление:

> <масть игральной карты><ранг игральной карты>
### 2. Также реализуйте класс данных Deck, описывающий классическую колоду из 52 игральных карт. Карты в колоде должны быть расположены сперва в порядке возрастания мастей, а затем — в порядке возрастания рангов. При создании экземпляра класс не должен принимать никаких аргументов.

#### Класс Deck должен иметь два метода экземпляра:

* shuffle() — метод, перемешивающий все карты в колоде. Перемешивать колоду можно только в том случае, если в колоде на данный момент находятся все 52 карты. Если в колоде меньше 52 карт, должно быть возбуждено исключение ValueError с текстом:
> Перемешивать можно только полную колоду
* deal() — метод, удаляющий из колоды последнюю карту и возвращающий ее. Если колода пуста, должно быть возбуждено исключение ValueError с текстом:
> Все карты разыграны
#### Экземпляр класса Deck должен иметь следующее неформальное строковое представление:

> Карт в колоде: <текущее количество карт в колоде>
##### Примечание 1. Порядок старшинства карточных рангов от младшего к старшему:

> 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K, A
##### Порядок старшинства карточных мастей от младшего к старшему:

> ♣, ♢, ♡, ♠
##### Примечание 2. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованные классы используются только с корректными данными.

##### Примечание 3. Никаких ограничений касательно реализаций классов нет, они могут быть произвольными.

<table align="center">
  <tbody>
    <tr>
      <th>Sample Input 1: </th>
      <th>Sample Input 2: </th>
      <th>Sample Input 3: </th>
      <th>Sample Input 4: </th>
    </tr>
    <tr>
      <td align="center">print(Card('♣', '4'))<br>
                        print(Card('♡', 'A'))<br>
                        print(Card('♢', '10'))<br></td>
      <td align="center">deck = Deck()<br>
                          print(deck)<br>
                          print(deck.deal())<br>
                          print(deck.deal())<br>
                          print(deck.deal())<br>
                          print(type(deck.deal()))<br>
                          print(deck)<br></td>
      <td align="center">deck = Deck()<br>
                        for _ in range(52):<br>
                            deck.deal()<br>
                        try:<br>
                            deck.deal()<br>
                        except ValueError as error:<br>
                            print(error)<br></td>
      <td align="center">deck = Deck()<br>
                          deck.deal()<br>
                          try:<br>
                              deck.shuffle()<br>
                          except ValueError as error:<br>
                              print(error)<br></td>
    </tr>
    <tr>
      <td>Sample Output 1:</td>
      <td>Sample Output 2:</td>
      <td>Sample Output 3:</td>
      <td>Sample Output 4:</td>
      </tr>
    <tr>
      <td align="center">
                        ♣4<br>
                        ♡A<br>
                        ♢10<br>
      </td>
      <td align="center">
                        Карт в колоде: 52<br>
                        ♠A<br>
                        ♠K<br>
                        ♠Q<br>
                        class '__main__.Card'<br>
                        Карт в колоде: 48<br>
      </td>
      <td align="center">
                        Все карты разыграны<br>
      </td>
      <td align="center">
                        Перемешивать можно только полную колоду<br>
      </td>
    </tr>
  </tbody>
</table>



## Примеры решений:
* Первый вариант решения
```python
from random import shuffle


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f'{self.suit}{self.rank}'


class Deck:
    def __init__(self):
        self.sum_card = 52
        self.__card = self.__card()

    @staticmethod
    def __card():
        _card = [f'{i}{j}' for i in ['♣', '♢', '♡', '♠']for j in
                 [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']]
        return _card

    def shuffle(self):
        if self.sum_card == 52:
            return shuffle(self.__card)
        raise ValueError('Перемешивать можно только полную колоду')

    def deal(self):
        if self.__card:
            self.sum_card -= 1
            last_card = self.__card.pop()
            suit = last_card[0]
            rank = last_card[1:]
            return Card(suit, rank)

        raise ValueError('Все карты разыграны')

    def __str__(self):
        return f'Карт в колоде: {self.sum_card}'
```
* Второй вариант решения

```python
from random import shuffle


class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __str__(self):
        return f'{self.suit}{self.value}'


class Deck:
    def __init__(self):
        suits = ['♣', '♢', '♡', '♠']
        values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        self.cards = [Card(suit, value) for suit in suits for value in values]

    def __str__(self):
        return f'Карт в колоде: {len(self.cards)}'

    def shuffle(self):
        if len(self.cards) < 52:
            raise ValueError('Перемешивать можно только полную колоду')
        shuffle(self.cards)
        return self

    def deal(self):
        if not self.cards:
            raise ValueError('Все карты разыграны')
        return self.cards.pop()
```


