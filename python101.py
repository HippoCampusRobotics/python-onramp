# %% [markdown]
# # Introduction to Python, Numpy, and some useful tips.
# This notebook serves as a mini-tutorial to introduce Python and some of the libraries and tools used in this course. You will encounter many of them repeatedly in the following assignments.
# In this notebook, there are text blocks and code blocks, with the code blocks providing a way to code directly within the text. Everything within them is just **regular Python code**.
# They usually contain addiotional knowledge or tips that are not necessarily relevant in this very moment for completing the tasks in the notebook.
# <div class="alert alert-block alert-info">
# The blue boxes are <b>info</b> boxes. They usually contain additional knowledge or tips that are not necessarily relevant for completing the tasks in the notebook.
# </div>
#
# <div class="alert alert-block alert-warning">
# The orange boxes always indicate <b>short tasks</b>. Below them, you will usually find empty code blocks where you should complete the tasks.
# </div>

# %%
# Python Playground - This is the empty code block mentioned above.
# TODO Code & Conquer - Unleash your inner coding warrior and dominate the digital realm one line of Python at a time!


# %% [markdown]
# # Usage
# The easiest way to use this notebook is to select the first text block by clicking on it a single time.
# And subsequently, move forward to the next block by hitting Shift+Enter. 
# If the current block was a code block it gets executed. and the output will be printed below.
# <div class="alert alert-block alert-info">
# You can identify code blocks by the square brackets on the left, i.e. <code>[ ]</code>
# </div>

# %% [markdown]
# ## 1. "Hello, World!" ##
# But let's start with the basics. This is what “Hello, World!” would look like in Python:

# %%
print('Hello World!')

# %% [markdown]
# ## 2. Declaring variables and their handling 
#
# ### 2.1 Declaring variables
#
# Unlike in many other programming languages, no variable types need to be declared in Python. The data type is only determined by assigning a value:

# %%
a = 2
b = 'I want 1000 BlueROVS'
print('a is of type: ', type(a), ' with the value: ', a)
print('b is of type: ', type(b), ' with the value: ', b)

# %% [markdown]
# __Pro Tip: F-Strings__ <br> Usually, it's better to use F-Strings, also known as format strings, because they allow you to directly embed variables or expressions within the string, unlike traditional strings: <br>
#
# <code> print(f'a is of type: {type(a)} with the value {a}') </code><br>
#
# The big advantage is that <b>single quotes '...'</b> only appear once, and variables can be referenced using <b> curly braces {...}</b>.
#
# <div class="alert alert-block alert-warning"> <b>🔽 Your Turn: 🔽</b> <br><br>
# Try using <b>F-Strings</b> in the code block right below, initialize different variable types, and see what happens when you run the script again. <br> You can either click on <b>"Run All"</b> in the navigation above,<br> <left><img src="figures/excecuteall.png" width="300"><br> or on the <b>triangle ▷ on the left</b> next to the code block itself :D<br> <left><img src="figures/excecutecell.png" width="200"> </div>

# %%
# ENTER YOUR CODE HERE!

# %% [markdown]
# ### 2.2 Arithmetic operations
#
# work in the same way as in most programming languages with
#  - addition `+`
#  - subtraction `-`
#  - multiplication `*`
#  - division `/`.

# %%
# With ** you can raise values to a power

solution = 3**2 * 2
print(solution)

# %% [markdown]
# So much for the basics.

# %% [markdown]
# ## 3. ✨ Numpy ✨ ##
# <div class="alert alert-block alert-info">
# <b>You have already worked with Matlab before? </b> In that case the following website could be quite helpful for you <a href="https://numpy.org/doc/stable/user/numpy-for-matlab-users.html">NumPy for Matlab Users</a> <br>
# Equivalent code examples are listed here in tabular form and the relevant differences between the two languages are highlighted.
# </div>
#
# Unlike many other programming languages, Python's standard library does not provide explicit array data types. Instead, lists are typically used to represent arrays.
#
# That’s why we have <b><code>NumPy</code></b> (Numerical Python), an additional library that we will use in this course. It is particularly useful when dealing with large datasets, as operations are executed faster and memory is used more efficiently. Additionally, <code>NumPy</code> offers an extensive library of functions for statistical, algebraic, and mathematical operations on arrays, which eliminates the need for explicit loops in many cases and makes the code cleaner and faster.
#
# <div class="alert alert-block alert-info"> There is very detailed documentation online on all the functionalities of the library elements with code examples. It is generally worthwhile to quickly check the documentation if you're unsure about the syntax or input variables, or if you're looking for a specific element.<br> <a href="https://numpy.org/doc/stable/reference/routines.array-creation.html">NumPy Documentation</a> <br> Alternatively, you can also hover your mouse over the function to see possible inputs for the function. </div></br>
# To take full advantage of NumPy, we first need to import it:

