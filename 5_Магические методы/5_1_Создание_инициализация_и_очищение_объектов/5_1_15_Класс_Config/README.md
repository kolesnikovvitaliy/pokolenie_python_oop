<h2 style="text-align:center">Класс Config</h2>

### Реализуйте класс Config, который соответствует шаблону синглтон и описывает конфигурационный объект с фиксированными параметрами. При создании экземпляра класс не должен принимать никаких аргументов.
### При первом вызове конструктора класса Config должен создаваться и возвращаться экземпляр этого класса, а при последующих вызовах должен возвращаться экземпляр, созданный при первом вызове.
#### Экземпляр класса Config должен иметь четыре атрибута:
* program_name — атрибут со строковым значением GenerationPy
* environment — атрибут со строковым значением release
* loglevel — атрибут со строковым значением verbose
* version — атрибут со строковым значением 1.0.0
#### Класс Rectangle должен иметь два свойства:
* perimeter — свойство, доступное только для чтения, возвращающее периметр прямоугольника
* area — свойство, доступное только для чтения, возвращающее площадь прямоугольника

##### Примечание 1. Никаких ограничений касательно реализации класса Config нет, она может быть произвольной.

<table align="center">
  <tbody>
    <tr>
      <th>Sample Input 1: </th>
      <th>Sample Input 2: </th>
    </tr>
    <tr>
      <td align="center">config = Config()<br>
                          print(config.program_name)<br>
                          print(config.environment)<br>
                          print(config.loglevel)<br>
                          print(config.version)<br></td>
      <td align="center">config1 = Config()<br>
                          config2 = Config()<br>
                          config3 = Config()<br>
                          print(config1 is config2)<br>
                          print(config1 is config3)<br></td>
    </tr>
    <tr>
      <td>Sample Output 1:</td>
      <td>Sample Output 2:</td>
      </tr>
    <tr>
      <td align="center">
                        GenerationPy<br>
                        release<br>
                        verbose<br>
                        1.0.0<br>
      </td>
      <td align="center">
                        True<br>
                        True<br>
      </td>
    </tr>
  </tbody>
</table>



## Примеры решений:
* Первый вариант решения
```python
class Config:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = object.__new__(cls)
        return cls._instance

    def __init__(self):
        self.program_name = 'GenerationPy'
        self.environment = 'release'
        self.loglevel = 'verbose'
        self.version = '1.0.0'
```
* Второй вариант решения

```python
class Config:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = object.__new__(cls)
            cls._instance.program_name = 'GenerationPy'
            cls._instance.environment = 'release'
            cls._instance.loglevel = 'verbose'
            cls._instance.version = '1.0.0'
        return cls._instance
```


