# Image Practice
# Mr. Scott
# June 8, 2026
# Simple Image Algorithms (same for every pixel)

# Image boilerplate
import image, random
img = image.Image("rooster.jpg")
width = img.get_width()
height = img.get_height()
wn = image.ImageWin(width,height)

# Pixel Functions
def black_white(p, threshold):
    # turn a pixel into black or white
    # input: p → pixel object (src)
    # input: threshold → int (0-765)
    total = p.get_red() + p.get_green() + p.get_blue()
    if total > threshold:
        return image.Pixel(255,255,255)
    else:
        return image.Pixel(0,0,0)   
# Main Program
for x in range(width):
    for y in range(height):
        src_pixel = img.get_pixel(x,y)
        new_pixel = black_white(src_pixel, 400)
        img.set_pixel(x,y,new_pixel)
    img.draw(wn)

wn.exitonclick() #optional
