#!/usr/bin/env python
# coding: utf-8

# # Beginner-friendly python for GIS: A hands-on journey to satellite imagery

# ## Workshop Goals
# 
# In this workshop we will learn:
# 
#     - What is Python and how it works (this morning)
#     - What is GIS data (this morning still)
#     - What is vector data, and how to manipulate it (this afternoon)
#     - What is raster data, and how to manipulate it (tomorrow morning)
#     - How to use satellite imagery to produce usable data (tomorrow afternoon)
# 
# We are embarking in an ambitious and intense journey. It is going to feel like a lot.

# ## Workshop Organization
# 
# The way we'll organize:
# 
#     - As much as possible we need to move altogether in the workshop.
#     - It means everyone must be able to live understand and code while we have the class.
#     - We'll thus make frequent breaks, that will allow for persons experiencing difficulty to come up to me and to solve whatever issue they may face.
# 
# Since we're doing project oriented programming from this afternoon onwards, if it feels easy, do not hesitate to go ahead with the project and to improve it!

# ## A bit about me
# 
# I am not a computer scientist but a social scientist.
# I have worked with GIS data in my research.
# 
# In this class, I will teach GIS and Python from a practitioner's perspective:
# 
# - focusing on real research workflows
# - using Python as a tool for spatial analysis
# - not from a software engineering perspective
# 
# Do not expect from this class to understand the geometry of projections and coordinate reference systems. We'll make sure we understand these concepts not to make mistake, but won't go into the math.

# ## Why Python?
# 
# Some of you may already know GIS software such as **QGIS** or **ArcGIS**.
# These tools rely on a **Graphical User Interface (GUI)**.
# 
# GUI GIS tools are extremely useful, especially for:
# 
# • exploring spatial data  
# • visualizing maps  
# • performing quick analyses  
# 

# However, they are less well suited for **integrated analytical workflows**.
# 
# Main limitations of GUI workflows:
# 
# - **Reproducibility**: point-and-click operations are harder to document and replicate.
# - **Automation**: repeating the same operation on many datasets can be cumbersome.
# - **Integration**: linking spatial analysis with statistics or data science tools is limited.
# 
# Python helps address these issues by allowing us to build **scripted and reproducible workflows**.
# 
# GUI tools and Python are **complementary rather than substitutes**.
# 
# In this course we focus on Python because it allows more flexible and reproducible spatial analysis (although it is initially harder to learn).

# ## Python and LLMs
# 
# The good thing when you learn Python is that now you've got LLMs:
# 
#     - Whatever trouble you have, LLMs can now help you figure out what's wrong.
#     - Whenever you have a bug, just copy-paste code and bug to self-solve with LLMs.
# 
# It greatly decreased the entry cost into Python. But also on GIS:
# 
#     - LLMs work extremely well as a side-kick for GIS management.

# ## Python
# 
# One surprising aspect of Python is that the hardest part is often the **installation**, **setup** and **package management**.
# 
# Unlike software such as Stata or Matlab, Python is an **ecosystem** rather than a single program.
# 
# As in R, for those of you familiar with it, there is a distinction between:
# 
# - **The language / interpreter** (Python itself)
# - **The development environment (IDE)** used to write and run code
# 
# In R, most users rely on **RStudio**.
# 
# In Python, there is no single standard environment — several options exist
# (e.g. Jupyter, VS Code, Spyder, PyCharm).
# 
# This morning we will spend some time making sure everyone has a **working Python setup**.

# Python is not a single program.
# 
# A typical Python setup includes:
# 
# - A version ofPython
# - a development environment (Jupyter, Spyder, Visual Studio Code...)
# - packages (pandas, geopandas, numpy…)
# 
# For this class, we'll be using **Miniconda**, it allows you to navigate the **Python ecosystem** easily:
# 
# - Python
# - a package manager (conda)
# - many scientific packages
# - development environments (Jupyter, Spyder)
# - Virtual environments
#     

