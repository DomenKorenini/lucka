#!/usr/bin/env python3

""" Lucka is a smart lamp designed to turn itself on or off whenever
    it is dark or bright - in a smart way.
    Copyright (C) 2020  Domen Korenini

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>."""


import sys
import time
import RPi.GPIO as GPIO
from Light_Sensor.light_sensor import rc_time, pin_to_circuit, max_count
import settings_lucka as sl


__author__ = "Domen Korenini"
__credits__ = ["", ]
__license__ = "GPLv3"
__version__ = "0.1"
__maintainer__ = "Domen Korenini"
__email__ = "domen.2045@gmail.com"
__status__ = "Development"



pin_to_relay = 11

GPIO.setmode(GPIO.BOARD)
# Output on the pin for
GPIO.setup(pin_to_relay, GPIO.OUT)


# Check settings
if not type(sl.start_level) == type("abc"):
    print("Error in settings; start_level must be 'on' or 'off'.")
    GPIO.cleanup()
    sys.exit(0)

if not ((sl.start_level.lower() == "on") or (sl.start_level.lower() == "off")):
    print("Error in settings; start_level must be 'on' or 'off'.")
    GPIO.cleanup()
    sys.exit(0)

if not ((type(sl.sensitivity) == type(123)) or (type(sl.sensitivity) == type(1.23))):
    print("Error in settings; sensitivity must be int or float.")
    GPIO.cleanup()
    sys.exit(0)

if not (sl.sensitivity >= 1 and sl.sensitivity <= 10):
    print("Error in settings; sensitivity must be a number from 1 to 10.")
    GPIO.cleanup()
    sys.exit(0)

if not type(sl.light_limit) == type(123):
    print("Error in settings; light_limit must be an integer.")
    GPIO.cleanup()
    sys.exit(0)

if not sl.light_limit > 0:
    print("Error in settings; light_limit must be greater than 0.")
    GPIO.cleanup()
    sys.exit(0)

if not ((type(sl.pause_time) == type(123)) or (type(sl.pause_time) == type(1.23))):
    print("Error in settings; pause_time must be int or float.")
    GPIO.cleanup()
    sys.exit(0)

if not sl.pause_time >= 0:
    print("Error in settings; pause_time must be greater than 0.")
    GPIO.cleanup()
    sys.exit(0)


decision_limit = sl.repeats * (10 - sl.sensitivity) / 10


"""
About sensor values
High sensor value: sensor senses dark.
Low sensor value: sensor senses light.
"""


def run_sml():
    if sl.start_level.lower() == "on":
        main_list = [1, ] * sl.repeats
        currently = 1
        if sl.print_values == "yes":
            print("Start with the light switched ON.")
        GPIO.output(pin_to_relay, GPIO.HIGH)
    else:
        main_list = [0, ] * sl.repeats
        currently = 0
        if sl.print_values == "yes":
            print("Start with the light switched OFF.")
        GPIO.output(pin_to_relay, GPIO.LOW)

    try:
        while True:
            # Read data from sensor.
            sensor_value = rc_time(pin_to_circuit)
            if sl.print_values == "yes":
                print("Sensor value: %s \t" % sensor_value, end="")
            # Apply the logic (1 is dark)
            if sensor_value > sl.light_limit:
                main_list.insert(0, 1)
            else:
                main_list.insert(0, 0)
            # Remove the oldest sensor value.
            main_list.pop()

            # Evidence from the sensor; sensor says:
            dark_times = sum(main_list)
            bright_times = sl.repeats - dark_times

            # Make changes to currently if there is enough evidence for the opposite.
            if currently == 0 and dark_times > decision_limit:
                currently = 1
                if sl.print_values == "yes":
                    print("Switching the light ON.")
                GPIO.output(pin_to_relay, GPIO.HIGH)
            elif currently == 1 and bright_times > decision_limit:
                currently = 0
                if sl.print_values == "yes":
                    print("Switching the light OFF.")
                GPIO.output(pin_to_relay, GPIO.LOW)
            else:
                if sl.print_values == "yes":
                    print("Light state unchanged: ", end="")
                    if currently == 0:
                        print("OFF.")
                    elif currently == 1:
                        print("ON.")
                pass
            time.sleep(sl.pause_time)
    except KeyboardInterrupt:
        GPIO.cleanup()
        print("Exiting")
        print("")


run_sml()