# Variables are how we store data in our program. 
# In Python it is the norm to use "snake_case" when naming variables
player_health = 1000
print(player_health)

'''
Doing Math:

sum = a + b
difference = a - b
product = a * b
quotient = a / b

'''

armor_multiplier = 2
armored_health = player_health * armor_multiplier
# create armored_health here
print(armored_health)

'''
Basic Variable Types

In Python there are several basic data types.

String Type
"Strings" are raw text in coding speak. They are called "strings" because they are a list of characters strung together. Strings are declared in Python by using single quotes or double quotes. That said, for consistency's sake, we prefer double quotes.

name_with_single_quotes = 'boot.dev'
name_with_double_quotes = "boot.dev"

Numeric Types
Numbers aren't surrounded by quotes when created, but they can have decimals and negative signs.

Integers are numbers without a decimal
x = 5
y = -5

A "Float" is a number with a decimal
x = 5.2
y = -5.2

Boolean Type
A "Boolean" (or "bool") is a type that can only have one of two values: True or False. As you may have heard, computers really only use 1's and 0's. These 1's and 0's are just Boolean values.

is_tall = True
is_short = False

F-strings in Python
You can create a string with dynamic values by using f-strings in Python. It's a beautiful syntax that I wish more programming languages used.
'''
num_bananas = 10
print(f"You have {num_bananas} bananas")
# You have 10 bananas

'''
NoneType Variables
Not all variables have a value. We can declare an "empty" variable by setting it to None.

What is None?
None is a special value in Python that represents the absence of a value or a null value. It is not the same as zero, False, or an empty string.
'''
empty = None

'''
Math With Strings
Most of the math operators we went over earlier don't work with strings, aside from the * and addition operators. When working with strings the + operator performs a "concatenation".

"Concatenation" is a fancy word that means the joining of two strings. You should prefer string interpolation with f-strings over concatenation.


'''

first_name = "Lane "
last_name = "Wagner"
full_name = first_name + last_name
print(full_name)
# prints "Lane Wagner"

'''
Multi-Variable Declaration
We can save space when creating many new variables by declaring them on the same line:
'''
sword_name, sword_damage, sword_length = "Excalibur", 10, 200
'''
Copy icon
Which is the same as:
'''
sword_name = "Excalibur"
sword_damage = 10
sword_length = 200

'''
Copy icon
Any number of variables can be declared on the same line, and variables declared on the same line should be related to one another in some way so that the code remains easy to understand.

We call code that's easy to understand "clean code".
'''