# <p align="center">
# <img src="images/tikz_graph.svg" width="700"  style="display:block; margin:auto;">
# </p>

# We will use **Miniconda** to manage Python environments.
# 
# Download Miniconda here:
# 
# https://www.anaconda.com/download
# 
# You normally don't have to Sign Up (sorry if you do).
# 
# Choose the installer for your system:
# 
# - Windows → Miniconda3 Windows 64-bit installer
# - Mac → Miniconda3 MacOS installer
# - Linux → Miniconda3 Linux installer

# 
# <p align="center">
# <img src="images/start_anaconda_site.png" width="1400"  style="display:block; margin:auto;">
# </p>
# 

# 
# <p align="center">
# <img src="images/miniconda_dl.png" width="1400"  style="display:block; margin:auto;">
# </p>
# 

# ## Using Miniconda
# 
# 
# Miniconda is typically used through a command-line interface (CLI).
# 
# - On Windows, you can access it by opening the `Anaconda Prompt`
# - On macOS, you can use the standard `Terminal`
#     - Apple: Cmd + Space > type `Terminal` (or go to applications to find it)
# 
# The Anaconda Prompt is simply a terminal window that is pre-configured to use conda commands.
# 
# 
# <p align="center">
# <img src="images/conda_prompt.png" width="700"  style="display:block; margin:auto;">
# </p>
# 
# 

# <p align="center">
# <img src="images/tikz_graph.svg" width="700"  style="display:block; margin:auto;">
# </p>

# ## Create a virtual environment
# 
# To create a virtual environment you can first type inside the terminal:
# 
# `conda create -n gis_workshop python=3.11`
# 
# This create a new environment named gis_workshop with a specific python version.
# 
#     - Then we want to step in the environment, and start installing stuff in it.
#     
# `conda activate gis_workshop`
# 
# <p align="center">
# <img src="images/base_anaconda.png" width="700">
# </p>
# 
# <p align="center">
# <img src="images/gis_workshop_anaconda.png" width="700">
# </p>
# 
# 

# <div style="text-align: center;">
# <img src="images/first_environment_step.svg" width="700" style="display:block; margin:auto;">
# </div>

# ## Choosing an IDE
# 
# Before moving on, you need to choose a **development environment (IDE)** to write and run Python code.
# 
# For this class, I recommend two options:
# 
# - **Jupyter**
# - **Spyder**
# 
# Both are good tools, especially for social science workflows.

# **Spyder**
# - similar to **RStudio** or **Matlab**
# - includes a **variable explorer**
# - includes an **interactive console** and a **code editor**
# - convenient for writing and debugging scripts
# 
# **Jupyter**
# - lightweight and very flexible
# - ideal for **notebooks combining code, results, and explanations**
# 
# Personally, I often use:
# - **Spyder for developing code**
# - **Jupyter for presenting results or building a final analysis**

# ## Setting Up Spyder
# 
# I strongly advise the ones of you from Stata/R to install Spyder. You usually install Spyder just one time:
# 
# <div style="text-align: center;">
# <img src="images/graph-spyder.svg" width="700" style="display:block; margin:auto;">
# </div>

# Install just one spyder version in the base environment:
# 
# <p align="center">
# <img src="images/base_spyder_install.png" width="700">
# </p>
# 
# Inside the environment then install spyder-kernels inside the conda:
# 
# <p align="center">
# <img src="images/spyder-kernels_install.png" width="700">
# </p>
# 

# ## Connecting Spyder to your environment
# 
# Tools > Preferences > Python Interpreter > Select interpreter
# 
# If you opt for this solution, you can manually connect to which-ever thing you want 
# 

# ## Jupyter Notebook / JupyterLab
# 
# Another tool I recommend is Jupyter Notebook or JupyterLab (which are very similar in practice).
# 
# It can be installed in each environment and is relatively lightweight.
# 
# Jupyter is a powerful tool for several reasons:
# 
# - It provides an effective way to present work by:
#     - Combining code cells with explanatory text
#     - Supporting images and mathematical equations
# - It allows you to organize a project into self-contained, interactive documents
# 
# However, it also has some limitations:
# 
# - The execution environment can be difficult to reproduce or manage
# - Harder modularization compared to `.py` files

