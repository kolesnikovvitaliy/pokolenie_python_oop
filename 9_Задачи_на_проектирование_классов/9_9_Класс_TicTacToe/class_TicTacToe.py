''' Первый вариант решения'''
class TicTacToe:
    def __init__(self):
        self.tic = [[' ' for i in range(3)] for j in range(3)]
        self.count = 0
        self.flag = None

    def mark(self, i: int, j: int):
        self.flag = self.winner()

        if self.flag:
            print('Игра окончена')
            return

        if self.tic[i-1][j-1] != ' ':
            print('Недоступная клетка')
            return
        else:
            if self.count % 2 == 0:
                self.tic[i-1][j-1] = 'X'
                self.count += 1
            else:
                self.tic[i-1][j-1] = 'O'
                self.count += 1

    def chec_win(self, items: list):
        if ' ' in items:
            return
        elif all(map(lambda x: x == items[0], items)):
            return items[0]
        return

    def win(self):
        tasks = ('self.tic[i][j]', 'self.tic[j][i]',
                 'self.tic[j][j]', 'self.tic[j][-1-j]')
        flag = None
        item = []
        for k in tasks:
            for i in range(3):
                for j in range(3):
                    item.append(eval(k))
                    if len(item) == 3:
                        flag = self.chec_win(item)
                        if flag:
                            return flag
                        else:
                            item.clear()
        return flag

    def winner(self):
        flag = self.win()
        _lst = [j for i in self.tic for j in i]

        if ' ' not in _lst and not flag:
            return 'Ничья'

        if not flag:
            return
        return flag

    def show(self):
        _lst = [['|'.join(i)] for i in self.tic]
        for k, v in enumerate(_lst):
            if k < len(_lst)-1:
                print(*v, end='\n-----\n')
            else:
                print(*v)
''' Второй вариант решения'''    
# class TicTacToe:
#     def __init__(self):
#         self._game_field = [[' ' for _ in range(3)] for _ in range(3)]
#         self._player = 'X'
#         self._move = 0

#     def _is_win(self, mark):
#         if any((
#                 any(([mark, mark, mark] == self._game_field[r]) for r in range(3)),
#                 any(((mark, mark, mark) == list(zip(*self._game_field))[r]) for r in range(3)),
#                 all((mark == self._game_field[r][r]) for r in range(3)),
#                 all((mark == self._game_field[r][-r - 1]) for r in range(3)),
#         )):
#             return True
#         return None

#     def winner(self):
#         for mark in 'XO':
#             if self._is_win(mark):
#                 return mark
#         if self._move >= 9:
#             return 'Ничья'
#         return None

#     def mark(self, r, c):
#         if self.winner() or self._move >= 9:
#             print('Игра окончена')
#         elif self._game_field[r - 1][c - 1] != ' ':
#             print('Недоступная клетка')
#         else:
#             self._move += 1
#             self._game_field[r - 1][c - 1] = self._player
#             self._player = ['X', 'O'][self._move % 2]

#     def show(self):
#         field = ['|'.join(self._game_field[r]) for r in range(3)]
#         print(*('\n-----\n'.join(field)), sep='')