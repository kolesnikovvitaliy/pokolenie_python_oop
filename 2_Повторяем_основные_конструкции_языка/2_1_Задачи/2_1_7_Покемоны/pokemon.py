''' Первый вариан решения '''

import sys 
pokemons = [pokemon.strip() for pokemon in sys.stdin]
print(len(pokemons) - len(set(pokemons)))

''' Второй вариант решения'''
p_list = [i.strip() for i in __import__('sys').stdin]
print(len(p_list) - len(set(p_list)))