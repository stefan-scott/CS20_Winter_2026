# More about Functions (inputs/outputs)
# Mr. Scott
# April 15, 2026
#
# Arguments, Parameters, Return
#
# Variable Scope: WHERE in a program a variable is accessible
#    - variable is LOCAL to the CODE BLOCK (def, if, while, for)
#      it is defined within
#
#    - if you make a variable in a function, it only
#      exists in that function


# variables inside the brackets are PARAMETERS
# - these are LOCAL variables to the function
# - the variables recieve the input data
def add_three(num1, num2, num3):
    # adds three numbers together
    # num1,2,3 → INT numbers to add
    result = num1 + num2 + num3
    # result is LOCAL.
    # if I only need it short term: just use in the function
    # if I need later/elsewhere: return it from the function
    
    # trying to modify a global from in a function
    # instead creates a LOCAL with the same name.
    a = 10
    print("from function:",a)
    
    return result
    # return immediately exits the function, sends data out.

# WITH INDENTATION (not a code block) → Global Variable
# Can access anywhere, not modify from functions
a = 99

# With returned data, typically 2 OPTIONS:
# 1. Store in a variable
# 2. Print it directly
r = add_three(1,2,3)
print(r)
print(add_three(40,40,40))
print("global:",a)   