# Following along the workshop can be done in three ways:
# 
# - Code on you own with spyder
# - Code on your own with jupyter notebook
# - Follow along the slide with an old jupyter notebook version.
# 
# I think the best way is probably spyder.

# # Break for installation

# In[2]:


# First create a variable
x = 25
# You can print that variable
print(x)


# If you're on Spyder, you should see the variable appear in the variable explorer tab

# In[7]:


# Create another variable
y = 5

# A whole range of operation is possible
print(x+y, "- addition")
print(x*y, "- multiplication")
print(x**y, f"- {x} at the power {y}")
print(x/y, f'- {x} divided by {y}') # division
print(x%y, f'the rest when {x} is divided by {y}') # remainder of the division


# Variables you create all have a specific `class` which can be found using function `type()`

# In[5]:


z = "salut"
# x,y are numbers whereas z is a string
print("the variable x's value is", x)
print("the variable z's value is", z)
print(type(x))
print(type(z))


# A useful feature of strings in python is that you can ask for objects to be evaluated and then considered as string

# In[4]:


print(f"the variable is {x}")
print("the variable is x")


# Functions are also objects you can find the class of

# In[10]:


# Printing the type of function print
print(type(print))


# In[8]:


# Printing the type of an empty evaluation of function print
print(type(print()))


# In[10]:


# Printing the type of a string called print
print(type("print"))


# Some operations are not compatible with all types of classes

# In[12]:


# Write two variables
x = 25
z = "salut"

# Strings and integers are different and cannot be combined
print(x + z)


# Classes can be changed.

# In[13]:


# Types of objects can be changed. I can change x to a string
x = str(x)
print(x)
print(type(x))


# In[14]:


# Strings and integers are different and cannot be combined
print(x + z)


# ## Boolean statements in Python
# 
# Boolean statements are logical statements, which may be very useful when doing programming.

# In[14]:


print(x)
print(y)
print(x == y)


# Booleans can be reversed with language:

# In[15]:


print(not x == y)


# In[16]:


print(x != y)


# Boolean are a very important part of programming with Python. They work just like logical statements

# In[18]:


x = False
y = True
z = True

print(x | y)
print((x | y) & z)
print(x & y)


# # If/Else Statements in Python
# 
# Boolean values (`True` / `False`) are essential because they allow your program to make decisions using **if/else statements.**
# 
# **In Python, indentation matters**
# 
# Indentation is not just for readability—it defines the structure of the code.
# It tells Python which instructions belong to a given condition.

# Basic structure
# 
# An if/else statement starts with a condition:

# In[70]:


condition = True
if condition:
    # code executed if the condition is True
    smthing = 1
else:
    # code executed if the condition is False
    smthing = 1


# - The indented block after if runs only if the condition is true
# - The else block is optional and runs otherwise
# - The block ends when the indentation stops

# Let's create an example here:

# In[19]:


if x == y:
    print("ça c'est bien")
else:
    print("c'est pas bien")


# **Why use if/else statements?**
# 
# If/else statements are useful when the value or state of a variable is uncertain before running the code. They allow you to define different actions depending on the conditions that arise.
# 
# In practice, you specify a set of anticipated cases and assign a corresponding behavior to each of them.
# 
# 
# **Rule-based logic ≠ AI**
# 
# During the early AI/ML boom, simple if/else programs were sometimes presented as “AI.” However, they are fundamentally different:
# 
# - The programmer explicitly defines how the code behaves in every possible case
# - The system does not learn or adapt beyond the predefined rules

# If/else statement can be defined for many many cases

# In[21]:


x = 5
y = 10


# In[38]:


if x == y:
    print('Perfect equality')
elif x > y:
    x = x - 1
    y = y + 1
    print('Wealth redistribution from x to y')
