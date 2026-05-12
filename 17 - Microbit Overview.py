# Microbit Overview
# May 12, 2026
# Mr. Scott
# Display, Buttons, Accelerometer

# How to install library
# 1. Tools → Open System Shell
# 2. type:  pip install cs20-microbitio

import microbit, time, turtle, random

# ---- Display ----
# # Static Text
# for ch in "SASKATCHEWAN":
#     microbit.display.show(ch)
#     time.sleep(0.25) #delay in seconds
# 
# microbit.display.scroll("CENTENNIAL")

# ---- Buttons ----
# # .is_pressed()  → says if button is currently pressed
# # .was_pressed() → returns true ONCE per button press
# 
# count_a = 0
# count_b = 0
# 
# # BUG ALERT!
# print("3 second delay")
# time.sleep(3) #press B button during this time
# 
# microbit.button_a.was_pressed() #"resets" was_pressed
# microbit.button_b.was_pressed() #"resets" was_pressed
# 
# while True:
#     if microbit.button_a.is_pressed():
#         count_a += 1
#     if microbit.button_b.was_pressed():
#         count_b += 1
#     print(f"a: {count_a} \t b: {count_b}")

# ---- Accelerometer ----
# Measure orientation (by inertial forces)
# X-tilt
# FLAT          reading ~ 0
# Left 90 deg   reading ~ -1048
# Right 90 deg  reading ~ +1048
#
# -1048    |    0   |   1048
#        -300      300 
#  LEFT       FLAT      RIGHT

def x_tilt(threshold):
    # report the orientation of microbit(flat, left, right) 
    # threshold → positive number to determine how much
    #             tilt causes a non-flat reading
    x = microbit.accelerometer.get_x()
    if x < threshold *-1 :
        return "left"
    elif x > threshold:
        return "right"
    else:
        return "flat"

# SET UP BASIC TURTLE
t = turtle.Turtle()
wn = turtle.Screen()
t.speed(0)
movement = 5

while True:
    # Accel
    current = x_tilt(300)# flat, left, right
    print(current)
    if current == "left":
        t.left(10)
    elif current == "right":
        t.right(10)
    t.fd(movement)
    
    # Buttons
    
# 1. Use A/B buttons to
#    increase/decrease speed

# 2. Add background and turtle color

# 3. If A and B pressed:
#      toggle turtle pen on/off

    
    
    
    
