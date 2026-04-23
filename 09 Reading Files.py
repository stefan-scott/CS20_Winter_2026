# Reading Data from Files
# Mr. Scott, Nov 19

# Make sure the file to read is in the
# SAME FOLDER as your python file.

# STEP ONE: open the file
my_file = open("poem.txt", "r")#r → READING

# STEP TWO: read the contents
# Option One: read whole file into a string
# full_text = my_file.read()
          # usually, at this point we would
          # split up the string somehow...

# Option Two: Read each line, store in list
list_of_lines = my_file.readlines()

# STEP THREE: Strip away newline character
#             for each line.
for index in range(len(list_of_lines)):  #[0,1,2] len 3
    list_of_lines[index] = list_of_lines[index].rstrip("\n")

import random
print(f"""A poem:
{random.choice(list_of_lines)}
{list_of_lines[1]}
{list_of_lines[2]}""")

my_file.close() #LAST STEP