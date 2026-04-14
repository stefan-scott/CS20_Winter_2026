# Try - Except Demo
# Mr. Scott
# April 14, 2026
# Try to stop our programs from crashing...

my_list = [88, 44, "Twenty Two"]
#           0   1       2         X

while True:
    try:
        index = int(input("an Index: ")) #ValueError
        chosen_num = my_list[index]      #IndexError
        print("Num: " + chosen_num)      #TypeError
        # if we reach this line, there
        # were no exceptions. So no
        # need to repeat
        break
    
    except: #catch-all generic case
        print("Something went wrong!:( ")
#     except TypeError:
#         print("Type Error! Please choose a string")
#     except IndexError:
#         print("Index Error! Please enter 0, 1, or 2")
#     except ValueError:
#         #jumps here if a ValueError occurs
#         #in the try section.
#         print("Value Error! Enter a number.")
    
    