'''Python store and execute code line by line'''
'''Variable store reference in memory'''
'''Input always returning string'''
#EXRESSION & STATEMENT

#EXPRESSION:---->
'''Expression is a combination of operator and operand
example:-->
x = 10[not expression]
x+3[(x+3)--> expression],[(+)--> Operand],[(x,3)--> operator] 
and this also return value'''

# A program is the series of statement 
'''Many statements contain one or more expressions, 
 but a statement is an instruction executed by Python.'''

#Many statements contain one or more expressions, but a statement is an instruction executed by Python.

#COMMENT--->
'''Every thing after hash(#) is consider as comment, we can also comment something by using three single quotes '''

'''A comment is text written in your Python code that is ignored by Python when the program runs. It's mainly there for humans to explain the code.

You create a single-line comment using #:'''

# This is a comment
x = 10

'''Python sees # This is a comment and doesn't execute it.
You can also put a comment after code:
x = 10  # Storing 10 in x
How does it relate to expressions and statements?
x = 10 → statement
10 → expression
# Storing 10 in x → comment
So a comment is neither an expression nor a statement. It's simply explanatory text for the programmer.'''

#INDENTATION:-

'''Indentation means the spaces at the beginning of a line of code.

In Python, indentation is used to show which statements belong to a particular block of code.

For example:

if x > 5:
    print("x is greater than 5")
    print("This is also inside the if")

The spaces before the two print() statements tell Python:

These statements belong to the if block.

Usually, Python uses 4 spaces for one level of indentation.

Without indentation ❌
if x > 5:
print("x is greater than 5")

Python will give an IndentationError because it expects the code belonging to if to be indented.

Multiple levels
if x > 5:
    if x > 10:
        print("x is greater than 10")

Here:

if x > 5: → level 0
if x > 10: → level 1
print() → level 2

So you can think of indentation as creating blocks/hierarchy in your code.

One important distinction

Indentation itself is not a statement or expression.

It's a way Python's syntax represents code blocks.

For example:

if age >= 18:
    print("Adult")
age >= 18 → expression
if ...: → if statement
print("Adult") → expression statement
the spaces before print() → indentation'''
