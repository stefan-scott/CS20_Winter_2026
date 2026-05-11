# L - Systems Demo
# Mr. Scott
# May 8, 2026

# Set Up Turtle Boilerplate - TODO
import turtle
t = turtle.Turtle()
wn = turtle.Screen()
wn.setup(800,800)
t.speed(0)

def draw_L_system(instructions, angle, distance):
    # have the turtle make a draw based
    # on the Lsystem instructions
    for cmd in instructions:
        if cmd == "F":
            t.fd(distance)
        elif cmd == "B":
            t.bk(distance)
        elif cmd == "+":
            t.right(angle)
        elif cmd == "-":
            t.left(angle)

# Create the L-System
def apply_rules(ch):
    # inspect ch(character) and apply the rules
    # to it (if any).
    if ch == "X":
        return "YF+XF+Y"
    elif ch == "B":
        return "AB"
    else:
        return ch

def process_string(original_str): #ABBAB 
    # Loop through original_str and apply rules
    # to each character individually
    next_str = ""
    for c in original_str:
        next_str = next_str + apply_rules(c)
    return next_str

def create_L_system(num_steps, axiom):
    #Run L-System for a set number of growth steps
    curr_str = axiom
    for i in range(num_steps):
        next_str = process_string(curr_str)
        curr_str = next_str
    return curr_str

# Main Code Section
commands = create_L_system(24, "A")
print(commands)
