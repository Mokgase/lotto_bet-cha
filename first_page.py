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


    #  appender = "animeGenre.txt"
    #  file = open(appender, "a")
    #     title = input("Enter the anime you want to add to your list: ")
    #     file.write(title + "\n")
    #     file.close()

def looper():
    theList =[]
    while True:
        for i in range(6):
            theList.append(random.randint(1,59))
            finalStrList = ' '.join(map(str,theList))
            print(finalStrList)
            appender = "lottoList.txt"
            file=open(appender, "a")
            print ("here are the lucky lotto picks")
            file.write(finalStrList)
            file.close()
            continuePrompt(userName,userSurname)
    

def continuePrompt(userName,userSurname):
    listOfAnswers1=["Y","YES","Yes" ]
    listOfAnswers2=["N","NO","No","no","n"]
    userInput =input("Do you still want more lotto numbers?")
    if userInput == listOfAnswers1[0][1][2]:
        looper()
    elif userInput == listOfAnswers2[0][1][2][3][4]:
        print("Alright then "+ userName + "" + userSurname + ".")
        exit()
        


login()
