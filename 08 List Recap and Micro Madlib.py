# List Modify + Madlib
# Mr. Scott
# April 20, 2026

# LIST MODIFY
# foods[2] = x  → replace item at pos 2 with x
# foods.append(x) → adds x to end of array
# foods.pop(i) → removes and returns item at pos i
#          0         1          2
foods = ["apple", "banana", "cantaloupe"]
foods[2] = "durien"
foods.append("cantaloupe")

import random
#random.choice(list) → pick one item at random
# MICRO MADLIB
nouns = []
verbs = []
def create_story():
    # create a simple madlib
    num = input("enter a number 1-10: ")
    cost = input("enter a cost: ")
    food = random.choice(foods)
    # generate story with substitutions
    story = f"""I am hungry for {food}. 
I wish I had {num}.
But I would need {cost} dollars!
"""
    print(story)

#MAIN CODE HERE
create_story()
 