# Python Cheetsheet

### Integer
* Number of Digits
``` python
# method 1
import math
if n > 0:
    digits = int(math.log10(n))+1
elif n == 0:
    digits = 1
elif n < 0:
    digits = int(math.log10(-n))+2
print(digits)

# method 2
len(str(n))
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
numbers[::3] # 每隔3個取一次
numbers[::-1] # reverse
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

### Tuples
> Iterable, Unmodifiable(不可修改的)
* Construct
``` python
price = (10, 20, 30)
price = 10, 20, 30
price = 10, # 如果只有一個資料一定要再加逗號
price = ([10, 20, 30])
price = 'Amy'
price = tuple(range(10)) # (0, 1, 2, 3, ...)
price = (10, 20) * 2 # (10, 20, 10, 20)
```
* Index
    * Same as **List**
``` python
price[1]

if i in price:
    price.index(i)
```

### String
* 在字串的前方加上f/F ，在 {} 符號中傳入變數或運算式
``` python
print(f"Hi I am {name}.")
```
* Built-in function
``` python
.upper()
.lower()
.capitalize() # 將字串的首字轉大寫
.title() # 每個單字字首轉大寫
len()
.strip() #清除字串的前後空白
```
* Python **does not** support string’s item assignment directly.
``` python
a = "Hello Python"
l = list(a)
l[0], l[6] = 'h', 'p'
''.join(l) # 'hello python'
```

### Dataframe
* Construct
``` python
df = pandas.DataFrame(字典或陣列資料)
df.index = ["s1", "s2", "s3", "s4"]  #自訂索引值
df.columns = ["student_name", "math_score"]  #自訂欄位名稱

grades = {
    "name": ["Mike", "Sherry", "Cindy", "John"],
    "math": [80, 75, 93, 86],
}
df = pd.DataFrame(grades)

grades = [
    ["Mike", 80],
    ["Sherry", 75],
    ["Cindy", 93],
    ["John", 86]
]
df = pd.DataFrame(grades)
```
* Index
``` python
df.head(3)
df.tail(3)
df['name'] # Series
df[['name']] # Dataframe
df[['name', 'math']] # Dataframe
df[0:3] # index 0-2
df.at[1, 'math'] # at[資料索引值, 欄位名稱]
df.iat[1, 0] # iat[資料索引值, 欄位順序]
df.loc[[1, 3], ['name', 'math']] # loc[資料索引值,欄位名稱]
df.iloc[[1, 3], [0, 2]] # iloc[資料索引值,欄位順序]
```
* Add
``` python
df.insert(2, column='english', value=[88, 72, 74, 98]) # 在第三欄的地方新增一個欄位資料
new_df = df.append({ 'name': 'Henry', 'math': 60,
    'english': 62 }, ignore_index=True) # 透過傳入 Dictionary 來指定各欄位的值

new_df = pd.concat([df1, df2], ignore_index=True) # 合併df來新增資料
```
* Delete
``` python
new_df = df.drop([0, 3], axis = 0) # 刪除指定資料索引的資料, 刪除第一筆及第四筆資料
new_df = df.drop(['math'], axis = 1) # 刪除指定欄位名稱的欄
new_df = df.dropna()
new_df = df.drop_duplicates()
```
* Filter
``` python
df[df['math'] > 80]
df[df['name'].isin(['John'])]
```
* Sort
``` python
df.sort_index(ascending = True) # 遞增排序
df.sort_index(ascending = False) # 遞減排序
df.sort_values(['math'], ascending = True)
```

### Dictionary
* Construct
``` python
store = {'apple' : 10, 'banana' : 20}
if 'apple' in store:
    store['apple']

for key in store:
    print(key) # key..
for key_value in store.items():
    print(key_value) # (key, value)..

store.get('apple') # if not exist, return None
store.get('apple', 'not exist')
```
* Delete
``` python
del store['apple']
store.clear()
```

---

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
* Function
``` python
def function(*args) # tuple
def function(**kwargs) # dict
```

### Exception Handler
* try-except
``` python
try:
    ...
except ValueError: # 特定錯誤
    ...
except ZeroDivisionError: # 特定錯誤
    ...
except: # 若不是特定錯誤就會到這
    ...
finally: # 不管怎樣最後都會執行
    file.close() # 釋放資源
```

### Looping Techniques
* Dictionary
``` python
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k, v)
```
* Sequence
``` python
for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)
```
* Two Sequences
``` python
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(q, a))
```
* Reverse
``` python
for i in reversed(range(1, 10, 2)):
    print(i)
# 9, 7, 5, 3, 1
```
* Sort
``` python
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for i in sorted(basket):
    print(i)

for f in sorted(set(basket)): ## eliminates duplicate element
    print(f)
```

### OOP
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
* Example of ** instance method ** 
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
``` python
# 汽車類別
class Cars:
    door = 4  #類別屬性
    # 實體方法(Instance Method)
    def drive(self):
        self.__class__.door = 5
print("Cars original door: ", Cars.door)
mazda = Cars()
mazda.drive()
print("Cars new door: ", Cars.door)
```
* ** Class method **
``` python
# 汽車類別
class Cars:
    # 建構式
    def __init__(self, seat, color):
        self.seat = seat
        self.color = color
    # 廂型車
    @classmethod
    def van(cls):
        return cls(6, "black")
    # 跑車
    @classmethod
    def sports_car(cls):
        return cls(4, "yellow")
van = Cars.van()
sports_car = Cars.sports_car()
```
* ** Static method **
``` python
# 汽車類別
class Cars:
    # 速率靜態方法
    @staticmethod
    def speed_rate(distance, minute):
        return distance / minute
# 透過物件呼叫
van = Cars()
van_rate = van.speed_rate(10000, 20)
print("van rate: ", van_rate)
# 透過類別呼叫
sports_car_rate = Cars.speed_rate(20000, 20)
print("sports car rate: ", sports_car_rate)
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

### Reference
* Python: https://www.learncodewithmike.com/