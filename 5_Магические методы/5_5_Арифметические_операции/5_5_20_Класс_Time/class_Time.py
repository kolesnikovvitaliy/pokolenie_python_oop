''' Первый вариант решения'''
from datetime import time


class Time:
    def __init__(self, hours, minutes):
        __time = (hours%24,*divmod(minutes,60))
        self.hours, self.minutes = (__time[0]+__time[1],__time[2])
    
    def __add__(self, other):
        if isinstance(other, __class__):
            h, m = map(sum, zip((self.hours, self.minutes), (other.hours, other.minutes)))
            return __class__(h, m)
        return NotImplemented
    
    def __iadd__(self, other):
        if isinstance(other, __class__):
            self.hours += other.hours 
            self.minutes += other.minutes
            return self
        return NotImplemented
    
    def __str__(self) -> str:
        __time = (self.hours%24,*divmod(self.minutes,60))
        hours, minutes = (__time[0]+__time[1],__time[2])
        return f"{time(hours, minutes).strftime('%H:%M')}"
''' Второй вариант решения'''    
# class Time:
#     def __init__(self, hours, minutes):
#         self.hours, self.minutes = Time._normalize(hours, minutes)

#     @staticmethod
#     def _normalize(hours, minutes):
#         return (hours + minutes // 60) % 24, minutes % 60

#     def __str__(self):
#         return f'{self.hours:>02}:{self.minutes:>02}'

#     def __add__(self, other):
#         if isinstance(other, Time):
#             hours, minutes = self._normalize(self.hours + other.hours, self.minutes + other.minutes)
#             return Time(hours, minutes)
#         return NotImplemented

#     def __iadd__(self, other):
#         if isinstance(other, Time):
#             self.hours, self.minutes = self._normalize(self.hours + other.hours, self.minutes + other.minutes)
#             return self
#         return NotImplemented