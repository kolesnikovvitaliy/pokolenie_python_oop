<h2 style="text-align:center">Классы WeatherWarning и WeatherWarningWithDate</h2>

### Реализуйте класс WeatherWarning, описывающий объект, предупреждающий о погодных изменениях. При создании экземпляра класс не должен принимать никаких аргументов.
#### Класс WeatherWarning должен иметь три метода экземпляра:
* rain() — метод, выводящий текст:
> Ожидаются сильные дожди и ливни с грозой
* snow() — метод, выводящий текст:
> Ожидается снег и усиление ветра
* low_temperature() — метод, выводящий текст:
> Ожидается сильное понижение температуры
### Также реализуйте класс WeatherWarningWithDate, наследника класса WeatherWarning, описывающий объект, предупреждающий о погодных изменениях с указанием даты. Процесс создания экземпляра класса WeatherWarningWithDate должен совпадать с процессом создания экземпляра класса WeatherWarning.
#### Класс WeatherWarningWithDate должен иметь три метода экземпляра:
* rain() — метод, принимающий в качестве аргумента дату (тип date) и выводящий текст:
> <дата в формате DD.MM.YYYY>
> Ожидаются сильные дожди и ливни с грозой
* snow() — метод, принимающий в качестве аргумента дату (тип date) и выводящий текст:
> <дата в формате DD.MM.YYYY>
> Ожидается снег и усиление ветра
* low_temperature() — метод, принимающий в качестве аргумента дату (тип date) и выводящий текст:
> <дата в формате DD.MM.YYYY>
> Ожидается сильное понижение температуры

##### Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.
##### Примечание 2. Никаких ограничений касательно реализации классов нет, она может быть произвольной.

<table align="center">
  <tbody>
    <tr>
      <th>Sample Input 1: </th>
      <th>Sample Input 2: </th>
      <th>Sample Input 3: </th>
    </tr>
    <tr>
      <td align="center">print(issubclass(WeatherWarningWithDate, WeatherWarning))<br></td>
      <td align="center">weatherwarning = WeatherWarning()<br>
                          weatherwarning.rain()<br>
                          weatherwarning.snow()<br>
                          weatherwarning.low_temperature()<br></td>
      <td align="center">from datetime import date<br>
                          weatherwarning = WeatherWarningWithDate()<br>
                          dt = date(2022, 12, 12)<br>
                          weatherwarning.rain(dt)<br>
                          weatherwarning.snow(dt)<br>
                          weatherwarning.low_temperature(dt)<br></td>
    </tr>
    <tr>
      <td>Sample Output 1:</td>
      <td>Sample Output 2:</td>
      <td>Sample Output 3:</td>
      </tr>
    <tr>
      <td align="center">
                        True<br>
      </td>
      <td align="center">
                        Ожидаются сильные дожди и ливни с грозой<br>
                        Ожидается снег и усиление ветра<br>
                        Ожидается сильное понижение температуры<br>
      </td>
      <td align="center">
                        12.12.2022<br>
                        Ожидаются сильные дожди и ливни с грозой<br>
                        12.12.2022<br>
                        Ожидается снег и усиление ветра<br>
                        12.12.2022<br>
                        Ожидается сильное понижение температуры<br>
      </td>
    </tr>
  </tbody>
</table>



## Примеры решений:
* Первый вариант решения
```python
class WeatherWarning:
    def rain(self):
        print('Ожидаются сильные дожди и ливни с грозой')

    def snow(self):
        print('Ожидается снег и усиление ветра')

    def low_temperature(self):
        print('Ожидается сильное понижение температуры')


class WeatherWarningWithDate(WeatherWarning):
    def rain(self, date_):
        print(date_.strftime('%d.%m.%Y'))
        super().rain()

    def snow(self, date_):
        print(date_.strftime('%d.%m.%Y'))
        super().snow()

    def low_temperature(self, date_):
        print(date_.strftime('%d.%m.%Y'))
        super().low_temperature()
```
* Второй вариант решения

```python
from datetime import date


class WeatherWarning:
    @staticmethod
    def rain():
        print('Ожидаются сильные дожди и ливни с грозой')

    @staticmethod
    def snow():
        print('Ожидается снег и усиление ветра')

    @staticmethod
    def low_temperature():
        print('Ожидается сильное понижение температуры')


class WeatherWarningWithDate(WeatherWarning):
    def rain(self, dt: date):
        print(dt.strftime("%d.%m.%Y"))
        super().rain()

    def snow(self, dt: date):
        print(dt.strftime("%d.%m.%Y"))
        super().snow()

    def low_temperature(self, dt: date):
        print(dt.strftime("%d.%m.%Y"))
        super().low_temperature()
```


