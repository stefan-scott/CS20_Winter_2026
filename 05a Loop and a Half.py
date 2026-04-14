# Loop and a Half
# Mr. Scott
# April 14, 2026
# "Forever" Loop, break, continue

# break → exit the loop it is most
#         immediately within.
# continue → stops the current iteration,
#            and begins the next one.
while True:
    choice = input("Stop the loop? [yes/no]")
    if choice.lower() == "yes":
        break
    elif choice.upper() == "MAYBE":
        print("restarting loop")
        continue
    print("Let's ask again...")
    #yes YES YeS 