# -Basic-python-repo

# what is python?
Definition: python is a high-level,interpreted programming language.
Python is a general-purpose programming language that emphasizes code readability, simplicity, and ease of writing. Created by Guido van Rossum and released in 1991, it has become one of the world's most popular languages, especially in fields like data science, web development, automation, and artificial intelligence Python is called an interpreted language because it executes code logic directly, line by line, without the need for a separate compilation step. In methods to compiled languages like C or C++, where the source code is translated into machine code before execution, Python code is translated into intermediate code by the Python interpreter. 
# Example: 
print("Hello World!") 
#output: Hello World!
# Used of python: 
develop software, 
analyze data,and
create AI/ML applications.
# Core features 
# Interpreted:
Python runs code line-by-line, which means it executes immediately without a separate compilation step, making debugging faster.Python is an Interpreted as well as Compiled language
Python is Interpreted as well as compilation language here, we will understand what does means by interpreted and compilation.
# Dynamically Typed: 
You do not need to declare variable types (like integer or string) ahead of time; Python determines them automatically at runtime.
# Readable Syntax: 
It uses clean, English-like words and relies on mandatory whitespace indentation to define code blocks instead of curly braces {} or semicolons ;.
## Source Code
In Python, the supply code is written in undeniable textual content documents with a .Py extension. These documents incorporate human-readable code this is written the use of Python's syntax and language features.
# Python Data Types 
Data types in Python define the type of value stored in a variable and determine the operations that can be performed on that data. Since Python treats everything as an object, each value is associated with a specific data type.

Helps the interpreter understand how to store and process different kinds of data efficiently.
Enables correct operations by ensuring only valid actions are performed on compatible data types.
<img width="800" height="369" alt="image" color="gray" src="https://github.com/user-attachments/assets/4b2f7004-cae4-4346-9f7e-0aa906ccba49" />
Below code assigns different types of values to variable x. With each new assignment, the previous value is replaced and x changes to the new data type.

### x = 50
### x = 20.92
### x = "hello everyone"
### x = ["haw","are","you"]
### x = ("this is my github page")
### x = "hello everyone"
## Numeric Data Types
In, Python Numeric data types are used to store numeric values. It can be an integer, floating number or even a complex number. It supports three main numeric types:
#### ntegers: value is represented by int class. It contains positive or negative whole numbers (without fractions or decimals).
#### Float: value is represented by float class. It is a real number with a floating-point representation. It is specified by a decimal point.
#### Complex: It is represented by a complex class. It stores numbers with real and imaginary parts. For example: 2+3j




### a = 5
### b = 5.0
### c = 2 + 4j
​
### print(type(a))
### print(type(b))
### print(type(c))

Output
### <class 'int'>
### <class 'float'>
### <class 'complex'>
# Sequence Data Types
A sequence is an ordered collection of items, which can be of similar or different data types. Elements in a sequence can be accessed using indexing.

## 1. String
Strings are used to store text data. A string is represented using the str class and can be created using single, double or triple quotes.





### s = 'Welcome to my github'
### print(s)
### print(type(s))
​
# access string with index
### print(s[1])
### print(s[-1])

Output
### Welcome to my github 
### <class 'str'>
### e
### b
## indexing Types & syntax for string - "python"

## 2. List
Lists are ordered and mutable collections used to store multiple items in a single variable. Elements in a list can be of different data types and are accessed using indexing.





### a = [1, 2, 3]
### print(a)
​
### b = ["thanks", "For", "reading", 4, 5]
### print(b[3])
### print(b[-3])

Output
### [1, 2, 3]
### 4
### reading
## 3. Tuple
Tuples are ordered and immutable collections used to store multiple items in a single variable. Once created, tuple elements cannot be modified and are accessed using indexing.

# Note: A tuple with a single element must include a trailing comma, otherwise Python treats it as a normal value instead of a tuple.
### t1 = (1,)
### print(type(t1))
​
### t2 = ('github', 'For', 'github', 1, 2)
### print(t2[3])
### print(t2[-3])

Output
### <class 'tuple'>
### 1
### github
# Boolean Data Type
Boolean data type represents one of two values: True or False. It is mainly used in conditions and comparisons and is represented by the bool class.
### print(type(True))
### print(type(False))

Output
### <class 'bool'>
### class 'bool'>
### Truthy and Falsy Values
truthy and falsy values are values that evaluate to True or False in a Boolean context. Truthy values behave like True, while falsy values behave like False when used in conditions.

### if 1:
  ###   print("1 is truthy")
​
### if not 0:
 ###   print("0 is falsy")

Output
### 1 is truthy
### 0 is falsy
# Set Data Type
Sets are unordered and mutable collections used to store unique elements. Since sets are unordered, elements cannot be accessed using indexing. Elements are usually accessed by iterating through the set using a loop.

### s1 = {"a", "a", "b", "c", "b"}
### print(s1)
​
### s2 = {"Github", "For", "Github"}
### for i in s2:
###    print(i)

Output
### {'b', 'a', 'c'}
### Github
### For
## Note: Sets in Python are unordered, so the order of elements when printed may vary each time the code is run.

## Dictionary Data Type
Dictionaries are used to store data in key:value pairs. Each key in a dictionary must be unique and values are accessed using their keys with square brackets [] or get() method.

# Note: Dictionary keys are case sensitive, the same name but different cases of Key will be treated distinctly. 
### d = {1: 'github', 2: 'For', 3: 'github'}
### print(d[1])    
### print(d.get(2))

Output
### github
### For
