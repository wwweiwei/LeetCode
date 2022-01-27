# Python Cheetsheet
### Class
* Class
``` python
class classname：
　　statement
```
* Object
``` python
object_name = classname()
``` 
* Check whether object is belonging to class
``` python
isinstance(object_name, class_name)
```
* Attribute
``` python
object_name.attribute_name
```
* Method
``` python
def method_name(self):
　　statement
```
* Example
``` python
# 汽車類別
class Cars:
    # 建構式
    def __init__(self, color, seat):
        self.color = color  # 顏色屬性
        self.seat = seat  # 座位屬性
    # 方法(Method)
    def drive(self):
        print(f"My car is {self.color} and has {self.seat} seats.")
mazda = Cars("blue", 4)
mazda.drive()  #執行結果：My car is blue and has 4 seats.
```

### Lambda
* lambda parameter_list: expression
    E.g. 
    ``` python
    multiply = lambda x, y: x * y
    multiply(2, 3)
    > 6
    ```
* (lambda parameter: expression)(argument)
    E.g.
    ``` python
    (lambda x, y: x * y)(2, 3)
    ```
* filter(lambda parameter: expression, iterable)
    E.g.
    ``` python
    x_list = [1, 10, 100]
    filter(lambda x: x > 10, x_list)
    ```
* map(lambda parameter: expression, iterable)
    E.g.
    ``` python
    x_list = [1, 10, 100]
    map(lambda x: x * 2, x_list)
    ```
* reduce(lambda parameter1, parameter2: expression, iterable)
    E.g.
    ``` python
    from functools import reduce
    x_list = [1, 10, 100]
    reduce(lambda a, b: a + b, x_list)    
    ```
* sorted(iterable, key=lambda parameter: expression)
    E.g.
    ``` python
    cars = [
        ('mazda', 2000),
        ('toyota', 1000),
        ('benz', 100)
    ]
    sorted(x_list, key = lambda car: car[1])
    ```

### List
* Construction
``` python
numbers = [0, 1, 2]
numbers = list(range(3))
numbers = [1] * 3
title = list('Hello')
title = ['H'] * 3
``` 
* Index
``` python
numbers[0]
numbers[-1] # last element
numbers[0:]
numbers[::3] # 每格3個取一次
title.index('e') # find the index of 'e'
``` 
* Add
``` python
numbers = [0, 1, 2]
numbers.append(3)
numbers.insert(3, 3) # .insert(index, values)
```
* Delete
``` python
numbers.pop() # delete the last element
numbers.pop(1) # delete the second element
del numbers[0:3] # delete the first, second, third elements
title.remove(e) # delete the first element 'e'
title.clear() # delete all elements
```
* Count
``` python
numbers.count(1)
```
* 
``` python

```
* 
``` python

```
* 
``` python

```
* 
``` python

```
* 
``` python

```
* 
``` python

```
* 
``` python

```
* 
``` python

```
* 
``` python

```
* 
``` python

```
* 
``` python

```