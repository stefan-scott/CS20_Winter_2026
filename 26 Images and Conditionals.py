# Images and Conditional
# Mr. Scott
# June 9, 2026
# - change pixels of a certain color
# - change pixels in a particular location
# - combining pixels from multiple images

# image boilerplate
import image

img = image.Image("sneakers.jpg")
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
    # 
# main program




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