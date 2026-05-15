# Microbit Image Functions
# Mr. Scott
# May 15, 2026

import microbit, time, random

# ----------------------------
#    Microbit Pixel Library
# ----------------------------
grid = [ [0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0] ]

def print_grid():
    #print out grid in an easy-to-read format
    for row in grid:
        print(row)

def show_grid():
    #convert 2D list into a string, and display
    result = ""
    for row in grid:
        for pixel in row:
            result += str(pixel)
        result += ":"
    result = result[0:-1]
    
#     print(result)
    microbit.display.show(microbit.Image(result))

def set_pixel(x, y, intensity):
    # set pixel at (x,y) to a brightness (0-9)
    grid[y][x] = intensity
    show_grid()

def plot(x,y):
    # turn pixel at (x,y) full on
    set_pixel(x,y,9)

def unplot(x,y):
    # turn off pixel at (x,y)
    set_pixel(x,y,0)

def queue_pixel(x, y, intensity):
    # update pixel at (x,y) but don't update display
    grid[y][x] = intensity
    
def set_all(intensity):
    #turn all pixels to a brightness (0-9)
    for x in range(5): #x: 0 1 2 3 4
        for y in range(5):  #y: 0 1 2 3 4
            queue_pixel(x,y,intensity)
    show_grid()

# ----------------------
#   Game Control Demo
# ----------------------

# Setup code

player_x = 2
player_y = 4

plot(player_x, player_y)


# Main Loop (Game Loop)
while True:
    #1. Plan to remove player LED
    queue_pixel(player_x, player_y, 0)
    
    #2. Check for user input, and update position
    if microbit.button_a.was_pressed():
        player_x = player_x - 1
        if player_x < 0:
            player_x = 0
    
    if microbit.button_b.was_pressed():
        player_x = min(player_x + 1, 4)
        
    #3. Redraw the player
    plot(player_x, player_y)

            