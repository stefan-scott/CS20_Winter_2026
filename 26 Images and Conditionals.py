# Images and Conditional
# Mr. Scott
# June 9, 2026
# - change pixels of a certain color
# - change pixels in a particular location
# - combining pixels from multiple images

# image boilerplate
import image

img = image.Image("moon.jpg")
width = img.get_width()
height = img.get_height()
wn = image.ImageWin(width,height)

# functions
def change_sky(p):
    # determine is pixel p is part of the sky
    # if so, change to a new color (blue)
    # input p (Pixel), output Pixel Object
    total = p.get_red() + p.get_green() + p.get_blue()
    if total == 0: #sky pixel
        return image.Pixel(95, 146, 227)
    else:
        return p
# main program



# p = img.get_pixel(40,40)
# print(p.get_red(),p.get_green(),p.get_blue())

img.draw(wn)
wn.exitonclick() 