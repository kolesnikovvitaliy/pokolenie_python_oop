<h2 style="text-align:center">Иерархия классов</h2>

### С помощью наследования и приведенной ниже схемы постройте иерархию классов, описывающих животных:

<div>
<img align="center" src="https://github.com/kolesnikovvitaliy/pokolenie_python_oop/blob/main/7_Наследование_и_полиморфизм/7_1_Наследование_Часть_1/7_1_25_Иерархия_классов/img/task.png" title="Git" **alt="Git">
​</div>

#### Класс Animal должен иметь два метода экземпляра:
* sleep() — пустой метод
* eat()— пустой метод
#### Класс Fish должен иметь один метод экземпляра:
* swim()— пустой метод
#### Класс Bird должен иметь один метод экземпляра:
* lay_eggs()— пустой метод
#### Класс FlyingBird должен иметь один метод экземпляра:
* fly()— пустой метод


<table align="center">
  <tbody>
    <tr>
      <th>Sample Input 1: </th>
    </tr>
    <tr>
      <td align="center">print(issubclass(Fish, Animal))<br>
                          print(issubclass(Bird, Animal))<br>
                          print(issubclass(FlyingBird, Animal))<br>
                          print(issubclass(FlyingBird, Bird))<br></td>
    </tr>
    <tr>
      <td>Sample Output 1:</td>
      </tr>
    <tr>
      <td align="center">
                        True<br>
                        True<br>
                        True<br>
                        True<br>
      </td>
    </tr>
  </tbody>
</table>



## Примеры решений:
* Первый вариант решения
```python
class Animal:
    def sleep(self): ...
    def eat(self): ...


class Fish(Animal):
    def swim(self): ...


class Bird(Animal):
    def lay_eggs(self): ...


class FlyingBird(Bird):
    def fly(self): ...
```
* Второй вариант решения

```python
class Animal:
    def sleep(self):
        pass

    def eat(self):
        pass


class Fish(Animal):
    def swim(self):
        pass


class Bird(Animal):
    def lay_eggs(self):
        pass


class FlyingBird(Bird):
    def fly(self):
        pass
```