# %%
import numpy

# %% [markdown]
# You only need this line of code once within a document, and it is usually written right at the beginning. <br>
# Now, we can get started:

# %%
# Simple NumPy array in row form
row_vector = numpy.array([1, 2, 3, 4, 5])

# Defining matrices
matrix1 = numpy.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matrix2 = numpy.array([[1, 0], [0, 0]])

# %% [markdown]
# <div class="alert alert-block alert-warning"> 
# <b>🔽 Your Turn: 🔽</b><br>
# With <b>@</b> you can <b>multiply matrices</b>. Try it out below by defining a new <code>matrix3</code> of appropriate size, and then multiply it with <code>matrix1</code>. 
# </div>

# %%
# ENTER YOUR CODE HERE
# TODO define matrix3 and multiply it with matrix1

# %% [markdown]
# __Pro Tip: Using Libraries Properly__ <br>
# You’ve probably noticed that every element from the NumPy library above is always prefixed with <code>numpy.</code>. That seems a bit annoying in the long run, right? <br>
# There’s an __easier__ way by using:
#
# <code>import numpy as np</code>,<br>
#
# where <code>np</code> (theoretically) can be replaced by any other abbreviation or "alias." From then on, you can access the library more easily: <code>np.name</code>
#
# <div class="alert alert-block alert-warning"> 
# <b>🔽 Your Turn: 🔽</b><br>
# Import <code>numpy</code> using the alias <code>np</code>!
# </div>

# %%
# ENTER YOUR CODE HERE
# TODO: import numpy and use it with the alias 'np'

# %% [markdown]
# <div class="alert alert-block alert-info"> 
# If you only need to access specific elements of a library, it can be useful to import them explicitly: <br>
# <code>from numpy import sinc, pi</code> In this case, <code>sinc()</code> (sine function) and <code>pi</code>. The big advantage is that <code>sinc()</code> and <code>pi</code> can now be called directly without needing the library name.
# </div> 
# <div class="alert alert-block alert-warning">
# <b>🔽 Your Turn: 🔽</b> <br>
# Calculate the inverse of the following matrix.<br>
# Check the online documentation for NumPy for help: <a href="https://numpy.org/doc/stable/reference/routines.array-creation.html">NumPy Documentation</a> <br>
# </div>

# %%
# ENTER YOUR CODE HERE

# np.random.rand(rows, cols) generates a random matrix of a defined size
A = np.random.rand(3,3)
print(f'A = {A}')

A_inv = A # TODO this doesn't seem right yet
print(f'the inverse of A is A_inv = {A_inv}')

# %% [markdown]
# Now that we’ve teased the **powerful tools** of NumPy, it doesn’t seem all that impressive just yet. So, here’s a tiny selection to showcase its capabilities:

# %%
# ARRAY WITH ZEROS OF DIMENSION 2X3
zero_matrix = np.zeros((2, 3))

# ARRAY WITH ONES OF DIMENSION 2X4
ones_matrix = np.ones((2, 4))

# ARRAY WITH ONES ON THE DIAGONAL AND ZEROS ELSEWHERE
eye_matrix = np.eye(3, 3)

# ARRAY OF A CERTAIN SIZE WITH UNINITIALIZED ENTRIES
empty_matrix = np.empty((2, 3))

# ARRAY WITH 50 EQUALLY SPACED VALUES BETWEEN 0 AND 5
t = np.linspace(0, 5, 50)

# ACCESSING INDIVIDUAL ELEMENTS
print(f'The first element in matrix1 is {matrix1[0, 0]} and is accessed with index 0')
print(f'The last element in matrix1 is {matrix1[-1, -1]} or {matrix1[2, 2]}')

# %%
# ELEMENTWISE MULTIPLICATION
print(f'the elementwise multiplication of matrix1 and eye_matrix is {matrix1*eye_matrix}')
    #(as a reminder: regular matrix multiplication with @)

# %%
# APPEND
    # create a new row array
new_row = np.array([[10, 11, 12]])
    # append new_row to Matrix1
print(np.append(matrix1, new_row, axis=0)) 
    # “axis=0” defines the axis along which new elements are to be added
    # if this argument is omitted, the entire array is “flattened” into a single row vector

