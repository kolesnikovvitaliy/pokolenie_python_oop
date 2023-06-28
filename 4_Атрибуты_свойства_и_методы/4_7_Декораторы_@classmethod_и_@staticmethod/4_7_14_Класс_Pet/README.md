<h2 style="text-align:center">Класс Pet</h2>

### Реализуйте класс Pet, описывающий домашнее животное. При создании экземпляра класс должен принимать один аргумент:
* name — имя домашнего животного
#### Экземпляр класса Pet должен иметь один атрибут:
* name — имя домашнего животного
#### Класс Pet должен иметь три метода класса:
* first_pet() — метод, возвращающий самый первый созданный экземпляр класса Pet. Если ни одного экземпляра еще не было создано, метод должен вернуть значение None
* last_pet() — метод, возвращающий самый последний созданный экземпляр класса Pet. Если ни одного экземпляра еще не было создано, метод должен вернуть значение None
* num_of_pets() — метод, возвращающий количество созданных экземпляров класса Pet

##### Примечание 1. Никаких ограничений касательно реализации класса Pet нет, она может быть произвольной.
##### Примечание 2. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.

<table align="center">
  <tbody>
    <tr>
      <th>Sample Input 1: </th>
      <th>Sample Input 2: </th>
    </tr>
    <tr>
      <td align="center">print(Pet.first_pet())<br>
                        print(Pet.last_pet())<br>
                        print(Pet.num_of_pets())<br></td>
      <td align="center">pet1 = Pet('Ratchet')<br>
                        pet2 = Pet('Clank')<br>
                        pet3 = Pet('Rivet')<br>
                        print(Pet.first_pet().name)<br>
                        print(Pet.last_pet().name)<br>
                        print(Pet.num_of_pets())<br></td>
    </tr>
    <tr>
      <td>Sample Output 1:</td>
      <td>Sample Output 2:</td>
      </tr>
    <tr>
      <td align="center">
                       None<br>
                        None<br>
                        0<br>
      </td>
      <td align="center">
                        Ratchet<br>
                        Rivet<br>
                        3<br>
      </td>
    </tr>
  </tbody>
</table>



## Примеры решений:
* Первый вариант решения
```python
class Pet:
    pets = [] 
    def __init__(self, name):
        self.name = name  
        __class__.pets.append(self)   

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        self._name = name
    
    @classmethod
    def first_pet(cls):
        if cls.pets:
            return cls.pets[0]
        else:
            return None
        
    @classmethod
    def last_pet(cls):
        if cls.pets:
            return cls.pets[-1]
        else:
            return None

    @classmethod
    def num_of_pets(cls):
        return len(cls.pets)
```
* Второй вариант решения

```python
class Pet:
    pets = []

    def __init__(self, name):
        self.name = name
        Pet.pets.append(self)

    @classmethod
    def first_pet(cls):
        return cls.pets[0] if cls.pets else None

    @classmethod
    def last_pet(cls):
        return cls.pets[-1] if cls.pets else None

    @classmethod
    def num_of_pets(cls):
        return len(cls.pets)
```


