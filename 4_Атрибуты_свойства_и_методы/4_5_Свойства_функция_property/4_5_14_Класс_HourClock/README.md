<h2 style="text-align:center">Класс HourClock</h2>

### Реализуйте класс HourClock, описывающий часы с одной лишь часовой стрелкой. При создании экземпляра класс должен принимать один аргумент:
* hours — количество часов. Если hours не является целым числом, принадлежащим диапазону [1; 12], должно быть возбуждено исключение ValueError с текстом:
> Некорректное время
#### Класс HourClock должен иметь одно свойство:
* hours — свойство, доступное для чтения и записи, возвращающее текущее количество часов. При изменении свойство должно проверять, что новое значение является целым числом, принадлежащим диапазону [1; 12], в противном случае должно быть возбуждено исключение ValueError с текстом:
> Некорректное время

##### Примечание 1. Никаких ограничений касательно реализации класса HourClock нет, она может быть произвольной.

<table align="center">
  <tbody>
    <tr>
      <th>Sample Input 1: </th>
      <th>Sample Input 2: </th>
      <th>Sample Input 3: </th>
    </tr>
    <tr>
      <td align="center">time = HourClock(7)<br>
                        print(time.hours)<br>
                        time.hours = 9<br>
                        print(time.hours)<br></td>
      <td align="center">time = HourClock(7)<br>
                            try:<br>
                                time.hours = 15<br>
                            except ValueError as e:<br>
                                print(e)<br></td>
      <td align="center">try:<br>
                            HourClock('pizza time ')<br>
                        except ValueError as e:<br>
                            print(e)<br></td>
    </tr>
    <tr>
      <td>Sample Output 1:</td>
      <td>Sample Output 2:</td>
      <td>Sample Output 3:</td>
      </tr>
    <tr>
      <td align="center">
                       7<br>
                        9<br>
      </td>
      <td align="center">
                        Некорректное время<br>
      </td>
      <td align="center">
                        Некорректное время<br>
      </td>
    </tr>
  </tbody>
</table>



## Примеры решений:
* Первый вариант решения
```python
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
```
* Второй вариант решения

```python
class HourClock:

    def __init__(self, hours):
        self.hours = hours

    @property
    def hours(self):
        return self._hours

    @hours.setter
    def hours(self, hours):
        if not isinstance(hours, int) or hours not in range(1,13):
            raise ValueError('Некорректное время')
        self._hours = hours
```