elif x < y:
    x = x + 1
    y = y - 1
    print('Wealth redistribution from y to x')
print(x)
print(y)


# # Loops in Python
# 
# Compared to software like Stata, Python provides a very intuitive way to write loops.
# 
# Loops allow you to repeat a set of instructions automatically, without rewriting the same code multiple times.
# 
# Why use loops?
# 
# - To iterate over a collection of elements (e.g., a list)
# - To perform repetitive tasks efficiently
# - To write cleaner and more concise code

# In[18]:


for ii in range(5):
    print(ii)


# Python starts counting at 0
# 
# In Python, indexing begins at 0 rather than 1. While this may feel unintuitive at first, it is a deliberate and widely adopted design choice in programming.
# 
# Why 0-based indexing?
# 
# - Memory alignment: In many languages, the index represents an offset from the first element. The first element is therefore at position 0 (no offset).
# - Simplicity in computation: Expressions like a[i] directly map to “start + i steps,” which simplifies implementation and improves efficiency.
# - Consistency across languages: Many major programming languages (like C programming language and Java) follow the same convention.

# In a loop, the code contained within the loop is run as many time as there are loop iterations 

# In[39]:


x = 5
for ii in range(5):
    x = x + 1


# In[40]:


print(x)


# The loop variable may be anything. Try in general to assign a name to it that allows another user to understand at first glance.

# In[81]:


x = 5
for ii in range(5):
    x = x + 1
print(x)


# In[82]:


x = 5
for loop_iterator in range(5):
    x = x + 1
print(x)


# Loops can feel a bit weird the first time you use them, it's not always clear when an object accumulates as in the previous example and when they do not.

# In[71]:


x = 5
y = 3


# In[72]:


for ii in range(5):
    x = y + 1


# In[73]:


print(x)


# Loops can also be defined given a `boolean` statement (True/False). In practice that means run the loop until a condition is met. Let's take our redistribution program.

# In[ ]:


if x == y:
    print('Perfect equality')
elif x > y:
    x = x - 1
    y = y + 1
    print('Wealth redistribution from x to y')
elif x < y:
    x = x + 1
    y = y - 1
    print('Wealth redistribution from y to x')
print(x)
print(y)


# Imagine we want to run the loop until full redistribution is achieved. We create a boolean loop

# In[53]:


x = 5
y = 9
# The condition is the loop goes on as long as x and y are not of the same value
while x != y:
    if x == y:
        print('Perfect equality')
    elif x > y:
        x = x - 1
        y = y + 1
        print('Wealth redistribution from x to y')
    elif x < y:
        x = x + 1
        y = y - 1
        print('Wealth redistribution from y to x')
print(x)
print(y)


# While loop may be a bit tricky because they can go infinite, when conceiving these loops, be careful to make sure the condition will always be satisfied after iterating long enough

# Loops and iterables in Python
# 
# In Python, loops are not limited to iterating over numerical ranges. They can iterate over any object that contains multiple elements—these are called iterables.
# 
# An iterable is any object that Python can traverse element by element (e.g., lists, strings, tuples, etc.).

# In[54]:


my_first_list = ["this", "is", "my", "first", "list"]


# In[57]:


print(my_first_list[0])


# Back to our first list!

# In[56]:


print(my_first_list[0])


# In[60]:


for item in my_first_list:
    print(item, end = " ")


# In loops we can also distribute several items. It suffices that an iterable is itself composed of another iterable

# In[61]:


other_list = [["Ceci", 1], ["N'est", 2], ["pas", 3], ['une', 4], ['pipe', 10]]

for word, number in other_list:
    print(word, end = " ")
    print(number)


# ## Small Exercise to start doing a bit of python: **FizzBuzz**
# 
# Go through numbers from 1 to 100, and for each number:
# 
# - print "fizz" if divisible by 3
# - print "buzz" if divisible by 5
# - print "fizzbuzz" if divisible by both
# - count how many times you print fizz, buzz and fizzbuzz
#     
# Create a simple code, we need a loop that goes to 100. And each iteration must have if/else statements.
# We'll need operation x%y for remainder of a division.

