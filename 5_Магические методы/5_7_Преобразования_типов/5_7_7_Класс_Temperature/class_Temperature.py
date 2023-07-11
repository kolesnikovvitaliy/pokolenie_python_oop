''' Первый вариант решения'''
class Temperature:
    def __init__(self, temperature):
        self.temperature = temperature

    def __str__(self) -> str:
        return f"{round(self.temperature,2)}°C"

    def to_fahrenheit(self):
        return self.temperature * (9/5) + 32

    @classmethod    
    def from_fahrenheit(cls, fahrenheit):
        temperature = ((5/9) * (fahrenheit - 32))
        return cls(temperature)

    def __bool__(self):
        return self.temperature > 0

    def __int__(self):
        return int(self.temperature)
    
    def __float__(self):
        return float(self.temperature)
''' Второй вариант решения'''    
# class Temperature:
#     def __init__(self, temperature):
#         self.temperature = temperature

#     def to_fahrenheit(self):
#         return self.temperature * 1.8 + 32

#     def __str__(self):
#         return f'{self.temperature.__round__(2)}°C'

#     def __bool__(self):
#         return self.temperature > 0

#     def __int__(self):
#         return int(self.temperature)

#     def __float__(self):
#         return float(self.temperature)

#     @classmethod
#     def from_fahrenheit(cls, value):
#         celsius = (5 / 9) * (value - 32)
#         return cls(celsius)