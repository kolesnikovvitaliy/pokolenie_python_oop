<h2 style="text-align:center">Класс PiggyBank 3</h2>

### Реализуйте класс PiggyBank, а затем создайте экземпляр этого класса и присвойте его переменной money_box.

#### Класс PiggyBank должен иметь:
* атрибут content со значением 'coins'
* атрибут alternate_name со значением 'penny bank'

## Примеры решений:
* Первый вариант решения
```python
class PiggyBank:
    content = 'coins'
    alternate_name = 'penny bank'


money_box = PiggyBank()
```
* Второй вариант решения
```python
class PiggyBank:
    pass

PiggyBank.content = 'coins'
PiggyBank.alternate_name = 'penny bank'

money_box = PiggyBank()
```


