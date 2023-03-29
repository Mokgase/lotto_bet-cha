import random

def login():
    global userName
    global userSurname
    userName = input("Enter your name:")
    userSurname = input("Enter you surname:")
    initialize()

def initialize():
    global userInput
    userInput = input("Press B to begin: ")
    if userInput == "b" or "B":
        looper()
    else:
        initialize()

def looper():
    theList =[]
    while True:
        for i in range(6):
            theList.append(random.randint(1-59))
            file=open("lottoList.txt", "a" + "\n")
            file.write("theList")
            file.close()
        print ("here are the lucky lotto picks")
        print(theList)
        continuePrompt()
    

def continuePrompt(userName,userSurname):
    listOfAnswers1=["Y","YES","Yes" ]
    listOfAnswers2=["N","NO","No","no","n"]
    userInput =input("Do you still want more lotto numbers?")
    if userInput == listOfAnswers1:
        looper()
    elif userInput == listOfAnswers2:
        print("Alright then "+ userName + "" + userSurname + ".")
        exit()
        


login()
