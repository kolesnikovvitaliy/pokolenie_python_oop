<h2 style="text-align:center">Класс MusicAlbum</h2>

### Реализуйте неизменяемый класс MusicAlbum, описывающий музыкальный альбом. При создании экземпляра класс должен принимать четыре аргумента в следующем порядке:

* title — название альбома (тип str)
* artist — автор альбома (тип str)
* genre — жанр альбома (тип str)
* year — год выпуска альбома (тип int)
#### Экземпляр класса MusicAlbum должен иметь четыре атрибута:

* title — название альбома
* artist — автор альбома
* genre — жанр альбома
* year — год выпуска альбома
#### Также экземпляр класса MusicAlbum должен иметь следующее формальное строковое представление:

> MusicAlbum(title='<название альбома>', artist='<автор альбома>')
#### Наконец, экземпляры класса MusicAlbum должны поддерживать между собой операцию сравнения с помощью операторов == и!=. Два музыкальных альбома считаются равными, если их названия, авторы и годы выпуска совпадают.

##### Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.

##### Примечание 2. Никаких ограничений касательно реализации класса MusicAlbum нет, она может быть произвольной.

<table align="center">
  <tbody>
    <tr>
      <th>Sample Input 1: </th>
      <th>Sample Input 2: </th>
      <th>Sample Input 3: </th>
    </tr>
    <tr>
      <td align="center">print(MusicAlbum('Calendar', 'Motorama', 'Post-punk', 2012))<br></td>
      <td align="center">musicalbum1 = MusicAlbum('Calendar', 'Motorama', 'Post-punk', 2012)<br>
                        musicalbum2 = MusicAlbum('Calendar', 'Motorama', 'New Wave, Indie Rock', 2012)<br>
                        print(musicalbum1 == musicalbum2)<br>
                        print(musicalbum1 != musicalbum2)<br></td>
      <td align="center">musicalbum = MusicAlbum('Calendar', 'Motorama', 'Post-punk', 2012)<br>
                          try:<br>
                              musicalbum.genre = 'Post-punk, New Wave, Indie Rock'<br>
                          except:<br>
                              print('Error')<br></td>
    </tr>
    <tr>
      <td>Sample Output 1:</td>
      <td>Sample Output 2:</td>
      <td>Sample Output 3:</td>
      </tr>
    <tr>
      <td align="center">
                        MusicAlbum(title='Calendar', artist='Motorama')<br>
      </td>
      <td align="center">
                        True<br>
                        False<br>
      </td>
      <td align="center">
                        Error<br>
      </td>
    </tr>
  </tbody>
</table>



## Примеры решений:
* Первый вариант решения
```python
from dataclasses import dataclass, field


@dataclass(frozen=True)
class MusicAlbum:
    title: str
    artist: str
    genre: str = field(repr=False, compare=False)
    year: int = field(repr=False)
```
* Второй вариант решения

```python
from dataclasses import dataclass, field


@dataclass(frozen=True)
class MusicAlbum:
    title: str
    artist: str
    genre: str = field(repr=False, compare=False)
    year: int = field(repr=False)
```


