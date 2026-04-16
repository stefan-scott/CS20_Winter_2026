import FreeSimpleGUI as sg

# Get a string from user... like input()
#                            prompt             title
name = sg.popup_get_text("Enter your name: ","Question")
greeting = f"Hello there, {name}"
print(greeting)

# Display text in a window
sg.popup(greeting)
