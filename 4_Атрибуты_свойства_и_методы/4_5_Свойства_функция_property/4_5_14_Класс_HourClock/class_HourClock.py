''' Первый вариант решения'''
class HourClock:
    def __init__(self, hours):
        self.hours = hours

    def set_hours(self, hours):
        if isinstance(hours, int) and hours in range(1,13):
            self._hours = hours
        else:
            raise ValueError('Некорректное время')
    
    def get_hours(self):
        return self._hours
    
    hours = property(get_hours, set_hours)
''' Второй вариант решения'''    
# class HourClock:

#     def __init__(self, hours):
#         self.hours = hours

#     @property
#     def hours(self):
#         return self._hours

#     @hours.setter
#     def hours(self, hours):
#         if not isinstance(hours, int) or hours not in range(1,13):
#             raise ValueError('Некорректное время')
#         self._hours = hours