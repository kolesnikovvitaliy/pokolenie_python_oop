''' Первый вариант решения'''
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
''' Второй вариант решения'''    
# from dataclasses import dataclass, field


# @dataclass(order=True)
# class FootballPlayer:
#     name: str = field(compare=False)
#     surname: str = field(compare=False)
#     value: int = field(repr=False)


# @dataclass
# class FootballTeam:
#     name: str
#     players: list = field(default_factory=list, repr=False, compare=False)

#     def add_players(self, *args):
#         self.players.extend(args)