# Images and Conditional
# Mr. Scott
# June 9, 2026
# - change pixels of a certain color
# - change pixels in a particular location
# - combining pixels from multiple images

# image boilerplate
import image

img = image.Image("rooster.jpg")
smile = image.Image("smile.png")

width = img.get_width()
height = img.get_height()
wn = image.ImageWin(width,height)

# functions
def change_sky(p):
    # determine is pixel p is part of the sky
    # if so, change to a new color (blue)
    # input p (Pixel), output Pixel Object
    total = p.get_red() + p.get_green() + p.get_blue()
    if total < 40: #sky pixel
        return image.Pixel(95, 146, 227)
    else:
        return p


def left_half_grey(p, x):
    # change left half of image to greyscale (blue channel)
    # input: p → Pixel object   x: horizontal location
    # output: Pixel object
    if x < width/2:
        b = p.get_blue()
        return image.Pixel(b,b,b)
    else:
        return p
    
# main program
# Challenge 3 - joining two images
s_width = smile.get_width()
s_height = smile.get_height()
for x in range(s_width):
    for y in range(s_height):
        src_pixel = smile.get_pixel(x,y)
        total = src_pixel.get_red()+src_pixel.get_green()+src_pixel.get_blue()
        
        if total < 750:
            dest_x = x + 150
            dest_y = y + 50
            img.set_pixel(dest_x,dest_y,src_pixel)
        
    img.draw(wn)



# Challenge 2: change left half only
# for y in range(height):
#     for x in range(width):
#         src_pixel = img.get_pixel(x,y)
#         new_pixel = left_half_grey(src_pixel, x)
#         img.set_pixel(x,y,new_pixel)
#     img.draw(wn)
            



# Program 1: Remove Sky
# for x in range(width):
#     for y in range(height):
#         src_pixel = img.get_pixel(x,y)
#         new_pixel = change_sky(src_pixel)
#         img.set_pixel(x,y,new_pixel)
#     img.draw(wn)

# p = img.get_pixel(40,40)
# print(p.get_red(),p.get_green(),p.get_blue())


wn.exitonclick() 