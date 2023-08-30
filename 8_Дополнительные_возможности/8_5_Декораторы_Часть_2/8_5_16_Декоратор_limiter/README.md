<h2 style="text-align:center">Декоратор @limiter</h2>

### Любой пользовательский класс по умолчанию способен создавать бесконечное количество собственных экземпляров. Шаблон проектирования синглтон, напротив, гарантирует, что класс имеет только один собственный экземпляр, и при попытке создать новый, он возвращает уже имеющийся. 

### Реализуйте декоратор @limiter для декорирования класса, с помощью которого можно ограничивать количество создаваемых декорируемым классом экземпляров до определенного числа. Декоратор должен принимать три аргумента в следующем порядке:

* limit — количество экземпляров, которое может создать декорируемый класс
* unique — имя атрибута экземпляра декорируемого класса, значение которого является его идентификатором. Два экземпляра с одинаковыми идентификаторами существовать не могут. Если происходит попытка создать экземпляр, идентификатор которого совпадает с идентификатором одного из ранее созданных экземпляров, должен быть возвращен этот ранее созданный экземпляр
* lookup — определяет, какой объект должен быть возвращен, если превышено ограничение limit, а значение атрибута unique ранее не использовалось. При значении FIRST возвращается самый первый созданный экземпляр, при значении LAST — самый последний созданный экземпляр
##### Примечание 1. Гарантируется, что экземпляры декорируемого класса всегда имеют атрибут, который содержит их идентификатор.

<table align="center">
  <tbody>
    <tr>
      <th>Sample Input 1: </th>
      <th>Sample Input 2: </th>
    </tr>
    <tr>
      <td align="center">@limiter(2, 'ID', 'FIRST')<br>
                          class MyClass:<br>
                              def __init__(self, ID, value):<br>
                                  self.ID = ID<br>
                                  self.value = value<br>
                          obj1 = MyClass(1, 5)          # создается экземпляр класса с идентификатором 1<br>
                          obj2 = MyClass(2, 8)          # создается экземпляр класса с идентификатором 2<br>
                          obj3 = MyClass(1, 20)         # возвращается obj1, так как экземпляр с идентификатором 1 уже есть<br>
                          obj4 = MyClass(3, 0)          # превышено ограничение limit, возвращается первый созданный экземпляр<br>
                          print(obj3.value)<br>
                          print(obj4.value)<br></td>
      <td align="center">@limiter(3, 'ID', 'LAST')<br>
                          class MyClass:<br>
                              def __init__(self, ID, value):<br>
                                  self.ID = ID<br>
                                  self.value = value<br>
                          obj1 = MyClass(1, 5)          # создается экземпляр класса с идентификатором 1<br>
                          obj2 = MyClass(2, 8)          # создается экземпляр класса с идентификатором 2<br>
                          obj3 = MyClass(3, 10)         # создается экземпляр класса с идентификатором 3<br>
                          obj4 = MyClass(4, 0)          # превышено ограничение limit, возвращается последний созданный экземпляр<br>
                          obj5 = MyClass(2, 20)         # возвращается obj2, так как экземпляр с идентификатором 2 уже есть<br>
                          print(obj4.value)<br>
                          print(obj5.value)<br></td>
    </tr>
    <tr>
      <td>Sample Output 1:</td>
      <td>Sample Output 2:</td>
      </tr>
    <tr>
      <td align="center">
                        5<br>
                        5<br>
      </td>
      <td align="center">
                        10<br>
                        8<br>
      </td>
    </tr>
  </tbody>
</table>



## Примеры решений:
* Первый вариант решения
```python
def limiter(limit, unique, lookup):
    def wrapper(cls):
        cls._instances = []

        def decorator(*args, **kwargs):
            num_uniq = [getattr(i, unique) for i in cls._instances]
            if args[1] in num_uniq:
                return cls._instances[args[1]]
            elif args[0] in num_uniq:
                return cls._instances[args[0]-1]

            if len(cls._instances) < limit:
                cls._instances.append(cls(*args, **kwargs))
                return cls._instances[-1]

            if lookup == 'FIRST':
                return cls._instances[0]
            return cls._instances[-1]
        return decorator
    return wrapper
```
* Второй вариант решения

```python
def limiter(limit, unique, lookup):
    instances = {}
    lookups = {}

    def wrapper(cls):
        def get_instance(*args, **kwargs):
            instance = cls(*args, **kwargs)
            lookups.setdefault('FIRST', instance)
            identifier = getattr(instance, unique)
            if len(instances) < limit:
                if identifier not in instances:
                    lookups['LAST'] = instances[identifier] = instance
                return instances[identifier]
            return instances.get(identifier) or lookups.get(lookup)

        return get_instance

    return wrapper
```


