from sense_hat import SenseHat
import time

s = SenseHat()
s.low_light = True

green = (0, 255, 0)
yellow = (255, 255, 0)
blue = (0, 0, 255)
red = (255, 0, 0)
white = (255, 255, 255)
nothing = (0, 0, 0)
pink = (255, 105, 180)
darkblue = (11, 11, 69)
lightgreen = (144, 238, 144)

# Write a python function displayColorForTemperature ,
# The function receives a float value as an argument representing a temperature in Celsius.
# Depending on the temperature range,
# the following colors will be displayed on the Sense HAT
while True:
    try:
        userInput = float(input("Enter the decimal number: "))
    except:
        print("You should not input string")
    else:
        if userInput < -40:
            print("You should input above -40")
        else:
            break


def displayColorForTemperature(temperature_input, o=(0, 0, 0)):
#
    screen_leds = [
        o, o, o, o, o, o, o, o,
        o, o, o, o, o, o, o, o,
        o, o, o, o, o, o, o, o,
        o, o, o, o, o, o, o, o,
        o, o, o, o, o, o, o, o,
        o, o, o, o, o, o, o, o,
        o, o, o, o, o, o, o, o,
        o, o, o, o, o, o, o, o,
    ]
    counter = 0
    while counter < len(screen_leds):
        if -40 <= temperature_input <= -10:
            screen_leds[counter] = darkblue
            counter += 1
        elif -9 <= temperature_input <= 0:
            screen_leds[counter] = blue
            counter += 1
        elif 1 <= temperature_input <= 15:
            screen_leds[counter] = lightgreen
            counter += 1
        elif 16 <= temperature_input <= 22:
            screen_leds[counter] = green
            counter += 1
        else:
            screen_leds[counter] = red
            counter += 1
    return screen_leds


s.set_pixels(displayColorForTemperature(userInput))


# 4
# Write a python function LedsOnForHumidity ,
# The function receives an integer value as an argument
# representing the humidity as a percentage Depending on the humidity range,
# the Sense HAT displays the relative number of blue lines (100% will be all leds sets to blue)
while True:
    try:
        humidity_value = int(input("Enter the humidity"))
    except:
        print("You should not input string")
    else:
        if humidity_value < 0:
            print("You should input a whole number")
        else:
            break


def LedsOnForHumidity(humidity, color=blue, o=(0, 0, 0)):
    relative_humidity = 64 * humidity / 100
    screen_leds = [
        o, o, o, o, o, o, o, o,
        o, o, o, o, o, o, o, o,
        o, o, o, o, o, o, o, o,
        o, o, o, o, o, o, o, o,
        o, o, o, o, o, o, o, o,
        o, o, o, o, o, o, o, o,
        o, o, o, o, o, o, o, o,
        o, o, o, o, o, o, o, o,
    ]
    counter = 0
    while counter < relative_humidity:
        screen_leds[counter] = color
        counter += 1
    return screen_leds


s.set_pixels(LedsOnForHumidity(humidity_value))
