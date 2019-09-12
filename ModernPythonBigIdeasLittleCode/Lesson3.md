# 1. Improving Reliability with MyPy and Type Hinting
<!-- TOC -->

- [Improving Reliability with MyPy and Type Hinting](#improving-reliability-with-mypy-and-type-hinting)
  - [Part 1](#part-1)
  - [Part 2](#part-2)

<!-- /TOC -->

## 1.1. Part 1

```text
Type Hinting and linting
========================

Big Idea: Add type hints to code helps clarify your thoughts,
          improves documentation, and may allow a static
          analysis tool to detect some kinds of error

* Use of "# type"
* Use of function annotations
* Use of class
* Container[Type]
* Tuple and ...
* Optional arguments
* Deque vs deque
* Issues with f-string, new colon notation, secrets module

Tools
=====

* mypy
* pyflakes
* hypothesis
* unittest -> nose py.test

```

```python
from typing import *
from collections import OrderedDict, deque, namedtuple

x = 10       # type: int
x2: int = 20

def f(x: int, y: Optional[int]=None) -> int:
  if y is None:
    y = 20
  return x + y

y = OrderedDict()   # type: OrderedDict

def g(x: List[int]) -> None:
  print(len(x))
  print(x[2])
  for i in x:
    print(i)
  print()

g([10, 20, 30])

hts = [97.1, 102.5, 97.5]         # type: List[float]
person = ('Raymond', 5 * 12 + 11) # type: Tuple[str, float]
info = ('Pearson', 'Course', 'Python' 'Raymond') # Tuple[str, ...]
fifo = deque()                   # type: eque

Point = namedtuple('Point', [('x', int), ('y' int)])
```

## 1.2. Part 2

```python
```
