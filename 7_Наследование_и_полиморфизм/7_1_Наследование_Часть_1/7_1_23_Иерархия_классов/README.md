<h2 style="text-align:center">Иерархия классов</h2>

### С помощью наследования и приведенной ниже схемы постройте иерархию пустых классов, описывающих транспортные средства:
<div>
<img align="center" src="https://github.com/kolesnikovvitaliy/pokolenie_python_oop/blob/main/7_Наследование_и_полиморфизм/7_1_Наследование_Часть_1/7_1_23_Иерархия_классов/img/task.png" title="Git" **alt="Git">
​</div>

<table align="center">
  <tbody>
    <tr>
      <th>Sample Input 1: </th>
      <th>Sample Input 2: </th>
    </tr>
    <tr>
      <td align="center">print(issubclass(LandVehicle, Vehicle))<br>
                        print(issubclass(WaterVehicle, Vehicle))<br>
                        print(issubclass(AirVehicle, Vehicle))<br></td>
      <td align="center">print(issubclass(Car, LandVehicle))<br>
                          print(issubclass(Motocycle, LandVehicle))<br>
                          print(issubclass(Bicycle, LandVehicle))<br></td>
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
      </td>
      <td align="center">
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
class Vehicle:
    pass


class LandVehicle(Vehicle):
    pass


class WaterVehicle(Vehicle):
    pass


class AirVehicle(Vehicle):
    pass


class Car(LandVehicle):
    pass


class Motocycle(LandVehicle):
    pass


class Bicycle(LandVehicle):
    pass


class Propeller(AirVehicle):
    pass


class Jet(AirVehicle):
    pass
```
* Второй вариант решения

```python
class Vehicle: ...
class LandVehicle(Vehicle): ...
class WaterVehicle(Vehicle): ...   
class AirVehicle(Vehicle): ...    
class Car(LandVehicle): ...    
class Motocycle(LandVehicle): ...    
class Bicycle(LandVehicle): ...    
class Propeller(AirVehicle): ...    
class Jet(AirVehicle): ...

```


