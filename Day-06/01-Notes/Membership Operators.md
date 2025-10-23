# Membership Operations in Python

## Introduction

Membership operators in Python are used to check whether a value is present in a sequence or collection, such as a list, tuple, or string. The membership operators are "in" and "not in."

## List of Membership Operators

1. **in:** Returns `True` if the left operand is found in the sequence on the right.
2. **not in:** Returns `True` if the left operand is not found in the sequence on the right.

### Examples

#### in Operator

```python
fruits = ["apple", "banana", "cherry"]
result = "banana" in fruits
# result will be True
```

#### not in Operator

```python
colors = ["red", "green", "blue"]
result = "yellow" not in colors
# result will be True
```


fruits = ['apple', 'banana', 'cherry']
print('banana' in fruits)    # True
print('grape' in fruits)     # False

print('grape' not in fruits) # True
print('apple' not in fruits) # False

s = "hello world"
print('h' in s)               # True
print('H' in s)               # False  # case‐sensitive

d = {'dog': 'mammal', 'cat': 'mammal'}
print('dog' in d)             # True  (key exists)
print('mammal' in d)          # False (value only, not key)
