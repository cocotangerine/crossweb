from sense_hat import SenseHat
import time
import random

s = SenseHat()
s.low_light = True

green = (0, 255, 0)
yellow = (255, 255, 0)
blue = (0, 0, 255)
red = (255, 0, 0)
white = (255, 255, 255)
nothing = (0, 0, 0)
pink = (255, 105, 180)

# Write a python function rollAdice.
# The function receives the number of faces of a dice and
# returns the value once the dice is rolled.
# Assume the number received by the function is a positive integer value.
# Your function makes use of the Random module.

def roll_a_dice(faces):
    """Take the number of faces and return a random number between 1 to the number of faces"""
    num = random.randint(1, faces)
    print("You got number {}".format(num))
    return num

# Prompt the user for the number of faces of the dice.
# Validates the number of faces as an integer (use try except and a while loop)
# On the Sense HAT, turn on as many leds as the number of faces.
# Use the color of your choice.

def show_dice_number(dice_number, color1=(0, 255, 0), color2=(0, 0, 0)):
    screen_leds = [
        color2, color2, color2, color2, color2, color2, color2, color2,
        color2, color2, color2, color2, color2, color2, color2, color2,
        color2, color2, color2, color2, color2, color2, color2, color2,
        color2, color2, color2, color2, color2, color2, color2, color2,
        color2, color2, color2, color2, color2, color2, color2, color2,
        color2, color2, color2, color2, color2, color2, color2, color2,
        color2, color2, color2, color2, color2, color2, color2, color2,
        color2, color2, color2, color2, color2, color2, color2, color2
    ]
    counter = 0
    while counter < dice_number:
        screen_leds[counter] = color1
        counter += 1
    return screen_leds


while True:
    try:
        userInput = int(input("Enter the number of faces of the dice: "))
    except:
        print("You should input a positive whole number")
    else:
        if userInput > 65:
            print("You should input less than 65")
        else:
            break

dice1 = roll_a_dice(userInput)
s.set_pixels(show_dice_number(dice1))
