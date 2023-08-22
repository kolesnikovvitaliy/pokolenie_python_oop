''' Первый вариант решения'''
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
''' Второй вариант решения'''    
# from random import shuffle


# class Card:
#     def __init__(self, suit, value):
#         self.suit = suit
#         self.value = value

#     def __str__(self):
#         return f'{self.suit}{self.value}'


# class Deck:
#     def __init__(self):
#         suits = ['♣', '♢', '♡', '♠']
#         values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
#         self.cards = [Card(suit, value) for suit in suits for value in values]

#     def __str__(self):
#         return f'Карт в колоде: {len(self.cards)}'

#     def shuffle(self):
#         if len(self.cards) < 52:
#             raise ValueError('Перемешивать можно только полную колоду')
#         shuffle(self.cards)
#         return self

#     def deal(self):
#         if not self.cards:
#             raise ValueError('Все карты разыграны')
#         return self.cards.pop()