# Microbit Radio
# May 15, 2026

import microbit
from microbit import radio

# Radio Setup Code
radio.on()
radio.config(channel=73)  # 0-83
radio.config(power=7)     # 0-7

# Radio Receive
while True:
    incoming = radio.receive() #str or "None"
    if incoming != "None":
        print(incoming)
        
# Radio Send
# radio.send(str)  "F10" forward speed 10
                #str[0]