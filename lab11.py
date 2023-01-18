from mysql.connector import MySQLConnection, Error

from mySqlDbConfig import readDbConfig

#
# if __name__ == '__main__':
# queryFetchone()

# Create a function insertGrade that receives 4 parameters, a lastName, a firstName, a province and a grade. The function then connects to the database lab11 and inserts the record.
def insertGrade(firstName, lastName, province, grade):
    try:
        dbconfig = readDbConfig()
        conn = MySQLConnection(**dbconfig)
        cursor = conn.cursor()
        cursor.execute(f"insert into grades values ('{firstName}', '{lastName}', '{province}', '{grade}')")
        row = cursor.fetchone()
    except Error as e:
        print(e)
    finally:
        conn.commit()
        cursor.close()
        conn.close()

# insertGrade('yeji','yoon','ON','A')

# Create a function deleteGrade that receives 4 parameters, a lastName, a firstName, a province and a grade. The function then connects to the database lab11 and deletes that record.
def deleteGrade(firstName, lastName, province, grade):
    try:
        dbconfig = readDbConfig()
        conn = MySQLConnection(**dbconfig)
        cursor = conn.cursor()
        cursor.execute(f"delete from grades where FName = '{firstName}' and LName = '{lastName}' and Province= '{province}' and Grade= '{grade}'")
        # cursor.execute(
            # f"DELETE FROM grades WHERE FName = '{firstName}' AND LName ='{lastName}' AND Province = '{province}' AND Grade = '{grade}'")
        row = cursor.fetchone()
    except Error as e:
        print(e)
    finally:
        conn.commit()
        cursor.close()
        conn.close()

# deleteGrade('yeji','yoon','ON','A')


# Create a function displayGrade that receives 3 parameters, a lastName, a firstName, a province.Make sure your query uses the sql LIKE function. The function then connects to the database lab11 and returns a list of grades.
def displayGrade(firstName, lastName, province):
    myList = []
    try:
        dbconfig = readDbConfig()
        conn = MySQLConnection(**dbconfig)
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM grades where FName like ('%{firstName}%') and LName like ('%{lastName}%') and Province like ('%{province}%')")
        row = cursor.fetchone()
        # print("<table border='1'>")
        while row is not None:
            # print("<tr><td>{}</td><td>{}</td><td>{}</td><td>{}</td></tr>".format(row[0],row[1],row[2],row[3]))
            myList.append(row)
            row = cursor.fetchone()
    except Error as e:
        print(e)
    finally:
        cursor.close()
        conn.close()
    return myList

# displayGrade('yeji','yoon','ON')


# The 3 functions should make use of the function readDbConfig from the sample program available on Brightspace and github, zip file week11.zip

# Write a python program that proposes the following options:
# - Enter a grade
# - Display a grade
# - Delete a grade
# - Exit

while True:
    try:
        user_input = int(input(
'''1. Enter a grade
2. Display a grade
3. Delete a grade
0. Exit'''))
    except:
        print('Please enter a whole number.')

    if user_input == 1:
        user_firstname = input('First name>> ')
        user_lastname = input('Last name>> ')
        user_province = input('Province>> ')
        user_grade = input('Grade>> ')
        insertGrade(user_firstname, user_lastname, user_province, user_grade)
    elif user_input == 2:
        user_firstname = input('First name>> ')
        user_lastname = input('Last name>> ')
        user_province = input('Province>> ')
        displayGrade_list = displayGrade(user_firstname, user_lastname, user_province)
        print(displayGrade_list)
        for grade in displayGrade_list:
            print("<tr><td>{}</td><td>{}</td><td>{}</td><td>{}</td></tr>".format(grade[0],grade[1],grade[2],grade[3]))

    elif user_input == 3:
        user_firstname = input('First name>> ')
        user_lastname = input('Last name>> ')
        user_province = input('Province>> ')
        user_grade = input('Grade>> ')
        deleteGrade(user_firstname, user_lastname, user_province, user_grade)
    elif user_input == 0:
        print('You have chosen exit. Bye')
        break








# For the display grade option, display the list of results as a html table, ie: generate the html code.