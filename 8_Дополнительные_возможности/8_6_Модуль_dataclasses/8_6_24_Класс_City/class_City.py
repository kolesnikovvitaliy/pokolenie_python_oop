''' Первый вариант решения'''
from dataclasses import dataclass


@dataclass
class City:
    name: str
    population: int
    founded: int
''' Второй вариант решения'''    
# from dataclasses import make_dataclass

# City = make_dataclass('City', ('name', 'population', 'founded'))