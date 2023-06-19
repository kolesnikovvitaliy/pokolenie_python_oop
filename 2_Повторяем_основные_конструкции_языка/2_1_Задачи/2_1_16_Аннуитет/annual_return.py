''' Первый вариант решения'''
def annual_return(start, percent, years):
    for i in range(years):
        start = ((start/100) * percent) + start
        yield start 

# for value in annual_return(70000, 8, 10):
#     print(round(value))

''' Второй вариант решения'''    
# from typing import Iterator

# def annual_return(start: int, percentage: int, years: int) -> Iterator:
#     return (start := start * ((percentage + 100) / 100) for _ in range(years))