# ## Continuation exercise
# 
# Go through integers, and for each number:
# 
# - print "fizz" if divisible by 3
# - print "buzz" if divisible by 5
# - print "fizzbuzz" if divisible by both
# - count how many times you print fizz, buzz and fizzbuzz
#     
# Create a simple code, that indicates until how many integers one has to count to get 1000 fizzbuzz?

# # Introducing Functions
# 
# Python is a highly flexible language that allows you to define your own objects, classes, and functions.
# 
# In this course, we will primarily focus on functions as a way to structure and reuse code.
# 
# More advanced features, such as object-oriented programming, will not be covered.

# ## Defining a Function
# 
# To create a function in Python, use the `def` keyword, followed by a function name and parentheses.
# 
# The code inside the function must be indented. This indentation defines the body of the function.
# 
# The function ends when the indentation stops.

# In[83]:


def myfirstfunction():

    print('I just ran my first function')


# Notice the new variable in your environment!

# To run the function, we invoke it with parenthesis, otherwise we're just presenting to the code the object of the function itself

# In[84]:


myfirstfunction


# In[85]:


myfirstfunction()


# Whatever happens in a function stays there: a function creates its own environment which disappears with it

# In[86]:


def mysecondfunction():

    newvariable = 1

    print('I just ran my first function')


# In[87]:


mysecondfunction()


# In[88]:


print(newvariable)


# If you want to access a variable created in a function from outside the function, you need to let `return` the variable

# In[89]:


def mythirdfunction():

    newvariable = 1

    print('I just ran my first function')

    return(newvariable)


# In[90]:


variable = mythirdfunction()


# In[29]:


print(newvariable)


# In[30]:


print(variable)


# Function may take input, with which they can do stuff

# In[92]:


def mythirdfunction(x):

    newvariable = 10 + x

    print('I just ran my first function')

    return(newvariable)


mythirdfunction(6)


# ## Continuation Exercise: **FizzBuzz** in a function
# 
# Take the fizzbuzz example from before, embed it inside a function and have the function take an input corresponding to the length of the loop ran in fizzbuzz.

# ## Why Python is Great: Packages
# 
# On Python, for most of what you want to do: someone created a package! You practically never use Python without packages.
# 
# We'll use another package that's pre-distributed on python which is called `random`.

# In[99]:


import random

random.randint(0, 1)


# ## Randomness and Reproducibility in Python
# 
# Random numbers generated in Python are not truly random—they are pseudo-random.
# They are produced by deterministic algorithms that generate long sequences of numbers that appear random.
# 
# Why does this matter?
# 
# Because the sequence depends on an initial value called a seed.
# 
# - If you use the same seed, you will obtain the same sequence of “random” numbers
# - This is essential for reproducibility in research and data analysis

# In[110]:


random.seed(500)
random.randint(0, 1)


# ## Small exercise with `Random`: cointoss
# 
# Create a function taking into input an integer
# 
# - It should tell us how many time we obtain `Heads` following the input's number of cointoss.

# ## Continuation exercise with `Random`
# 
# Create a function taking into input an integer
# 
# - It should tell us how many time we had to do a cointoss to obtain the input's number of `Heads`

# Before we start with `GIS` packages, we'll deal with two base packages that are always useful to know: `numpy` and `pandas`.
# 
# To install the packages, go back to `anaconda`, make sure you remember activating your virtual environment and type:
# 
# - `conda install numpy`
# - `conda install pandas`
# 
# <p align="center">
# <img src="images/install_numpy.png" width="700">
# </p>

# Then each time we run a script, we need to import packages.
# 
# They are not imported by default because you might not want all packages to be `loaded` all the time.
# 
# Let's start with `Numpy`, the main package for matrixes and mathematical operations.

# In[94]:


import numpy

my_matrix = numpy.array([['oui', 1],
                       [3, 4]])

print(my_matrix)

print(type(my_matrix))


