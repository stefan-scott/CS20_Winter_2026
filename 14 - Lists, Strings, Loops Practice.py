# Loops, Lists, and Strings
# Mr. Scott
# May 5, 2026
# Practice for Python Quiz 2

# 2 Types of Collections
# lists      strings
foods = ["apple", "banana", "cantaloupe", "dragonfruit"]
#           0         1           2             3
#          -4        -3          -2            -1
city = "Saskatoon"
#       012345678
# also negative indices for strings

# 1. Recap Looping through Collection
# LOOP BY ITEM...don't have access to position
#   loopvar      collection
for  item    in  foods:
    print(item)
    
for letter   in  city:
    print(letter)
    
# 2. LOOP BY INDEX. (loop through all the positions)
for i in range(len(foods)): #[0,1,2,3]
    item = foods[i]
    if i < len(foods)/2:
        print(item.upper())
    else:
        print(item.lower())

# Slicing:  get sub-list or a sub-string
# name_of_collection[start:end]
#                   [inc: excl]

# 5 MINUTE CHALLENGE
new_list = [11, 33, 55, 77, 99, 121, 143]  #X
#            0   1  2    3   4   5    6     7
new_word = "Centennial Collegiate"
#           0123456789  

# print out the following via slicing
# 1. [77, 99, 121, 143]
print( new_list[3:7] ) #new_list[3:]
# 2. "l C"
print( new_word[9:12] )
# 3. "Collegiate"
print ( new_word[11:] )
print ( new_word[11:][5] )
#        "Collegiate"[5]
