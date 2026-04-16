# Lists, Strings, For Loops
# Mr. Scott
# April 16, 2026
# Prep for our first Python Quiz

############ LISTS #############
pet_names = ["Frank", "Larry", "Margie", "Jack", "R2D2"]
#               0        1        2         3       4
#              -5       -4       -3        -2      -1

# access list items
# pet_names[3] → accesses item at 3 ("Jack")
# pet_names[-1] → negative index counts from right to left
# len(pet_names) → returns # of items 
 
########## FOR LOOPS ########### 
# repeat ONCE per item in a collection (list/string)
# current item is stored in a LOOP VARIABLE

#for   loopvar  in  collection
# for current_pet in pet_names:  #repeat 5
#     print(f"I love my pet {current_pet}")

# if you just want to repeat N times
# use  range(n) → auto generates list with n items
#                 0,1,2,3,...,n

# for i in range(6):  #[0,1,2,3,4,5]
#     print(f"hi {i}")

#             inc,exl
# for i in range(5,10): #[5,6,7,8,9]
#     print(i)

for i in range(0, 100, 5): #start, end, skip
    print(i)



