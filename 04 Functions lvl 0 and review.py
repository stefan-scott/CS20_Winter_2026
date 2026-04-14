# Fortune Teller Machine
# Mr. Scott
# April 13, 2026
#
# Revisit "level 0" function
#   - functions with no inputs, no outputs
#   - useful for reuse of code / organization

# 1. Any Import Statements
import random as r

# 2. Function Definitions
#    - def must be higher in file than fctn call

def fortune_one():
    # print out a single fortune for the user
    print("Today will be your lucky day!")
    
def fortune_two():
    #print another one
    print("Don't step on the cracks...")

# 3. Main Code
# 
# ask the user which fortune to print
# 1, 2, or random
print("1. Fortune 1") 
print("2. Fortune 2") 
print("3. Random Fortune")
choice = input("choice: ") #input yeild STR

if choice == "1":
    fortune_one()
elif choice == "2":
    fortune_two()
else:
    # random fortune
    flip = r.randrange(0,2) #either a 0 or 1
    if flip == 0:
        fortune_one() 
    else:
        fortune_two() 
    


