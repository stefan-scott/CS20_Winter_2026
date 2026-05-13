# Custom Images
# Mr. Scott

import microbit, time, random
# LED Values: 0-off      9-full bright

# create an image of a die with a one
dice1 = "33333:30003:30903:30003:33333"
dice1 = microbit.Image(dice1)

dice3 = "33333:" \
        "30093:" \
        "30903:" \
        "39003:" \
        "33333"
dice3 = microbit.Image(dice3)

dice4 = "33333:" \
        "39093:" \
        "30003:" \
        "39093:" \
        "33333"
dice4 = microbit.Image(dice4)

dice6 = "33333:39093:39093:39093:33333"
dice6 = microbit.Image(dice6)

# ON-YOUR-OWN:   Add at least 2 more dice images (4, 6)

# Using the Dice, Let's Make a Game...
dice_images = [dice1, dice3, dice4, dice6]
dice_values = [  1  ,   3  ,   4  ,   6  ]
#                0      1      2      3
user_total = 0

while True:
    # A Button - Roll the Die
    if microbit.button_a.was_pressed():
        i = random.randrange(0,len(dice_values))
        microbit.display.show(dice_images[i])
        user_total += dice_values[i]
        print(user_total)
        
        # Goal - get 21 points w/o going over
        if user_total > 21:
            print("Game over, you lose")
            time.sleep(1)
            microbit.display.show(microbit.Image.SKULL)
            break
        elif user_total == 21:
            print("You win!")


