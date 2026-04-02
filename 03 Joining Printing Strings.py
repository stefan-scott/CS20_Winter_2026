# Printing Multiple Values
# Mr. Scott
# April 2, 2026
# A look ways to output more than
# one value in print()

# can convert data forms
# str()  int()  float()  bool()

# 1. Create some variables
name = "Timothy" # string
age = 22         # integer
height = 170.5   # float
awake = True     # boolean

# Three ways to print multiple
# values/data types
#
# 1. Join strings using + (concatenation)
#   - must ensure all values are strings
#   - python adds no spaces/newlines
   #  STR     STR   INT     STR
print(name + "is" + str(age) + "yrs old")

# 2. if using print(), can separate things
#    to print with commas.
#    - print() adds a space b/w each thing
#    - not a good choice if we don't want space
print(name, "is", age, "yrs old")

# 3. Formatted String
#    - combine literal string with
#      variable/code substitutions
#    - special symbol before "" f
result = f"Hello there, {name}."
# result +=   same as result = result +
result += f" You are {age} years old."
print(result)




