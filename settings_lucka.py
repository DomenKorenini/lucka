# Set the start state of the smart light, possible values are "on" and "off".
start_level = "on"

# How many sensor value are used in each calculation.
repeats = 10

# Prints sensor values, possible values are "yes" and "no".
print_values = "yes"


"""
Sensitivity can be any number from 1 to 10. With high sensitivity light will blink a lot.
"""
sensitivity = 1

"""
Dividing line between light and dark.
"""
light_limit = 3000


"""
Wait time in seconds after each reading from the light-sensor.
Default is 0
"""
pause_time = 0

