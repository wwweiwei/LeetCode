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
numbers = [i for i in range(1, n+1)]
numbers = [[0] * cols ] * rows ## not good
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
* Zip
``` python
friends= ["芸芸", "萱萱", "琳琳", "娜娜"]
stars = ["天秤", "金牛", "雙魚","雙子"]
likes = ["餅乾", "巧克力", "草莓", "蛋糕"]

zipped = zip(friends, stars, likes)
print(list(zipped))
```
> output: [('芸芸', '天秤', '餅乾'), 
>          ('萱萱', '金牛', '巧克力'), 
>          ('琳琳', '雙魚', '草莓'), 
>          ('娜娜', '雙子', '蛋糕')]

    * if don't know the numbers of pair
    ``` python
    datas = [('芸芸', '天秤', '餅乾'), 
                ('萱萱', '金牛', '巧克力'), 
                ('琳琳', '雙魚', '草莓'), 
                ('娜娜', '雙子', '蛋糕')]
    zipped = zip(*datas)
    print(list(zipped))
    ```
> output: [('芸芸', '萱萱', '琳琳', '娜娜'), 
>          ('天秤', '金牛', '雙魚', '雙子'), 
>          ('餅乾', '巧克力', '草莓', '蛋糕')]

* Example
>>> a=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> a[-1:]
[9]
>>> a[-9:-1]
[1, 2, 3, 4, 5, 6, 7, 8]
>>> a[1:20]
[1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> a[:9]
[0, 1, 2, 3, 4, 5, 6, 7, 8]
>>> a[0:]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> a[9:3]
[]

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

### Array
* Array 和 List 的差異
    * Array: 
        * 每一個元素都必須有**相同**的資料型態
        * 在記憶體上的儲存位置會排在一起, 因此 array 的存取速度比 list 快
    * List: 每一個元素可以是**不同**的資料型態, 在記憶體中的儲存位置是很難以預測
``` python
import numpy as np
a = np.arange(0,4.0,0.5) # [ 0.  0.5  1.  1.5  2.  2.5  3.  3.5]
b = np.array(range(10)) # [0 1 2 3 4 5 6 7 8 9]
c = a[1:-1]**2 # [ 0.25  1.  2.25  4.  6.25  9.]
d = a[:-1] + b[-7:] # 將 array a 和 array b 的 index 0~-1 與 -7~ 最後元素取出相加
```
* 2D array
``` python
a = np.array([[1, 2], [3, 4]], dtype = float)
    ## a[0][0] a[0][1]
    ## a[1][0] a[1][1]
np.sum(a, axis = 0)  # 將矩陣的元素沿著直的方向加起來
np.sum(a, axis = 1)  # 將矩陣的元素沿著橫的方向加起來
np.zeros((5,3)) # 建立shape為(5,3), 每個元素都是0的Array
np.ones((5,3)) # 建立shape為(5,3), 每個元素都是1的Array
np.linspace(0,10,21) # array([ 0. ,0.5, 1. , 1.5, 2. , 2.5, 3. ,3.5, 4. , 4.5, 5. , 5.5, 6. , 6.5, 7. , 7.5, 8. , 8.5, 9. , 9.5, 10. ])
np.diag([1,2,3]) # 建立主對角線元素依序為1,2,3的方陣, shape為(3,3)
np.eye(5) # 產生5X5的1對角陣列
np.random.rand(5,5) # 建立shape為(5,5)的Array, 每個元素介於0~1之間均勻隨機產生
np.random.randn(5,5) # 建立shape為(5,5)的Array, 所有元素的產生呈常態分佈, 平均值為0, 標準差為1
np.random.randint(1,100,(3,5)) # 有參數(low, high,size)可以自己設定範圍, 該數字落在兩個數字區間中
``` 
* 維度擴充
``` python
a = np.array([1, 2, 3, 4]) # 建立1維的array
a[:, np.newaxis]  # 意義等同array([[1], [2], [3], [4]])
a[np.newaxis, :]  # 意義等同array([[1, 2, 3, 4]])
a.reshape(2,2) # 改變 NumPy Array 的 shape
a.max() / a.min()
a.argmax() / a.argmin()
a.dtype
```
* 
``` python

```
* 
``` python

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
* Regex (Regular expression)
    * \d: 從0到9的數字 
    * \w: 任何的字母、數字及底線符號_
    * \s: 空白字元，包括空格、定位符號空格(tab)、換行符號
    * \D: \d規則以外的字元
    * \W: \w規則以外的字元
    * \S: \s規則以外的字元
``` python
import re
phoneNumRegex = re.compile(r'\d\d-\d\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('Call me at 02-0000-0000 by today.')
print(mo.group()) # 02-0000-0000
```
    * findall() 與 search() 不同的是：
        * 不需要使用 group() 就可以呈現出比對成功的結果
        * findall(): return **list**
        * search(): return **string**
        * group() 的括號內填入組別, 取得指定的比對資料
        

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

### argparse
``` python
parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('integers', metavar='N', type=int, nargs='+',
                    help='an integer for the accumulator')
parser.add_argument('--sum', dest='accumulate', action='store_const',
                    const=sum, default=max,
                    help='sum the integers (default: find the max)')

args = parser.parse_args()
parser = argparse.ArgumentParser(description='Process some integers.')

```
* **ArgumentParser** 方法
    * description: 簡要描述這個程序做什麼以及怎麼做
* **add_argument** 方法
    * help
    * nargs
        * '*':引數可以是任意數量（0 個或任意多個）
        * N: 一個整數 e.g. 1, 2..
        * '?': 引數只能是 0 個或是 1 個
        * '+': 引數至少 1 個（1 個或任意多個）
    * default
    * type
    * choices：有範圍的等級 e.g. choices=[0, 1, 2]

* 儲存引數資料的 Namespace 物件
    * 使用 parse_args() 從 parser 取得引數資料後，此函數會回傳 Namespace 物件，這只是一個單純把資料用屬性（attribute）儲存下來的超簡單類別
``` python
args = parser.parse_args()
## args 是 Namespace 物件，只是個極簡單的類別
print(args) # Namespace(arg1='hello', arg2='world', arg3=3)

## 用一般取得 attribute 的方式來取得引數資料內容
print(args.arg1) # hello

## 可以使用 vars(), 以 dict 資料結構取得引數資料
print(vars(args)) # {'arg1': 'hello', 'arg2': 'world', 'arg3': 3}
```
* **action**
    * action = "**store_true**"
    ``` python
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--verbose",
                        action = "store_true",  # 引數儲存為 boolean
                        help = "簡單開關的引數")
    args = parser.parse_args()
    print(args.verbose)

    python3 test.py --verbose
    > args.verbose 的數值為：True

    python3 test.py ## 沒輸入 Flag 的話，預設為 False
    > args.verbose 的數值為：False
    ```
    * action = "**count**"
    ``` python
    parser.add_argument("-v",
                        "--verbose",
                        action="count",
                        default=0,
                        help="請輸入囉唆程度")
    args = parser.parse_args()
    print(f"args.verbose 的值為：{args.verbose}")

    python3 test.py -v # args.verbose 的值為：1
    python3 test.py -vv # args.verbose 的值為：2
    python3 test.py --verbose --verbose --verbose # args.verbose 的值為：3
    python3 test.py # args.verbose 的值為：0
    ```

### Others
* Bitwise Shift Assignment
``` python
A >>= B ## bitwise right shift and assigns value to the left operand
A <<= B ## bitwise left shift and assigns value to the left operand
```
* Count
``` python
string.count(substring, start=..., end=...)
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
* Argparse: https://haosquare.com/python-argparse/
