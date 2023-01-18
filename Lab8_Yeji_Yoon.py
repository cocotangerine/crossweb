
#Prompts the user for the number of Tests
#Note that this function will include call(s) to the input function
#Keep prompting until the number is an integer. Each grade is in between 0 and 100..
#Returns the number of Tests
def getNumberOfTests():
    while True:
        try:
            number_test_input = int(input("Enter the number of tests"))
            if number_test_input < 0 or number_test_input > 100:
                print("You should input between 0 and 100")
            else:
                return number_test_input
        except:
            print("You've got invalid number, put the whole number plz")


#Prompts the user for the weigth of Assignments
#Note that this function will include call(s) to the input function
#Keep prompting until the number is a float >= 0 and <= 1
#Returns the weight of assignments
def getWeightOfAssignments():
    while True:
        try:
            assignment_weight_input = float(input("Enter the weight of assignments"))
            if assignment_weight_input > 1 or assignment_weight_input < 0:
                print("You should input between 0 and 1")
            else:
                return assignment_weight_input
        except:
            print("You should input the decimal number")
    # return assignment_weight_input



#Prompts the user for the weigth of Midterms
#Note that this function will include call(s) to the input function
#Keep prompting until the number is a float >= 0 and <= 1
#Returns the weight of midterms
def getWeightOfMidTerms():
    while True:
        try:
            midterms_weight_input = float(input("Enter your weight of midterms (0-1)"))
            if midterms_weight_input < 0 or midterms_weight_input > 1:
                print("You should input between 0 and 1")
            else:
                return midterms_weight_input
        except:
            print("You should input the decimal number")




#Prompts the user for the weigth of the final
#Note that this function will include call(s) to the input function
#Keep prompting until the number is a float >= 0 and <= 1
#Returns the weight of final
def getWeightOfFinal():
    while True:
        try:
            final_weight_input = float(input("Enter your weight of the final "))
            if final_weight_input <= 0 or final_weight_input >= 1:
                print("You should input decimal numbers between 0 and 1")
            else:
                return final_weight_input
        except:
            print("You should input the decimal number")


#returns True if the sum of the 3 arguments is 1, False otherwise
#Assign the default values 0.4 0.35 0.25 to wAssign, wMidtern and wFinal respectively
def checkWeights(wAssign=0.4 ,wMidTerm=0.35, wFinal=0.25):
    if wAssign + wMidTerm + wFinal == 1:
        return True
    else:
        return False


#calculate the numeric grade as specified in the course outline
def calculateNumericGrade(AvgAssignments, AvgMid, Avgfinal, wOfAssign, wOfMidTerms, wFinal):
    total_grade = (AvgAssignments * wOfAssign) + (AvgMid * wOfMidTerms) + (Avgfinal * wFinal)
    return total_grade


#convert the numeric grade to a letter according to the conversion table in the course outline
def calculateLetterGrade(numericGrade):
    if numericGrade >= 90 and numericGrade <= 100:
        return "A+"
    elif numericGrade >= 85 and numericGrade <= 89:
        return "A"
    elif numericGrade >= 80 and numericGrade <= 84:
        return "A-"
    elif numericGrade >= 77 and numericGrade <= 79:
        return "B+"
    elif numericGrade >= 73 and numericGrade <= 76:
        return "B"
    elif numericGrade >= 70 and numericGrade <= 72:
        return "B-"
    elif numericGrade >= 67 and numericGrade <= 69:
        return "C+"
    elif numericGrade >= 63 and numericGrade <= 66:
        return "C"
    elif numericGrade >= 60 and numericGrade <= 62:
        return "C-"
    elif numericGrade >= 57 and numericGrade <= 59:
        return "D+"
    elif numericGrade >= 53 and numericGrade <= 56:
        return "D"
    elif numericGrade >= 50 and numericGrade <= 52:
        return "D-"
    else:
        return "F"


#Get the weight value of the assignments (call the appropriate function)
#Get the weight value of tests (call the appropriate function)
#Get the weight value of the final (call the appropriate function)
#Check the sum of weight values is 1 (call the appropriate function)
#Repeat the last four lines if not equal to 1
#    check_sum_weight = checkWeights(val_weight_ass, val_weight_midterm, val_weight_final)

sum_of_weight = 0

while sum_of_weight != 1:
    w_assignment = getWeightOfAssignments()
    w_midterm = getWeightOfMidTerms()
    w_final = getWeightOfFinal()
    if checkWeights(w_assignment, w_midterm, w_final):
        sum_of_weight = 1


#Get the average grade obtained on the assignments
#Validate the input as a float between 0 and 100
while True:
    try:
        avg_grade_ass = float(input("Your average grade obtained on the assignments: "))
        if avg_grade_ass < 0 or avg_grade_ass > 100:
            print("Please input between 0 and 100")

    except:
        print("You should input decimal numbers")
    else:
        break


#Get the number of tests (call the appropriate function)
#Prompt the user for each test grades and accumulate the value
#Validate the input as a float between 0 and 100
#Calculate the average test grade.

num_tests_value = getNumberOfTests()

test_num_list = []
while 0 < num_tests_value:
    try:
        grades_input = float(input("Your each test grade: "))
        test_num_list.append(grades_input)
        num_tests_value = num_tests_value - 1
    except:
        print("You have to input decimal numbers")
    else:
        if grades_input > 100 or grades_input < 0:
            print("You should input between 0 and 100")

"""calculated average"""
division_number = len(test_num_list)
total = 0
for grade in test_num_list:
    total += grade
avg_test_grade = total / division_number

"""
another way to solve
num_tests_value = getNumberOfTests()
counter = 0
accumulate = 0
while counter < num_tests_value:
    try:
        user_grade_input = float(input(f"Enter your test grade#{counter + 1}: "))
        if user_grade_input < 0 or user_grade_input > 100:
            print("Make sure that you have to input between 0 and 100")
        else:
            accumulate = accumulate + user_grade_input
            counter += 1
    except:
        print("You should input decimal numbers")
print(accumulate / num_tests_value)
"""

#Prompt and get the final grade
#Validate the input as a float between 0 and 100
while True:
    try:
        final_grade_input = float(input("Your final grade: "))
        if final_grade_input < 0 or final_grade_input > 100:
            print("You should input between 0 and 100")
    except:
        print("You've got invalid input")
    else:
        break


#Calculate and display the final numeric grade (call the appropriate function)
display_numeric = calculateNumericGrade(avg_grade_ass, avg_test_grade, final_grade_input, w_assignment, w_midterm, w_final)
print(f"{display_numeric}: This is your final numeric grade")

#Calculate and display the final alphabetical grade (call the appropriate function)
print(f"{calculateLetterGrade(display_numeric)}: This is your final alphabetical grade")
