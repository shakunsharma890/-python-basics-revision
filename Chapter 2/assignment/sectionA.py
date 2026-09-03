## Section A — Theory Questions

### 1. What are data types in Python? List any 4 with examples.

'''Python has several built-in data types. **Data types define what kind of value a variable can store.**

Four types of data types are:

1. **int** — `10`
2. **float** — `10.5`
3. **str** — `"Hello"`
4. **bool** — `True` or `False`

---'''

### 2. What is the difference between implicit and explicit type conversion? Give one example of each.

'''**Implicit Type Conversion:**
Implicit type conversion is a conversion that happens **automatically**. Python automatically converts one data type into another when required, without the programmer explicitly converting it.

**Example:**'''


a = 4
b = 5.5
c = a + b

print(c)
print(type(c))


'''Here, `a` is an `int` and `b` is a `float`. Python automatically converts `a` to a `float` while performing the operation, so `c` is also a `float`.'''

'''**Explicit Type Conversion:**
Explicit type conversion is a conversion in which **we manually change the data type** using built-in functions such as `int()`, `float()`, `str()`, etc.

**Example:**'''

x = "10"
y = int(x)
z = y + 9

print(z)


'''Here, the string `"10"` is manually converted into an integer using the `int()` function.

---'''

### 3. What are operators in Python? Explain any three types with examples.

'''**Operators:** Operators are symbols that we use to perform operations on operands.

There are several types of operators in Python:

1. Arithmetic operators
2. Logical operators
3. Assignment operators
4. Comparison operators
5. Identity operators
6. Membership operators'''

#### 1. Arithmetic Operators

'''Arithmetic operators are used to perform mathematical operations such as **addition, subtraction, multiplication, division, floor division, and modulus**.'''

#### 2. Logical Operators

'''Logical operators are used to perform logical operations on **conditions** using `and`, `or`, and `not`.'''

#### 3. Assignment Operators

'''Assignment operators are used to **assign values to variables**.'''

#### 4. Comparison Operators

'''Comparison operators are used to **compare two values** and return either `True` or `False`.'''

#### 5. Identity Operators

'''Identity operators are used to check whether **two variables refer to the same object**.'''

#### 6. Membership Operators

'''Membership operators are used to check whether **an item exists in a sequence or collection**.

---'''

### Example of Arithmetic Operators


a = 1
b = 80

print(a + b)
print(a - b)
print(a / b)
print(a % b)
print(a // b)


### Example of Comparison Operators


print(a > b)
print(a < b)
print(a >= b)
print(a <= b)
print(a == b)
print(a != b)


### Example of Logical Operators

print((a > b) and (a < b))
print((a > b) or (a < b))
print(not((a > b) or (a < b)))


### Example of Assignment Operators

a += b
print(a)

a -= 9
print(a)

b *= 3
print(b)

a /= b
print(a)

a %= 5
print(a)

