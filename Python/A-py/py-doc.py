
# Reiu's Python Documentation of Python main library.

'''

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
-                                                                             -
-    Scan and read what you need, this might come in handy for a refresher.   -
-                                                                             -
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

'''

# Well, throughout learning python and compared to other programming languages. Python utilizes indentations rather than using -
# curly braces in grouping a code. (ALWAYS TAKE NOTE OF THAT)

'''

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
-                                                                             -
-           Python Roadmap: This is for every beginners out there.            -
-                                                                             -
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

'''
# Python Coding Skillset:

'''
 
    Starter Roadmap:

    - Variables, Numbers, Strings, and Lists
    - Dictionary and Tuple
    - If and For control blocks
    - Functions/Methods
    - File Handling
    - Modules

    Intermediate Roadmap:

    #Includes OOP

    - Exception Handling
    - Classes and Objects
    - Inheritance
    - Iterators
    - Generators
    - List/Dict Comprehensions

    Advanced Roadmap:

    

'''


'''

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
-                                                                             -
-                           1. PYTHON COMMENTS                                -
-                                                                             -
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

'''

# For a single line comment we use "#" or the hashtag then we type our comment like this one as an example.

# For a multiple line comment use double-triple quotation marks, one example of a multi-line comment is the one that is shown above.

# Another example for multi-line comment:

'''

 This is a multi-line comment,
 I like to eat pizza.
 
'''

# Just the basic stuff, move on further..

'''

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
-                                                                             -
-                               2. VARIABLES                                  -
-                                                                             -
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

'''

# To create a variable, simply issue a value on a potential variable you're working with.

# For example:

# We assigned a 'int' or integer value in 'x' which is 10. Therefore it is now a variable but a int variable.
x = 10

# We assigned a string value inside the variable so therefore it is now a 'str' or string variable.
word_of_the_day = "None shall pass."

# As a general rule of thumb, you cant combine an 'int' variable with a 'str' variable. Don't be a dumbass okay?

'''

 [2.1]::[ VARIABLE NAMES : GENERAL RULE OF THUMB IN NAMING YOUR VARIABLES ]

'''

'''

       A variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume). Rules for Python variables:


            - A variable name must start with a letter or the underscore characte

            - A variable name cannot start with a number

            - A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )

            - Variable names are case-sensitive (age, Age and AGE are three different variables)

'''

# Here are some valid variable names by incorporating the general rules in naming a variable:

samplevar = "This is a sample variable."
sample_var = "This is a sample variable."
_sample_var = "This is a sample variable."
sampleVar = "This is a sample variable."
SAMPLEVAR = "This is a sample variable."
sampleVar1 = "This is a sample variable."

# And here are some of the invalid variable naming that you SHOULD avoid:

# 2samplevar = "This is a sample variable."
# sample-var = "This is a sample variable."   # If you remove the comment tags you will see that it showed some errors so that is why you should incorporate the naming rules.
# sample var = "This is a sample variable."

# And an example of multiple variable names:

# -- Camel Case:

myVariableName = "Reiu"

# -- Pascal Case:

MyVariableName = "Reiu"

# -- Snake Case:

My_Variable_Name = "Reiu"
