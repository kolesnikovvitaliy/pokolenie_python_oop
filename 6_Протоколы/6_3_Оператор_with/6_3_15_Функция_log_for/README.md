<h2 style="text-align:center">Функция log_for()</h2>

### Лог-файл — это текстовый файл, в который автоматически записывается важная информация о работе системы или программы. Форматов лог-файла довольно много, однако в рамках этой задачи будем считать, что все лог-файлы имеют следующий единый формат:
> 2022-01-01 INFO: User logged in
> 2022-01-01 ERROR: Invalid input data
> 2022-01-01 WARNING: File not found
> 2022-01-02 INFO: User logged out
> 2022-01-03 INFO: User registered
#### То есть каждая строка лог-файла описывает некоторое событие, которое характеризуется датой в формате YYYY-MM-DD, типом и кратким описанием.
#### Реализуйте функцию log_for(), которая принимает два аргумента в следующем порядке:
* logfile — имя лог-файла
* date_str — строковая дата в формате YYYY-MM-DD
#### Функция должна создавать текстовый файл с именем:
> log_for_<date_str>.txt
#### и записывать в него все события из файла logfile, которые произошли в дату date_str. События должны записываться без указания даты, а также располагаться в своем исходном порядке.

##### Примечание 1. Имя файла, передаваемого в функцию, уже содержит расширение.
##### Примечание 2. При открытии файла используйте явное указание кодировки UTF-8.
##### Примечание 3. В тестирующую систему сдайте программу, содержащую только необходимую функцию log_for(), но не код, вызывающий ее.

<table align="center">
  <tbody>
    <tr>
      <th>Sample Input 1: </th>
    </tr>
    <tr>
      <td align="center">with open('log.txt', 'w', encoding='utf-8') as file:<br>
                            print('2022-01-01 INFO: User logged in', file=file)<br>
                            print('2022-01-01 ERROR: Invalid input data', file=file)<br>
                            print('2022-01-02 INFO: User logged out', file=file)<br>
                            print('2022-01-03 INFO: User registered', file=file)<br>
                        log_for('log.txt', '2022-01-01')<br>
                        with open('log_for_2022-01-01.txt', encoding='utf-8') as file:<br>
                            print(file.read())<br></td>
    </tr>
    <tr>
      <td>Sample Output 1:</td>
      <td>Sample Output 2:</td>
      </tr>
    <tr>
      <td align="center">
                        INFO: User logged in<br>
                        ERROR: Invalid input data<br>
      </td>
    </tr>
  </tbody>
</table>



## Примеры решений:
* Первый вариант решения
```python
def log_for(logfile, date_str):
    with (
        open(logfile, mode='r', encoding='utf-8') as read_file,
        open(f'log_for_{date_str}.txt', mode='w', encoding='utf-8') as write_file,
        ):
        text = '\n'.join(map(lambda y: y[11:],filter(lambda x: date_str in x, map(str,read_file.read().split('\n')))))
        write_file.write(text)
```
* Второй вариант решения

```python
def log_for(logfile, date_str): 
    with open(f'log_for_{date_str}.txt', 'w') as result:
        for line in open(logfile):
            if date_str in line:
                date, info = line.split(' ', 1)
                result.write(info)
```


