''' Первый вариант решения'''
from dataclasses import dataclass, field


@dataclass(frozen=True)
class MusicAlbum:
    title: str
    artist: str
    genre: str = field(repr=False, compare=False)
    year: int = field(repr=False)
''' Второй вариант решения'''    
# from dataclasses import dataclass, field


# @dataclass(frozen=True)
# class MusicAlbum:
#     title: str
#     artist: str
#     genre: str = field(repr=False, compare=False)
#     year: int = field(repr=False)