# Python Chapter 2 – Data Types, Keywords, Type Conversion & Operators

This chapter covers the fundamentals of Python programming, including **data types, keywords, input/output, type conversion, and operators**.

## 📚 Topics Covered

* Data Types in Python
* Keywords in Python
* Input and Output
* Type Conversion

  * Implicit Conversion
  * Explicit Conversion
* Operators in Python
* Basic Python Programs
* Output-based Questions

---

## 1️⃣ Data Types in Python

Python has several built-in data types. They define the type of value a variable holds.

| Type    | Example           | Description                       |
| ------- | ----------------- | --------------------------------- |
| `int`   | `x = 10`          | Whole numbers                     |
| `float` | `y = 3.14`        | Numbers with decimals             |
| `str`   | `name = "Saumya"` | Sequence of characters            |
| `bool`  | `flag = True`     | Logical values: `True` or `False` |

The `type()` function can be used to check the data type of a variable.

```python
x = 10
print(type(x))
```

**Output:**

```text
<class 'int'>
```

### 🧩 Practice

Write a Python program that takes your age as input and prints:

* The value entered
* Its data type

---

## 2️⃣ Keywords in Python

Keywords are **reserved words that have special meaning in Python** and cannot be used as variable names.

Examples:

```text
and     as      assert    break     class
continue def    del       elif      else
except  False   finally   for       from
global  if      import    in        is
lambda  None    nonlocal  not       or
pass    raise   return    True      try
while   with    yield
```

You can use the following command to view Python's keywords:

```python
help("keywords")
```

### 🧩 Practice

Try to create a variable named `for`.

```python
for = 10
```

This produces a `SyntaxError` because `for` is a Python keyword and keywords cannot be used as variable names.

---

## 3️⃣ Print Sum Program

A simple program to input two numbers and calculate their sum:

```python
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

sum = a + b

print("The sum is:", sum)
```

### 🧩 Concepts Used

* `input()` takes user input as a string.
* `int()` converts the input into an integer.
* `print()` displays the result.
* `+` is an arithmetic operator.

### 🧩 Practice

Modify the program to calculate the **average of two numbers** instead of their sum.

---

## 4️⃣ Type Conversion

Type conversion means **changing one data type into another data type**.

### a. Implicit Conversion

Implicit conversion happens automatically when Python converts a value from one data type to another.

```python
x = 5
y = 2.5

z = x + y

print(z)
```

**Output:**

```text
7.5
```

Here, Python converts the integer `5` into a float during the calculation.

### b. Explicit Conversion

Explicit conversion is performed manually using built-in functions.

```python
x = "10"
y = int(x)

print(y + 5)
```

**Output:**

```text
15
```

### Common Conversion Functions

```python
int()
float()
str()
bool()
```

### 🧩 Practice

Take a number as input, convert it to a float, and print:

* The original value
* The converted value
* Their data types

---

## 5️⃣ Operators in Python

Operators are **symbols used to perform operations on operands**.

### Arithmetic Operators

Used for mathematical operations.

```text
+   -   *   /   %   //   **
```

Example:

```python
x = 5
y = 3

print(x + y)
```

### Comparison Operators

Used to compare values and return `True` or `False`.

```text
==   !=   >   <   >=   <=
```

Example:

```python
x = 5
y = 3

print(x > y)
```

**Output:**

```text
True
```

### Logical Operators

Used to perform logical operations on conditions.

```text
and
or
not
```

Example:

```python
x = 5
y = 3

print(x > 0 and y < 20)
```

**Output:**

```text
True
```

### Assignment Operators

Used to assign or modify values.

```text
=   +=   -=   *=   /=
```

Example:

```python
x = 10
x += 5

print(x)
```

**Output:**

```text
15
```

---

# 📝 Chapter 2 Assignment

## 📘 Section A – Theory Questions

### 1. What are data types in Python?

List any four data types with examples.

### 2. What is the difference between implicit and explicit type conversion?

Give one example of each.

### 3. What are operators in Python?

Explain any three types with examples.

---

# 💻 Section B – Coding Questions

## 1️⃣ Smart Temperature Converter

Take input in Celsius and print its equivalent temperature in Fahrenheit and Kelvin.

**Formulas:**

```text
Fahrenheit = (C × 9/5) + 32
Kelvin = C + 273.15
```

Example:

```text
Enter temperature in Celsius: 25

Fahrenheit: 77.0
Kelvin: 298.15
```

---

## 2️⃣ Bill Split Calculator

Write a program that takes:

* Total bill amount
* Number of friends

Calculate how much each person will pay.

Also print the data type of each variable used.

**Hint:** Use `float()` and the division operator `/`.

Example:

```text
Total bill: 1000
Friends: 4
Each will pay: 250.0
```

---

# 🧠 Section C – Application / Output-Based Questions

## 1. Predict the Output

```python
x = 5
y = 2.0

print(x // y)
print(x ** y)
```

## 2. Identify and Correct the Error

Incorrect code:

```python
if = 10
print(if)
```

Identify the error and explain why it occurs.

---

# 📌 Chapter 2 Summary

By completing this chapter, I practiced:

* Understanding Python's basic data types
* Checking data types using `type()`
* Understanding Python keywords
* Taking input using `input()`
* Converting input using `int()` and `float()`
* Understanding implicit and explicit type conversion
* Using arithmetic, comparison, logical, and assignment operators
* Writing basic Python programs
* Solving output-based questions
* Identifying syntax errors caused by Python keywords

---

## 📂 Chapter 2 Files

This chapter contains the following practice files:

```text
Chapter 2/
│
├── datatype.py
├── explicit.py
├── implicit.py
├── operator.py
├── practice.py
│
└── assignment/
    ├── sectionA.py
    ├── sectionB.py
    └── sectionC.py
```

---

### 🚀 Learning Progress

**Chapter 2 completed:** Data Types, Keywords, Type Conversion & Operators

> Practicing Python fundamentals one concept at a time. 🐍
