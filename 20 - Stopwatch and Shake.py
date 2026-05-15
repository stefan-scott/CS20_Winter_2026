# Stopwatch and Shake
# Mr. Scott
# May 15, 2026

import microbit, time, random

# what time is it?
# epoch Jan 1, 1970 at midnight UTO-0
# returns # of seconds since then
images = [microbit.Image.SKULL,
          microbit.Image.HAPPY,
          microbit.Image.GIRAFFE,
          microbit.Image.DUCK,
          microbit.Image.HOUSE]
delay = 0.05 #x1.2  0.05 0.06 0.072 ..and so on 
max_delay = 0.75

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

print("Shake to Roll...")
while not is_shaking():
    time.sleep(0.05)
    
start_time = time.time()
img = random.choice(images)
microbit.display.show(img)

while True:
    elapsed_time = time.time() - start_time
    print(f"{elapsed_time:.2f}")
    
    # time-based event (delay amount reached)
    # reset timer, new rnd image, increase delay
    if elapsed_time > delay:
        start_time = time.time()
        
        img = random.choice(images)
        microbit.display.show(img)
        
        delay = delay * 1.2
        if delay > max_delay:
            break
        
    # button A to restart
    if microbit.button_a.was_pressed():
        start_time = time.time()
