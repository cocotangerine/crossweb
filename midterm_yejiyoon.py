#
# def checkWeights (weightAssign, weightMidTerm, weigthFinal):
#     sum_of_calc = float(weightAssign + weightMidTerm + weigthFinal)
#     if sum_of_calc == 1:
#         print(True)
#
#     else:
#        print(False)

def checkWeights (weightAssign = 0.4, weightMidTerm = 0.35, weigthFinal = 0.25):
    sum_of_calc = weightAssign + weightMidTerm + weigthFinal
    if sum_of_calc == 1:
        return True
    else:
        return False



# while True:
#     try:
#         user_input_assignment = float(input("Enter your the weight of assignments"))
#         user_input_mid = float(input("Enter your the weight of mid term"))
#         user_input_final = float(input("Enter your the weight of final"))
#     except:
#         print("You should input float")
#     else:
#         if user_input_assignment < 0 and user_input_assignment > 1 and user_input_mid < 0 and user_input_mid > 1 and user_input_final < 0 and user_input_final > 1 :
#             print("You should input a number between 0 and 1")
#         else:
#             break

while True:
    try:
        user_input_assignment = float(input("Enter your the weight of assignments"))
        user_input_mid = float(input("Enter your the weight of mid term"))
        user_input_final = float(input("Enter your the weight of final"))
    except:
        print("You should input float")
    else:
        if user_input_assignment < 0 or user_input_assignment > 1 or user_input_mid < 0 or user_input_mid > 1 or user_input_final < 0 or user_input_final > 1:
            print("You should input a number between 0 and 1")
        else:
            break


print(checkWeights(user_input_assignment, user_input_mid, user_input_final))
# test_checkWeights = checkWeights(user_input_assignment, user_input_mid, user_input_final)


# def getWeightOfAssignments():
#     user_input = float(input("Enter your weight of assignments"))
#     try:
#         if user_input > 0 and user_input < 1:
#             return user_input
#         else:
#             print("You should input a number between 0 and 1")
#     except:
#         print("You should input a number")

def getWeightOfAssignments():
    try:
        user_input = float(input("Enter your weight of assignments"))
        if user_input > 0 and user_input < 1:
            return user_input
        else:
            print("You should input a number between 0 and 1")
    except:
        print("You should input a number")

def calculateAlphaGrade(user_input):
        if user_input >= 97.5:
            return "A+"
        elif user_input >= 92.5:
            return("A")
        elif user_input >= 90:
            return("A-")
        elif user_input >= 87.5:
            return("B")
        elif user_input >= 82.5:
            return("B")
        elif user_input >= 80:
            return("B-")
        elif user_input >= 77.5:
            return("C+")
        elif user_input >= 72.5:
            return("C")
        elif user_input >= 70:
            return("C-")
        elif user_input >= 67.5:
            return("D+")
        elif user_input >= 62.5:
            return("D")
        elif user_input >= 60:
            return("D-")
        else:
            return("E")


while True:
    try:
        user_input = float(input("Enter your numeric grade"))
    except:
        print("You should input float")
    else:
        if user_input < 0 and user_input > 100:
            print("You should input a number between 0 and 1")
        else:
            break


print(calculateAlphaGrade(user_input))
# test_calculateAlphaGrade = calculateAlphaGrade(user_input)

# while True:
#     try:
#         user_choice = input("1. Test checkWeights 2. Test calculateNumericGrade 0. Exit")
#         if user_choice >= 0 and user_choice < 3:
#             if user_choice == 0:
#                 break
#             elif user_choice == 1:
#                 test_checkWeights
#             else:
#                 test_calculateAlphaGrade
#     except:
#         print("You should input a number between 0 and 2")

while True:
    try:
        user_choice = int(input("1. Test checkWeights 2. Test calculateNumericGrade 0. Exit"))
        if user_choice >= 0 and user_choice < 3:
            if user_choice == 0:
                break
            elif user_choice == 1:
                checkWeights(user_input_assignment, user_input_mid, user_input_final)
            else:
                calculateAlphaGrade(user_input)
    except:
        print("You should input a number between 0 and 2")