# Many packages are imported not with their actual name, deemed too long. For renowned package, everyone uses the same convention. `numpy` is always imported under the name `np`

# In[111]:


import numpy as np

my_matrix = np.array([['oui', 1],
                       [3, 4]])
print(type(my_matrix))


# Inside `np` lies the whole distribution of functions created by the writers of that package. np.array() is a function np.where() is another. They all have different uses.

# Let's apply together `numpy` and `random` for a bit of econometrics: we'll simulate a random dataset and leverage `numpy` to do `OLS` regression.
# 
# Let's say we want to simulate a dataset replicating the university premium.

# In[139]:


# First, let's draw the university of individuals in our sample
university = np.random.randint(0, 2, size=200)

# You can also compute the average share of women
print(100*np.mean(1-university), "% of the sample have a university degree")
print(university[:5])  # Print the first 5 individuals of our sample


# To visualize data, we need another package: `matplotlib`

# In[143]:


import matplotlib.pyplot as plt

# Now, for each individual, we want to sample a random productivity number
productivity = np.random.normal(20, 5, 200)

# Instantiate a figure
plt.figure()
plt.hist(productivity, bins=15,density=True, alpha=0.6, color='b')  # Make up some bins so we get some form of "density"
# Write title, xlabel and y alabel
plt.title('Density Plot of Productivity')
plt.xlabel('Productivity')
plt.ylabel('Density')

# Display the plot
plt.show()


# In[145]:


# Now that we have both university diploma and productivity, we can generate wages, and let's add an error
wages = 100 + 100*productivity + 50*university + np.random.normal(0, 50, 200)
print(wages[:5])


# We now have a dataset, for 200 individuals:
# 
# - their university diploma
# - their productivity
# - their wages
# 
# How do we estimate the parameters of the model?

# Ordinary Least Square (OLS)! The formula is 
# 
# $\hat \beta = (X'X)^{-1}X'y$
# 
# What is the matrix X?

# In[147]:


# Let's build the matrix X
constant = np.ones(200)
X = np.vstack((constant, productivity, university))
# Create a small display of it
print(X.shape)
print('Matrix X has', X.shape[0], 'rows and', X.shape[1], 'columns')


# In[148]:


# Usually, an observation will be a row, and a variable a column
X = X.T
print(X[:6, :])


# In[152]:


# The matrix Y we already have, it is the matrix of wages
Y = wages

# We are ready to do the regression
beta = np.linalg.inv(X.T @ X) @ (X.T @ Y)
print(beta.T)


# In[155]:


print('The estimated constant is', round(beta[0], 2), '€')
print('The estimated university premium is', round(beta[2], 2), '€')
print('The estimated productivity contribution to wages is', round(beta[1],2), '€')


# ## Small exercise
# 
# Put that whole dataset simulation inside of a function that takes into input the number of individuals to be sampled.

# Okay. That was a bit of numpy, it will be very useful when we go to `GIS` because it's at the core of a lot of its operations. We need yet another package before we go `GIS`: `pandas`.
# 
# `Pandas` is the package that allows you to manipulate datasets, it replicates to some extent the structure you would find in stata. It's matrixes with additional structure to make some operations easier.

# In[160]:


import pandas as pd

X,y = sample(300)

df = pd.DataFrame(X, columns = ['Intercept', 'Productivity', 'University'])
print(df)


# With pandas, data manipulation is bit easier

# In[161]:


df['wage'] = y
df


# In[163]:


df.groupby('University')['wage'].mean()


# Let's do some regressions without having to go by hand now. Let's install `statsmodels`

# In[165]:


import statsmodels.api as sm

# Add a constant
df['constant'] = 1

reg1 = sm.OLS(endog=df['wage'], exog=df[['constant', 'University']], missing='drop')
print(type(reg1))


# In[166]:


reg1 = reg1.fit()
reg1.summary()


# ## Small Exercise
# 
# Compute the required sample to have that the confidence interval of the university coefficient contain the true coefficient more than 95% of the time.
