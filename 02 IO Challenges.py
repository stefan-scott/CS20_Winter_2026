# Comment Header Requirement
# Title
# Name
# Date
# One-Line Description


# Problem Two: CAD-YEN converter
# Get the user's name:
name = input("Enter a name: ")

amount_cad = input("amount CAD: ")
amount_cad = float(amount_cad)

amount_yen = amount_cad * 110

#Report the data back to the user
print("If you were to convert " + str(amount_cad))
print("CAD, you would get this much in yen: " + str(amount_yen))





# Problem One: Alarm Clock
# Time is 2pm. We set an alarm for 51h
# Print out what time the alarm rings

# Start by writing out your "algorithm"
# - use 24h clock, then convert back to 12h
# - add 51h, and as long as new time is >24
#   keep subtracting 24

'''
cur_time = 14 #set cur_time to 14 (2pm)
cur_time = cur_time + 51

while cur_time > 23:
    cur_time = cur_time - 24

# Convert back to 12h clock
if cur_time < 12: #AM
    print(str(cur_time)+"AM")
elif cur_time == 12:
    print("12PM")
else:
    cur_time = str(cur_time-12)
    print(cur_time + "PM")
'''