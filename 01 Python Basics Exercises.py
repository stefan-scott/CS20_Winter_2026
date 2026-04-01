# Text Editor / Code Editor
print("First Python Program")
# Write code to calculate area of rectangle

# Ask user for width, store in a variable
# input() ALWAYS yields a string

width = input("enter a width:")
height = input("enter a height:")
# in order to multiply, we need to
# convert these string to a number (int/float)
width = float(width)
height = float(height)
# str(x)  → convert x to string
# int(x)  → convert x to int
# bool(x) → convert x to bool
# float(x)→ convert x to float

# calculate result and print as output
area = width * height

#        STR        + "200.0"
print("The area is " + str(area))

# To finish, let's check if this is a BIG number
# if the number is 0-99.9 (small number)
# elif the number is 100-999.9 (medium number)
# elif the number is >= 1000 (large numbers)
if area < 100:
    print("Small Number")
elif area < 1000:  #100-999.99
    print("Medium")
else:
    print("Large Number")