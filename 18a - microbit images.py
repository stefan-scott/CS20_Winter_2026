# Microbit built-in images
# Mr. Scott
# May 13, 2026
# Displaying icons from microbit image library

import microbit, time, random

# Display a built-in image
# Show 3 pictures, 1 sec each...   time.sleep(99) #delay in seconds
icon = microbit.Image.SNAKE
microbit.display.show(icon)
time.sleep(1)

microbit.display.show(microbit.Image.CLOCK1)
time.sleep(1)

microbit.display.show(microbit.Image.TORTOISE)
time.sleep(1)


# --- Animating some images ---
clocks = microbit.Image.ALL_CLOCKS
ani_delay = 0.05

while True:
    for current in clocks:
        microbit.display.show(current)
        time.sleep(ani_delay)
    
        #Check for button presses
        if microbit.button_a.was_pressed():
            ani_delay = ani_delay - 0.02
            if ani_delay < 0: #code to prevent neg values
                ani_delay = 0
        if microbit.button_b.was_pressed():
            ani_delay = min(0.08, ani_delay + 0.02)
            
        