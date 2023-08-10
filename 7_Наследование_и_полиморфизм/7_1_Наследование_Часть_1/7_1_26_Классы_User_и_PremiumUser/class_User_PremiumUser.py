''' Первый вариант решения'''
class User:
    def __init__(self, name: str):
        self._name = name

    def skip_ads(self):
        return False


class PremiumUser(User):
    def skip_ads(self):
        return True
''' Второй вариант решения'''    
# class User:
#     def __init__(self, name: str):
#         self._name = name

#     def skip_ads(self):
#         return False


# class PremiumUser(User):
#     def __init__(self, name):
#         super().__init__(name)

#     def skip_ads(self):
#         return True