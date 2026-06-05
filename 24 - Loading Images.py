# Loading Images
# Mr. Scott
# June 5, 2026
# Loading Image files and basic edits...

import image #library:  cs20-image

img = image.Image("sneakers.jpg") #load an image

width = img.get_width()
height = img.get_height() #extract image dimensions

window = image.ImageWin(width,height)

def darken(p):
    # p → pixel object (image lib)
    # reduce each channel of p by 50 (but not below 0)
    # return updated pixel
    r = max(p.get_red() - 50, 0)
    g = max(p.get_green() - 50, 0)
    b = max(p.get_blue() - 50, 0)
    
    new_p = image.Pixel(r,g,b)
    return new_p

def negative_pixel(p):
    #input:  p → Pixel object
    #output: Pixel Object (inverted/negative)
    r = 255 - p.get_red()
    g = 255 - p.get_green()
    b = 255 - p.get_blue()
    
    new_p = image.Pixel(r,g,b)
    return new_p
    
def average(p):
    # compute the average intensity of a Pixel
    # and return as an int
    total = p.get_red() + p.get_green() + p.get_blue()
    avg = int(total / 3)
    return avg

def desaturate(p):
    # make a pixel into a greyscale representation
    # input: p → Pixel object
    # output: Pixel object
    avg = average(p)
    grey_pixel = image.Pixel(avg, avg, avg)
    return grey_pixel

# Inspect each pixel and apply a fil
for x in range(width):
    for y in range(height):
        cur_pixel = img.get_pixel(x,y)
        new_pixel = desaturate(cur_pixel)
        img.set_pixel(x, y, new_pixel)

    img.draw(window)

for y in range(height):
    for x in range(width):
        cur_pixel = img.get_pixel(x,y)
        new_pixel = negative_pixel(cur_pixel)
        img.set_pixel(x, y, new_pixel)

    img.draw(window)

