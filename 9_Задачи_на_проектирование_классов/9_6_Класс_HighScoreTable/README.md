<h2 style="text-align:center">Класс HighScoreTable</h2>

### Предположим, что у нас имеется некоторая игра. За каждую игровую сессию игрок получает определенное количество баллов в зависимости от своего результата. Вашей задачей является реализация класса HighScoreTable — таблицы рекордов, которую можно будет обновлять с учетом итоговых результатов игрока.

#### Изначально таблица рекордов является пустой. Максимальное количество рекордов указывается при создании таблицы:
```python 
high_score_table = HighScoreTable(3)
```
#### Таблица должна позволять просматривать текущие рекорды и добавлять новые результаты:
```python 
print(high_score_table.scores)    # []
high_score_table.update(10)
high_score_table.update(8)
high_score_table.update(12)
print(high_score_table.scores)    # [12, 10, 8]
```
#### Текущие рекорды всегда должны располагаться в порядке убывания. Так как таблица содержит именно рекорды, то после заполнения таблицы добавляться должны только те результаты, которые лучше текущих:
```python 
high_score_table.update(6)
high_score_table.update(7)
print(high_score_table.scores)    # [12, 10, 8]
high_score_table.update(9)
print(high_score_table.scores)    # [12, 10, 9]
```

#### Таблица должна поддерживать сброс всех результатов:
```python
high_score_table.reset()
print(high_score_table.scores)    # []
```

<table align="center">
  <tbody>
    <tr>
      <th>Sample Input 1: </th>
      <th>Sample Input 2: </th>
    </tr>
    <tr>
      <td align="center">high_score_table = HighScoreTable(3)<br>
                          print(high_score_table.scores)<br>
                          high_score_table.update(10)<br>
                          high_score_table.update(8)<br>
                          high_score_table.update(12)<br>
                          print(high_score_table.scores)<br></td>
      <td align="center">high_score_table = HighScoreTable(3)<br>
                        print(high_score_table.scores)<br>
                        high_score_table.update(10)<br>
                        high_score_table.update(8)<br>
                        high_score_table.update(12)<br>
                        print(high_score_table.scores)<br>
                        high_score_table.update(3)<br>
                        high_score_table.update(6)<br>
                        high_score_table.update(1)<br>
                        print(high_score_table.scores)<br>
                        high_score_table.reset()<br>
                        print(high_score_table.scores)<br></td>
    </tr>
    <tr>
      <td>Sample Output 1:</td>
      <td>Sample Output 2:</td>
      </tr>
    <tr>
      <td align="center">
                        []<br>
                        [12, 10, 8]<br>
      </td>
      <td align="center">
                        []<br>
                        [12, 10, 8]<br>
                        [12, 10, 8]<br>
                        []<br>
      </td>
    </tr>
  </tbody>
</table>



## Примеры решений:
* Первый вариант решения
```python
from dataclasses import dataclass, field


@dataclass
class HighScoreTable:
    _len_list_score: int = field(default=0)
    scores: list = field(default_factory=list[int], repr=False)

    def update(self, res=0):
        if len(self.scores) < self._len_list_score:
            self.scores.append(res)
        else:
            if not min(self.scores) > res:
                self.scores.pop()
                self.scores.append(res)
        self.scores = sorted(self.scores, reverse=True)

    def reset(self):
        self.scores.clear()
```
* Второй вариант решения

```python
class HighScoreTable:
    def __init__(self, limit):
        self._limit = limit
        self.scores = []

    def update(self, score):
        length = len(self.scores)
        for index in range(length):
            if score > self.scores[index]:
                if length == self._limit:
                    self.scores.pop()
                self.scores.insert(index, score)
                break
        else:
            if length < self._limit:
                self.scores.append(score)

    def reset(self):
        self.scores.clear()
```


