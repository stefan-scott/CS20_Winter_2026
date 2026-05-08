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
    if ch == "A":
        return "B"
    elif ch == "B":
        return "AB"
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

# Main Code