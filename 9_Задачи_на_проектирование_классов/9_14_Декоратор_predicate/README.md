<h2 style="text-align:center">Декоратор @predicate</h2>

### Предикат — это функция, которая возвращает True или False в зависимости от переданных аргументов.

### Реализуйте декоратор @predicate, который будет позволять удобно комбинировать предикаты с помощью операторов &, | и ~:
```python
@predicate
def is_even(num):
    return num % 2 == 0

@predicate
def is_positive(num):
    return num > 0

print((is_even & is_positive)(4))             # True; равнозначно is_even(4) and is_positive(4)
print((is_even & is_positive)(3))             # False; равнозначно is_even(3) and is_positive(3)
print((is_even | is_positive)(3))             # True; равнозначно is_even(3) or is_positive(3)
print((~is_even & is_positive)(3))            # True; равнозначно not is_even(3) and is_positive(3)
```
#### Декоратор должен уметь работать с любыми предикатами, независимо от того, сколько аргументов они принимают:
```python
@predicate
def to_be():
    return True

print((to_be | ~to_be)())                     # True; равнозначно to_be() or not to_be()

@predicate
def is_equal(a, b):
    return a == b

@predicate
def is_less_than(a, b):
    return a < b

print((is_less_than | is_equal)(1, 2))        # True; равнозначно is_less_than(1, 2) or is_equal(1, 2)
```
#### Также должны поддерживаться как позиционные аргументы, так и именованные:
```python
print((is_less_than | is_equal)(2, b=2))      # True; равнозначно is_less_than(2, b=2) or is_equal(2, b=2)
print((is_less_than | is_equal)(a=3, b=2))    # False; равнозначно is_less_than(a=3, b=2) or is_equal(a=3, b=2)
```
#### Задекорированная функция должна быть доступна вне комбинаций с другими функциями и вести себя как исходная функция:
```python
@predicate
def is_less_than(a, b):
    return a < b

print(is_less_than(1, 2))                     # True
print(is_less_than(2, 2))                     # False
print(is_less_than(3, 2))                     # False
```
#### Примечание 1. Гарантируется, что комбинируемые функции имеют одинаковые сигнатуры. 

<table align="center">
  <tbody>
    <tr>
      <th>Sample Input 1: </th>
      <th>Sample Input 2: </th>
    </tr>
    <tr>
      <td align="center">@predicate<br>
                            def to_be():<br>
                                return True<br>
                            print((to_be | ~to_be)())                     # True; равнозначно to_be() or not to_be()<br>
                            @predicate<br>
                            def is_equal(a, b):<br>
                                return a == b<br>
                            @predicate<br>
                            def is_less_than(a, b):<br>
                                return a < b<br>
                            print((is_less_than | is_equal)(1, 2))        # True; равнозначно is_less_than(1, 2) or is_equal(1, 2)<br>
                            print((is_less_than | is_equal)(2, b=2))      # True; равнозначно is_less_than(2, b=2) or is_equal(2, b=2)<br>
                            print((is_less_than | is_equal)(a=3, b=2))    # False; равнозначно is_less_than(a=3, b=2) or is_equal(a=3, b=2)<br></td>
      <td align="center">@predicate<br>
                          def is_even(num):<br>
                              return num % 2 == 0<br>
                          @predicate<br>
                          def is_positive(num):<br>
                              return num > 0<br>
                          print((is_even & is_positive)(4))             # True; равнозначно is_even(4) and is_positive(4)<br>
                          print((is_even & is_positive)(3))             # False; равнозначно is_even(3) and is_positive(3)<br>
                          print((is_even | is_positive)(3))             # True; равнозначно is_even(3) or is_positive(3)<br>
                          print((~is_even & is_positive)(3))            # True; равнозначно not is_even(4) and is_positive(4)<br></td>
    </tr>
    <tr>
      <td>Sample Output 1:</td>
      <td>Sample Output 2:</td>
      </tr>
    <tr>
      <td align="center">
                        True<br>
                        True<br>
                        True<br>
                        False<br>
      </td>
      <td align="center">
                        True<br>
                        False<br>
                        True<br>
                        True<br>
      </td>
    </tr>
  </tbody>
</table>



## Примеры решений:
* Первый вариант решения
```python
class Predicate:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        return self.func(*args, **kwargs)

    def __invert__(self):
        def invert_func(*args, **kwargs):
            return not self(*args, **kwargs)
        return __class__(invert_func)

    def __and__(self, other):
        def and_func(*args, **kwargs):
            return self(*args, **kwargs) and other(*args, **kwargs)
        return __class__(and_func)

    def __or__(self, other):
        def or_func(*args, **kwargs):
            return self(*args, **kwargs) or other(*args, **kwargs)
        return __class__(or_func)


def predicate(func):
    return Predicate(func)
```
* Второй вариант решения

```python
class predicate:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        return self.func(*args, **kwargs)

    def __invert__(self):
        def not_func(*args, **kwargs):
            return not self.func(*args, **kwargs)

        return type(self)(not_func)

    def __or__(self, other):
        def or_func(*args, **kwargs):
            return self.func(*args, **kwargs) or other.func(*args, **kwargs)

        return type(self)(or_func)

    def __and__(self, other):
        def and_func(*args, **kwargs):
            return self.func(*args, **kwargs) and other.func(*args, **kwargs)

        return type(self)(and_func)
```


