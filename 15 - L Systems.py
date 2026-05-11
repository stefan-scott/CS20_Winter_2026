# L-Systems
# May 8, 2026
# Mr. Scott

# Turtle BoilerPlate
import turtle
t = turtle.Turtle()
wn = turtle.Screen()
wn.setup(800,800)
t.speed(0)


# Create L-System Functions
def apply_rules(ch):
    # Apply the rules to a single char
    # -- need to update for each Lsystem
    if ch == "L":
        return "+RF-LFL-FR+"
    elif ch == "R":
        return "-LF+RFR+FL-"
    else:
        return ch
    
def process_string(original_str): #"ABBAB"
    # loop through our original_str and apply
    # the rules to each character
    next_str = ""
    for c in original_str:
        next_str = next_str + apply_rules(c)
    return next_str

def create_L_system(num_steps, axiom):
    current_str = axiom
    for i in range(num_steps):
        next_str = process_string(current_str)
        current_str = next_str
    return current_str

def draw_L_system(instructions, angle, distance):
    # have the turtle make a drawing based on
    # the L-system instructions
    for cmd in instructions:
        if cmd == "F":
            t.fd(distance)
        elif cmd == "B":
            t.bk(distance)
        elif cmd == "+":
            t.right(angle)
        elif cmd == "-":
            t.left(angle)

# Main Code
commands = create_L_system(8, "L")
print(commands)

# Reposition Turtle [optional]
t.up()
t.goto(-250,250)
t.down()

# To Change L-Systems
# 0. cs20.ca  PYTHON STRINGS → #4 (turtle drawing...)
# 1. update  apply_rules()  with new ruleset
# 2. update "commands" line w/ growth steps and axiom3
# 3. update ANGLE in draw_L_system() function call
# 4. [optional] change turtle reposition


#Draw the L-System
turtle.tracer(False) #insta-draw
draw_L_system(commands, 90, 3)

turtle.exitonclick()
