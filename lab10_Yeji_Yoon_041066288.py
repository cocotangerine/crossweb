from gtts import gTTS
import os

d = {'a':'alfa', 'b':'bravo', 'c':'charlie', 'd':'delta', 'e':'echo', 'f':'foxtrot',
     'g':'golf', 'h':'hotel', 'i':'india', 'j':'juliett', 'k':'kilo', 'l':'lima',
     'm':'mike', 'n':'november', 'o':'oscar', 'p':'papa', 'q':'quebec', 'r':'romeo',
     's':'sierra', 't':'tango', 'u':'uniform', 'v':'victor', 'w':'whiskey',
     'x':'x-ray', 'y':'yankee', 'z':'zulu'}


# read a name inside a txt file
f = open("myname.txt", 'r')
lines = f.read()
f.close()


# create a function that receives a string as an argument and the dictionary
def stringToICAO(string, dictionary):
     convert_char = []
     for character in string:
          if character == " ":
               continue
          convert_char.append(dictionary[character.lower()])
     return ''.join(convert_char)


arg_gtts = stringToICAO(lines, d)
print(arg_gtts)


myobj = gTTS(
    text=arg_gtts,
    lang="en",
    slow=False)

myobj.save("my_name.mp3")


# stringToICAO(read_file(), d)