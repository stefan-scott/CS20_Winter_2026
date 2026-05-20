# Micro:bopit Starter
# Mr. Scott
# May 19, 2026
# Initial Code for Microbit Game

import microbit, time, random

def is_shaking():
    # Boolean Function → returns True / False
    # based off of if the microbit is being
    # Shaken or not.
    min_z = microbit.accelerometer.get_z()
    max_z = min_z
    
    # use a loop to sample get_z() N times (10)
    for i in range(10):
        z = microbit.accelerometer.get_z()
        min_z = min(min_z, z)
        max_z = max(max_z, z)
    
    # determine the difference b/w max_z  min_z
    total_diff = abs(max_z - min_z)
    
    # 1200 is the "sensitivity"...can adjust
    if total_diff > 1200:
        return True
    else:
        return False

# ------ MAIN CODE BEGINS HERE -------
def show_target(t):
    # display on the LED grid either
    # an icon to represent char t
    # or char t itself
    if t == "S": #"Duck" means Shake.
        microbit.display.show(microbit.Image.DUCK)
    #elif for "L" and "R"
    else:
        microbit.display.show(t)
    
# SETUP
possible_actions = ["A","S"] #"B","L","R",

target = random.choice(possible_actions)
show_target(target)

microbit.button_a.was_pressed() #reset button counter
microbit.button_b.was_pressed() # ""

start_time = time.time()

# GAME LOOP BEGINS HERE
while True:
    #1. Check for Shake
    if is_shaking():
        if target == "S": #correct
            print("Shake - Correct!")
            time.sleep(1) # Buffer to stop shaking
            #increase score by 1
            microbit.display.clear()
            time.sleep(0.2)
            target = random.choice(possible_actions)
            show_target(target)
        else:   #incorrect!
             print("Shake - Incorrect!")
             break
    #2. Check for Button A
    #3. Check for Button B
    #4. Check for Tilt Left
    #5. Check for Tilt Right
    #6. Check for Out-of-Time