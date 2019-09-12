# 1. Topics
<!-- TOC -->

- [Topics](#topics)
  - [F Strings](#f-strings)
  - [Counter Object](#counter-object)
  - [Statistics Module](#statistics-module)
  - [Sequence Operations having count](#sequence-operations-having-count)
  - [Lambda Expressions](#lambda-expressions)
  - [Chained Comparison](#chained-comparison)
  - [Random Module](#random-module)
    - [seed()](#seed)
    - [Continuous Distributions from Random Module](#continuous-distributions-from-random-module)
    - [Discrete Distributions](#discrete-distributions)
    - [Choice and Sample](#choice-and-sample)

<!-- /TOC -->

## 1.1. F Strings

```python
x = 11
y = 20
print(f'The value of {x} and {y} printed using f-string')
The value of 11 and 20 printed using f-string
```
  
## 1.2. Counter Object

```python
from collections import Counter
from collections import Counter
print(c)
from collections import Counter
```
  
## 1.3. Statistics Module

- For descriptive statistics

```python
from statistics import mean, median, stdev, pstdev
a = [10, 20, 30, 30, 40]
print(mean(a))
26
print(median(a))
30
print(stdev(a))
11.40175425099138
print(pstdev(a))
10.198039027185569
```
  
## 1.4. Sequence Operations having count

## 1.5. Lambda Expressions

- Promise/ Thunk

```python
x = 11
y = 20
# Define a promise
f = lambda : x ** y
f()
672749994932560009201
x= 2
y = 5
f()
32
```

## 1.6. Chained Comparison

```python
x > 10 and x < 20
10 < x < 20
```

## 1.7. Random Module

### 1.7.1. seed()

- Used when we want to have reproducible results

```python
from random import *

seed(8675309)
print(random())
0.40224696110279223
print(random())
0.5102471779215914
print(random())
0.6637431122665531

seed(8675309)
print(random())
0.40224696110279223
print(random())
0.5102471779215914
print(random())
0.6637431122665531
```

### 1.7.2. Continuous Distributions from Random Module

- [Continuous Uniform Distribution](https://en.wikipedia.org/wiki/Uniform_distribution)
  - Chooses a continuous value in the range uniformly (a line)
  - The shape of Continuous Uniform Distribution is a line

  ```python
  from random import *

  print(uniform(1000, 1100))
  1086.0716692339552
  ```

- [Triangular Distribution](https://en.wikipedia.org/wiki/Triangular_distribution)
  - Choosing half-way point much more frequently than the edges
  - Chosen values will often centered around the middle and very few entries towards the start and end range

  ```python
  from random import *

  print(triangular(1000,1100))
  1057.65582224645
  ```

- [Gaussian Distribution](https://en.wikipedia.org/wiki/Normal_distribution)
  - Similar to Triangular, except that tails are little angular (unlike line kind of in triangular)

  ```python
  from random import *

  print(gauss(100,15))
  93.5190441331644
  ```

- [Expo Variate Distribution](https://en.wikipedia.org/wiki/Exponential_distribution)
  - Also called as Poission Distribution

  ```python
  from random import *

  print(expovariate(20))
  0.0025031711703413593

  from statistics import mean, stdev

  seed(8675309)
  data = [triangular(1000,1100) for i in range(1000)]
  print(mean(data), stdev(data))
  1048.7066714907694 20.122912471146602

  seed(8675309)
  data = [uniform(1000,1100) for i in range(1000)]
  print(mean(data), stdev(data))
  1047.9972670913842 28.867097997620476

  seed(8675309)
  data = [gauss(100,15) for i in range(1000)]
  print(mean(data), stdev(data))
  100.73966226032182 14.411715471821212

  seed(8675309)
  data = [expovariate(20) for i in range(1000)]
  print(mean(data), stdev(data))
  0.04657302276891186 0.04607919272293802
  ```

### 1.7.3. Discrete Distributions

```python
from random import choice, choices, sample, shuffle
from collections import Counter

outcomes = ['win', 'lose', 'draw', 'play again', 'double win']
```

- Choice
  - Used to make a single choice out of a list
    - I.e., duplications are allowed in the choices

  ```python
  In [67]: choice(outcomes)
  Out[67]: 'double win'

  In [68]: choice(outcomes)
  Out[68]: 'lose'

  In [69]: choice(outcomes)
  Out[69]: 'draw'

  In [70]: choice(outcomes)
  Out[70]: 'play again'

  In [71]: choice(outcomes)
  Out[71]: 'double win'
  ```

- Choices
  - Used for making multiple choices, we can tell how many we want
  - Sampling with replacements
    - I.e., duplications are allowed in the choices

  ```python
  In [72]: choices(outcomes, k=10)
  Out[72]:
  ['draw',
   'play again',
   'double win',
   'draw',
   'play again',
   'play again',
   'draw',
   'win',
   'double win',
   'double win']

  In [73]: from collections import Counter

  In [74]: Counter(choices(outcomes, k=10))
  Out[74]: Counter({'double win': 1, 'play again': 3, 'lose': 2, 'draw': 2, 'win': 2})

  In [75]: Counter(choices(outcomes, k=10000))
  Out[75]:
  Counter({'lose': 2027,
           'play again': 2050,
           'double win': 1987,
           'draw': 1974,
           'win': 1962})

  In [76]: Counter(choices(outcomes, [5,4,3,2,1],k=10000))
  Out[76]:
  Counter({'win': 3319,
           'play again': 1346,
           'draw': 1997,
           'lose': 2680,
           'double win': 658})
  ```

- Shuffle
  - It works in place, shuffles the items

  ```python
  In [78]: outcomes
  Out[78]: ['win', 'lose', 'draw', 'play again', 'double win']

  In [79]: shuffle(outcomes)

  In [80]: outcomes
  Out[80]: ['draw', 'lose', 'win', 'play again', 'double win']

  In [81]: choices(outcomes, k=5)
  Out[81]: ['double win', 'double win', 'double win', 'win', 'double win']


  ```

- Sample
  - Sampling without replacement
    - That is, choosing items without duplication

  ```python
  In [82]: sample(outcomes, k=4)
  Out[82]: ['play again', 'win', 'double win', 'draw']

  In [83]: sample(outcomes, k=4)
  Out[83]: ['win', 'lose', 'play again', 'double win']
  ```

### 1.7.4. Choice and Sample

- Choice is a special case of sample

  ```python
  # Both of the are similar in relation
  # Choice is a special case of sample
  In [84]: sample(outcomes,k=1)
  Out[84]: ['lose']
  In [86]: choice(outcomes)
  Out[86]: 'play again'

  # Both of the are similar in relation
  # Shuffle is a special case of sample
  In [87]: shuffle(outcomes); outcomes
  Out[87]: ['win', 'lose', 'play again', 'double win', 'draw']
  In [88]: sample(outcomes,k=len(outcomes))
  Out[88]: ['draw', 'lose', 'win', 'play again', 'double win']
  ```