# %% [markdown]
# ## 4. if else & for loops
#
# ### 4.1 if else
#
# In Python, if-else conditions allow different blocks of code to be executed based on the truth of a condition. While `if else` makes it clear that only one of the two blocks will be executed, multiple independent `if` conditions result in each condition being checked separately. This can be more inefficient in certain cases.
# Here is a simple example of `if else` that checks whether a number is positive, negative or zero:

# %% [markdown]
# number = 10
#
# if number > 0:
#     print(f'the number {number} is positive')
# elif number < 0:
#     print(f'the number {number} is negative')
# else:
#     print(f'the number {number} is negative or zero')

# %% [markdown]
# The `elif` stands for `else if` and can theoretically be used as often as you like.

# %% [markdown]
# ### 4.2 For Loops
# In Pyhton, `for` loops iterate over lists/arrays, which is why the syntax usually looks like this:

# %%
words = np.array((['a', 'big', 'water', 'tank']))

for i in words:
    print(i)

# %% [markdown]
# If you want to iterate over a numerical sequence with a starting and ending value, you can simply do so using `for i in range(start_val, last_val): ...`.

# %% [markdown]
# ## 5. Enumerate
# With `enumerate` you can enumerate elements from an array or a list and save them in a new array/list as a tuple.

# %%
words_enum = enumerate(words)
print(list(words_enum))

# %%
# start the enumeration at 2 (default is 0)
print(list(enumerate(words, 2)))

# %%
# Iteration and accessing the first tuple
for index, word in enumerate(words):
    print(index, word)

# %% [markdown]
# ## 6. Functions
# Among other advvantages, functions allow you to write code once and reuse it multiple times without repeating it and help break a large problem into smaller, manageable parts, making the code easier to understand, debug, and maintain.
#
# <div class="alert alert-block alert-warning">
# <b>🔽 Your Turn: 🔽 </b><br><br>
#
# Write a function, that extracts all <b>zeros</b> and <b>twos</b> out of the array <code> measure_data </code> and adds them to a new array <code> reduced_data </code> while enumerating them. At the end, print <code> reduced_data </code> with the numbers and the corresponding count.
#
# </div>

# %%
# Python Playground

# TODO define reduced_data as an empty array


# define function to process data
def my_function(measures):
    # TODO make sure reduced_data is accessible and can be manipulated within the function
    
    # TODO iterate over measures and extract zeros and twos in reduced_data


    reduced_data = measures # this doesn't seem right yet



# define Measure data array
measure_data = np.array([[0, 2, 3 ,5 ,1 ,0 ,4 ,3 ,2 ,0 ,1, 9, 6, 7, 8]])

# TODO call the function

# TODO print reduced_data and count its entrys along the way


# %% [markdown]
# ## 7. list comprehensions
#
# *"List comprehensions are like the Python way of saying, 'Why take the long way around when you can just teleport to your destination?'"*
#
# Here ist a quick example why


# %%
# Traditional way using a for loop
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squared_evens = []

for num in numbers:
    if num % 2 == 0:
        squared_evens.append(num ** 2)

print(squared_evens)

# %% [markdown]
# In this snippet, the goal is to square every even number of an original list `numbers` and save those squared numbers in a new list `squared_evens`.
# <div class="alert alert-block alert-info"> 
# You may have noticed that the syntax for <code>.append()</code> is slightly different here as opposed to <code>np.append</code>. That is because <code>.append()</code> ist more convenient when working with lists.
# </div> 
#
# And here comes the magic of list comprehensions: with just **one simple line of code** (instead of 4 in this case) we can accomplish the same thing:

# %%
# Simplified version using list comprehension
SQUARED_EVENS = [num ** 2 for num in numbers if num % 2 == 0]

print(SQUARED_EVENS)

# %% [markdown]
# As you can see, list comprehensions are concise, allowing you to perform tasks in a single line, making the code cleaner and easier to read. Despite their brevity, they clearly express the operation, and they are often more efficient than traditional loops due to their optimization for such tasks.
#
# <div class="alert alert-block alert-warning">
# <b>🔽 Your Turn: 🔽 </b>
#
# Convert a list of distances from feet to metres using list comprehension if the original distance is equal to or below 100 ft.
# </div>
#
# **Hint:** the formula for transferring distances from feet to metres is:
# $$ [m] = {{[ft]} \over 3.281} $$

# %%
# python playground

# distances in feet
feet = [70, 50, 102, 68, 86, 104, 100]

# TODO convert feet to metres if <= 100
metres = feet # this doesn't seem right yet
