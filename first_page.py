import random
import numpy
def login():
    userName = input("Enter your name:")
    userSurname =("Enter you surname:")
    initialize()

def initialize():
    theList =[]
    userInput = input("Press Enter to begin")
    while True:
        if userInput == "":
            for i in range(6):
                theList.append(random.randint(1-59))
                finalList = numpy.array(theList)
                content=str(finalList)
                file.write(content + "\n")
                file.close()
            print ("here are the lucky lotto picks")
            print(theList)
        elif userInput != "":
            print("Press enter if you want to begin")
        else:
            exit()


