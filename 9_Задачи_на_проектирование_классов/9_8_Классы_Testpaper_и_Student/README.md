<h2 style="text-align:center">Классы Testpaper и Student</h2>

### В этой задаче вам необходимо реализовать класс Testpaper, который позволит составлять экзаменационные тесты. Каждый тест должен создаваться на основе темы, схемы верных ответов и минимального процента верных решений:
```python
testpaper1 = Testpaper('Maths', ['1A', '2C', '3D', '4A', '5A'], '60%')
testpaper2 = Testpaper('Chemistry', ['1C', '2C', '3D', '4A'], '75%')
testpaper3 = Testpaper('Computing', ['1D', '2C', '3C', '4B', '5D', '6C', '7A'], '75%')
```
#### Созданные тесты должны сдаваться студентом — экземпляром класса Student. Он должен иметь метод take_test(), который принимает в качестве аргументов тест и ответы студента на этот тест:
```python
student1 = Student()
student2 = Student()

student1.take_test(testpaper1, ['1A', '2D', '3D', '4A', '5A'])
student2.take_test(testpaper2, ['1C', '2D', '3A', '4C'])
student2.take_test(testpaper3, ['1A', '2C', '3A', '4C', '5D', '6C', '7B'])
```
#### Результаты тестов должны быть доступны в виде словаря, ключом в котором является тема теста, а значением — результат теста (сдан или не сдан), а также процент верных решений:
```python
print(student1.tests_taken)    # {'Maths': 'Passed! (80%)'}
print(student2.tests_taken)    # {'Chemistry': 'Failed! (25%)', 'Computing': 'Failed! (43%)'}
```
#### Если студент еще не сдал ни одного теста, атрибут tests_taken должен содержать строку No tests taken:
```python
student3 = Student()

print(student3.tests_taken)    # No tests taken
```
#### Примечание 1. Округление процента верных решений должно происходить до ближайшего целого числа.

<table align="center">
  <tbody>
    <tr>
      <th>Sample Input 1: </th>
      <th>Sample Input 2: </th>
    </tr>
    <tr>
      <td align="center">paper1 = Testpaper('Maths', ['1A', '2C', '3D', '4A', '5A'], '60%')<br>
                          paper2 = Testpaper('Chemistry', ['1C', '2C', '3D', '4A'], '75%')<br>
                          paper3 = Testpaper('Computing', ['1D', '2C', '3C', '4B', '5D', '6C', '7A'], '75%')<br>
                          student1 = Student()<br>
                          student2 = Student()<br>
                          student1.take_test(paper1, ['1A', '2D', '3D', '4A', '5A'])<br>
                          student2.take_test(paper2, ['1C', '2D', '3A', '4C'])<br>
                          student2.take_test(paper3, ['1A', '2C', '3A', '4C', '5D', '6C', '7B'])<br>
                          print(student1.tests_taken)<br>
                          print(student2.tests_taken)<br></td>
      <td align="center">paper1 = Testpaper('Maths', ['1A', '2C', '3D', '4A', '5A'], '60%')<br>
                        paper2 = Testpaper('Chemistry', ['1C', '2C', '3D', '4A'], '75%')<br>
                        paper3 = Testpaper('Computing', ['1D', '2C', '3C', '4B', '5D', '6C', '7A'], '75%')<br>
                        student = Student()<br>
                        print(student.tests_taken)<br></td>
    </tr>
    <tr>
      <td>Sample Output 1:</td>
      <td>Sample Output 2:</td>
      </tr>
    <tr>
      <td align="center">
                        {'Maths': 'Passed! (80%)'}<br>
                        {'Chemistry': 'Failed! (25%)', 'Computing': 'Failed! (43%)'}<br>
      </td>
      <td align="center">
                        No tests taken<br>
      </td>
    </tr>
  </tbody>
</table>



## Примеры решений:
* Первый вариант решения
```python
from dataclasses import dataclass, field


@dataclass
class Testpaper:
    topic: str = field(default='')
    correct: list = field(default_factory=list)
    percent: str = field(default='')


class Student:
    def __init__(self):
        self.tests_taken = 'No tests taken'

    def take_test(self, obj, item=list):
        if isinstance(self.tests_taken, str):
            self.tests_taken = dict()
        res = self._result(item, obj)
        self.tests_taken[obj.topic] = res

    @staticmethod
    def _result(answers_student, obj):
        _result = list(set(answers_student) & set(obj.correct))
        _result = round((len(_result) / len(obj.correct)) * 100)
        result = f'{str(_result)+"%"}'
        if _result >= int(obj.percent[:-1]):
            return f'Passed! ({result})'
        return f'Failed! ({result})'
```
* Второй вариант решения

```python
class Testpaper:
    def __init__(self, subject, markscheme, pass_mark):
        self.subject = subject
        self.markscheme = markscheme
        self.pass_mark = pass_mark


class Student:
    def __init__(self):
        self.tests_taken = 'No tests taken'

    def take_test(self, paper: Testpaper, student_answers):
        score = len(set(paper.markscheme) & set(student_answers)) / len(paper.markscheme) * 100
        result = 'Passed!' if score >= int(paper.pass_mark[:-1]) else 'Failed'
        percent = f'{score:.0f}%'

        if self.tests_taken == 'No tests taken':
            self.tests_taken = {paper.subject: f'{result} ({percent})'}
        else:
            self.tests_taken[paper.subject] = f'{result} ({percent})'
```


