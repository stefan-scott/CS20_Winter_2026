# Images Demo - Day 1
# Mr. Scott
# June 4, 2026
# Initial Usage of the image library

import image #DON'T save your file as image.py

width = 400
height = 300

window = image.ImageWin(width,height) #creates a window
img = image.EmptyImage(width,height)

#manipulate the image
a_pixel = image.Pixel(124, 212, 217)
b_pixel = image.Pixel(0,0,0)

for x in range(width):
    for y in range(height):
        if x%2==0:
            img.set_pixel(x,y,a_pixel)
        else:
            img.set_pixel(x,y,b_pixel)


#draw the image on the window
img.draw(window)