 

![](https://upload.wikimedia.org/wikipedia/commons/thumb/0/0a/Python.svg/640px-Python.svg.png)

<div align="center"> MINI GUIDE - PYTHON FUNDAMENTALS :snake: :woman_technologist:   </div align="center">   



***VARIABLES***

In Python, variables are used to store and manipulate data. Here are some key points about variables:

Variable Assignment: To assign a value to a variable, you use the assignment operator (`=`). For example, `x = 5` assigns the value 5 to the variable `x`.

Dynamic Typing: Python is a dynamically typed language, which means you don't need to explicitly declare the data type of a variable. The type of a variable is inferred based on the value assigned to it.

Variable Naming: Variable names in Python can contain letters, numbers, and underscores. They must start with a letter or an underscore, and they are case-sensitive. It's good practice to use descriptive names that reflect the purpose of the variable.

Variable Reassignment: You can change the value of a variable by assigning a new value to it. For example, `x = 10` changes the value of `x` from 5 to 10.

Variable Scope: The scope of a variable determines where it can be accessed in your code. Variables can have either global scope (accessible throughout the program) or local scope (accessible only within a specific block of code).

Variable Naming Conventions: Python follows the snake_case naming convention for variables, where words are separated by underscores. For example, `my_variable` is a valid variable name.



**DATA TYPES**

In Python, there are several built-in data types that you can use to store and manipulate different kinds of data. Here are some of the most common data types:

Numeric: Python supports different types of numeric data, including integers (`int`), floating-point numbers (`float`), and complex numbers (`complex`).

String: Strings (`str`) are used to represent text in Python. They are enclosed in either single quotes ('') or double quotes ("").

Boolean: Boolean data type (`bool`) represents either `True` or `False`. It is often used for logical operations and conditional statements.

List: Lists (`list`) are ordered collections of items. They can contain elements of different data types and can be modified (mutable).

Tuple: Tuples (`tuple`) are similar to lists, but they are immutable, meaning their elements cannot be changed once defined.

Dictionary: Dictionaries (`dict`) are key-value pairs that allow you to store and retrieve data based on unique keys. They are unordered and mutable.

Set: Sets (`set`) are unordered collections of unique elements. They are useful for performing mathematical set operations like union, intersection, and difference.
 

**STRINGS** 

Strings are used to represent text in Python, and they are enclosed in either single quotes ('') or double quotes (""). Here are some key points about strings:

String Concatenation: You can concatenate, or join, two or more strings together using the `+` operator. For example, `"Hello" + "World"` would result in the string "HelloWorld".

String Indexing: Each character in a string has an index, starting from 0. You can access individual characters of a string using square brackets and the index. For example, `"Python"[0]` would return the character 'P'.

String Slicing: You can extract a portion of a string using slicing. Slicing allows you to specify a range of indices to extract a substring. For example, `"Hello World"[6:11]` would return the substring "World".

String Length: You can find the length of a string using the `len()` function. For example, `len("Python")` would return 6.

String Methods: Python provides many built-in methods to manipulate and work with strings. Some common string methods include `lower()`, `upper()`, `replace()`, `split()`, and `strip()`. These methods allow you to perform operations like converting case, replacing characters, splitting a string into a list, and removing whitespace.

String Formatting: Python provides different ways to format strings, including the `format()` method and f-strings. These allow you to insert variables or values into a string in a formatted way.



***LOOPS***   

For loops in Python are used to iterate over a sequence of elements, such as a list, tuple, or string. They allow you to perform a set of actions repeatedly for each item in the sequence.

Here's an example of a for loop in Python that prints each element of a list:

```python
my_list = [1, 2, 3, 4, 5]

for item in my_list:
    print(item)
```

In this example, the variable `item` represents each element in the `my_list` sequence. The loop will iterate over each element in the list and print it.

For loops can also be used with other sequences, like strings. Here's an example:

```python
my_string = "Hello, World!"

for char in my_string:
    print(char)
```

This loop will iterate over each character in the string and print it.

You can also combine for loops with other programming concepts, like conditional statements, to perform more complex operations within the loop.

While loops in Python allow you to repeatedly execute a block of code as long as a certain condition is true. They are useful when you don't know in advance how many times the loop will run.

Here are some key points about while loops:

1. The loop condition is checked before each iteration. If the condition is true, the code inside the loop is executed. If the condition is false, the loop is exited and the program continues with the next statement.

2. The syntax of a while loop in Python is as follows:

```python
while condition:
    # code to be executed
```

3. The condition can be any expression that evaluates to either True or False. It is checked at the beginning of each iteration.

4. Inside the loop, you can perform any desired actions, such as updating variables, performing calculations, or printing output.

5. It's important to ensure that the condition eventually becomes false; otherwise, you may end up with an infinite loop, which will cause your program to run indefinitely.

Here's an example of a while loop that counts from 1 to 5:

```python
count = 1

while count <= 5:
    print(count)
    count += 1
```

In this example, the loop starts with `count` equal to 1. The loop will continue to execute as long as `count` is less than or equal to 5. Inside the loop, the current value of `count` is printed, and then `count` is incremented by 1.
   

  
***COLLECTIONS***    
Collections in Python are data structures that allow you to store and manipulate groups of related data. They provide various ways to organize, access, and modify data efficiently.

Here are some key points about collections in Python:

Lists: Lists are ordered collections that can hold any type of data. They are mutable, meaning you can modify their elements. You can access elements by their index, and lists support various operations like appending, removing, and sorting.

Tuples: Tuples are similar to lists, but they are immutable, meaning you cannot modify their elements once defined. They are often used to represent a collection of related values that should not be changed.

Sets: Sets are unordered collections of unique elements. They do not allow duplicate values. You can perform set operations like union, intersection, and difference. Sets are useful for removing duplicates or checking membership.

Dictionaries: Dictionaries are key-value pairs that allow you to store and retrieve data based on a unique key. They are unordered and mutable. You can add, modify, or delete key-value pairs. Dictionaries are efficient for looking up values based on their keys.

Arrays: Arrays are collections of elements of the same type. They are more efficient than lists when dealing with large amounts of numeric data. Arrays are provided by the `array` module in Python.

Collections module: The `collections` module in Python provides specialized data structures like `deque`, `Counter`, `defaultdict`, and `OrderedDict`. These data structures offer additional functionalities beyond the built-in collections.

These collections provide flexibility and efficiency when working with different types of data in Python. Each collection has its own characteristics and use cases, so choosing the right one depends on your specific needs.


***FUNCTIONS***  

Functions in Python are blocks of reusable code that perform a specific task. They allow you to organize your code, make it more modular, and avoid repetition.

Here are some key points about functions in Python:

Functions are defined using the `def` keyword, followed by the function name and parentheses. Any input parameters are specified within the parentheses.

The code inside a function is indented and can contain any valid Python statements.

Functions can have a return statement to send a value back as the result of the function's execution. If there is no return statement, the function returns `None` by default.

You can call a function by using its name followed by parentheses. If the function has input parameters, you provide their values within the parentheses.

Functions can be defined with default parameter values. These values are used if the caller does not provide specific values for those parameters.

You can pass arguments to a function by position or by keyword. Positional arguments are passed based on their position, while keyword arguments are passed with the parameter name.

Functions can also have docstrings, which are string literals used to document the function's purpose, inputs, and outputs. They are enclosed in triple quotes and can be accessed using the `__doc__` attribute.

Here's an example of a function that adds two numbers together:

```python
def add_numbers(a, b):
    return a + b
```

In this example, the function `add_numbers` takes two parameters, `a` and `b`, and returns their sum.

To call this function and get the result, you would do something like:

```python
result = add_numbers(3, 5)
print(result)  # Output: 8
```


I'm on linkedin, if you'd like to connect :smile: [![Badge](https://img.shields.io/badge/Linked-in-blue)](https://www.linkedin.com/in/sahra-a-91142b173?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=ios_app)


