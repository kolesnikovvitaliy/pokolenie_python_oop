''' Первый вариант решения'''
class Greeter:
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        print(f"Приветствую, {self.name}!")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print(f"До встречи, {self.name}!")
        return True
''' Второй вариант решения'''    
# class Greeter:
#     def __init__(self, name):
#         self.name = name

#     def __enter__(self):
#         print(f'Приветствую, {self.name}!')
#         return self

#     def __exit__(self, *args, **kwargs):
#         print(f'До встречи, {self.name}!')