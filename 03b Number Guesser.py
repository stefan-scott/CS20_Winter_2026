# Like our Scratch Project
# Random number 1-100
# user guesses, program tells "too high" / "too low"
# keep track of number of guesses

import random
# never save your file random.py

# print(random.randrange(1,10)) #int (1 to 9)
# print(random.uniform(1,10)) #float(1 to 9.9999)

# START PROGRAM HERE
secret = random.randrange(1,101)
print(secret)
guess = -1
num_tries = 0
while guess != secret:
    num_tries += 1   # num_tries = num_tries + 1
    guess = int(input("guess? "))
    if guess > secret:
        print("TOO HIGH!")
    elif guess < secret: #too low
        print("TOO LOW!")
# When loop ends, number has been guessed
print(f"Correct! That took you {num_tries} tries.")