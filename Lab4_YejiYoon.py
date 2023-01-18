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
o = (0,0,0)
c2 = (255, 255, 255)
c1 = (220, 220, 220)

def trinket_logo(G=green, Y=yellow, B=blue, O=nothing):
    G = green
    Y = yellow
    B = blue
    O = nothing
    logo = [
        O, O, O, O, O, O, O, O,
        O, Y, Y, Y, B, G, O, O,
        Y, Y, Y, Y, Y, B, G, O,
        Y, Y, Y, Y, Y, B, G, O,
        Y, Y, Y, Y, Y, B, G, O,
        Y, Y, Y, Y, Y, B, G, O,
        O, Y, Y, Y, B, G, O, O,
        O, O, O, O, O, O, O, O,
    ]
    return logo


def raspi_logo(G=green, R=red, O=nothing):
    G = green
    R = red
    O = nothing
    logo = [
        O, G, G, O, O, G, G, O,
        O, O, G, G, G, G, O, O,
        O, O, R, R, R, R, O, O,
        O, R, R, R, R, R, R, O,
        R, R, R, R, R, R, R, R,
        R, R, R, R, R, R, R, R,
        O, R, R, R, R, R, R, O,
        O, O, R, R, R, R, O, O,
    ]
    return logo



def plus(W=white, O=nothing):
    W = white
    O = nothing
    logo = [
        O, O, O, O, O, O, O, O,
        O, O, O, W, W, O, O, O,
        O, O, O, W, W, O, O, O,
        O, W, W, W, W, W, W, O,
        O, W, W, W, W, W, W, O,
        O, O, O, W, W, O, O, O,
        O, O, O, W, W, O, O, O,
        O, O, O, O, O, O, O, O,
    ]
    return logo


def equals(W=white, O=nothing):
    W = white
    O = nothing
    logo = [
        O, O, O, O, O, O, O, O,
        O, W, W, W, W, W, W, O,
        O, W, W, W, W, W, W, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, W, W, W, W, W, W, O,
        O, W, W, W, W, W, W, O,
        O, O, O, O, O, O, O, O,
    ]
    return logo


def heart(P=pink, O=nothing):
    P = pink
    O = nothing
    logo = [
        O, O, O, O, O, O, O, O,
        O, P, P, O, P, P, O, O,
        P, P, P, P, P, P, P, O,
        P, P, P, P, P, P, P, O,
        O, P, P, P, P, P, O, O,
        O, O, P, P, P, O, O, O,
        O, O, O, P, O, O, O, O,
        O, O, O, O, O, O, O, O,
    ]
    return logo


def elephant(C1=c1, C2=c2, O=o):
    logo = [
        o, o, c1, c1, o, o, o, o,
        o, c1, c1, c1, c1, c1, c1, o,
        c1, o, c1, c1, c1, c1, c1, c1,
        c1, c1, c1, c1, c1, c1, c1, c1,
        c1, c2, c2, c1, c1, c1, c1, c1,
        c1, o, c1, c1, c1, c1, c1, c1,
        c1, o, c1, c1, o, c1, c1, o,
        c1, o, c2, c1, o, c2, c1, o,
    ]
    return logo

pictures = [0, trinket_logo(), plus(), equals(), raspi_logo(), heart(), elephant()]

def getUserChoice():
    while True:
        try:
            user_choice = int(input("What do you want to display (0. to exit) 1. Logo 2. Plus sign 3. Equals sign 4. Raspberry 5. Heart 6. Elephant 0. Exit"))
        except:
            print("You should input a number")
        else:
            return user_choice


while True:
    compare = getUserChoice()
    if compare == 0:
        print("---Good bye---")
        break
    elif compare > 6:
        print("Please enter 0 to 6")
    else:
        s.set_pixels(pictures[compare])

        pictures = [0, trinket_logo(), plus(), equals(), raspi_logo(), heart(), elephant()]


def getUserChoice():
    while True:
        try:
            user_choice = int(input(
                "What do you want to display (0. to exit) 1. Logo 2. Plus sign 3. Equals sign 4. Raspberry 5. Heart 6. Elephant 0. Exit"))
            if (user_choice == 0):
                print("---Good bye---")
                break
            elif (user_choice > 6):
                print("Please enter the number(0 to 6)")
                continue
                #7 눌렀을 때 except까지 뜬다. 인덱스에러 때문에.. -> elif에서 반복문을 다시 실행시키고 싶다면
            s.set_pixels(pictures[user_choice])
        except:
            print("You should not input string")
        # else:
        #     s.set_pixels(pictures[user_choice])


getUserChoice()

#
def getUserChoice():
    while True:
        try:
            user_choice = int(input("""What do you want to display (0. to exit):

            1. Logo
            2. Plus sign
            3. Equals sign
            4. Raspberry
            5. Heart
            6. Elephant
            0. Exit
            """))
        except:
            print("Enter a valid number")
        else:
            return user_choice


images = [
    trinket_logo(green, yellow, blue, nothing),
    plus(white, nothing),
    equals(white, nothing),
    raspi_logo(green, red, nothing),
    heart(pink, nothing),
    elephant(blue, white, nothing)
]

while True:
    selection = getUserChoice()
    if selection == 0:
        print("closing program.")
        break
    s.set_pixels(images[selection - 1])

