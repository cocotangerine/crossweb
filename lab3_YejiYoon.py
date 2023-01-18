import pylightxl as xl

with open('city.xlsx', 'rb') as f:
    db = xl.readxl(f)
#jhfjhgjhkg
l = list(db.ws(ws='Sheet1').col(col=3))

#ask the user for the code of the country and save it into a variable
country = input("Enter your country: ")

#Scan the list l line by line and add 1 to the counter if the country is the one looked for
counter = 0
for cont in l:
    if country == cont:
        counter += 1

#Format and print the result
print("{} is the counter for the country".format(counter))

#Ask the user for the population looked for. Use a loop and a try except to validate the input as a valid integer
done = False

while done == False:
    try:
        population = int(input('Enter your population: '))
        if population > 0:
            done = True
    except:
        print("Invaild number")

#Store the population values into a list called l1 (see line 6)
l1 = list(db.ws(ws='Sheet1').col(col=5))

#Initialize a list lstOfRecords to an empty list
lstOfRecords = []

#Scan the list l1, if the population is larger than the population looked for, add the list index to lstOfRecords
for pop in l1:
    if population < pop:
        lstOfRecords.append(l1.index(pop))

#Print the list lstOfRecords
print(lstOfRecords)

#Bonus: Print the name of the cities whose index is in lstOfRecords
l2 = list(db.ws(ws='Sheet1').col(col=2))
for index in lstOfRecords:
    print(l2[index])
