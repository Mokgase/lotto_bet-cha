import random
import string

def login():
    global userName
    global userSurname
    userName = input("Enter your name:")
    userSurname = input("Enter you surname:")
    

def initialize():
    global userInput
    while True :
        userInput = input("Press Enter to begin: ")
        if userInput == "":
            looper()
        else:
            initialize()


    #  appender = "animeGenre.txt"
    #  file = open(appender, "a")
    #     title = input("Enter the anime you want to add to your list: ")
    #     file.write(title + "\n")
    #     file.close()

def looper():
    theList = []
    finalList = []
    for i in range(6):
        if i < range(6):
            theList.append(random.randint(1,59))
        else:
            print("Done generating")
        break
    for x in theList:
        finalList.append(str(x))
        print("Here's your lucky lotto numbers "+finalList+" .")
        theFile = "lottoList.txt"
        file = open(theFile, "a")
        file.write(finalList + "\n")
        file.close()

    #  theList = []
    #  i = 1
    #  while i < 7:
    #       theList.append(random.randint(1,59))
    #       if i == 7:
    #         break
    #       else:
    #         i+=1
    #         for item in theList:
    #             finalList = print(str(item))
    #             file = open("lottoList.txt","a")
    #             file.write(finalList + "\n")
    #             file.close()
    #             print("Here are your lucky lotto picks:" + "\n" + finalList)
    #         continuePrompt()
                
        
    # theList =[]
    # while True:
    #     #generates 6 numbers and puts them in a list
    #     for i in range(6):
    #         theList.append(random.randint(1,59))
        
    #     #itterates through the list and converts it to a string and writes it into a file
    #     for x in theList:
    #         finalPick = x
    #         appender = "lottoList.txt"
    #         file = open(appender, "a")
    #         file.write(finalPick + "\n")
    #         file.close()
    #         print ("here are the lucky lotto picks" + "\n" + finalPick)
    #     continuePrompt()


        # for i in range(6):
        #     theList.append(random.randint(1,59))
        #     finalStrList = ' '.join(map(str,theList))
        #     print(finalStrList)
        #     appender = "lottoList.txt"
        #     file=open(appender, "a")
        #     print ("here are the lucky lotto picks")
        #     # the issue
        #     file.write(finalStrList)
        #     file.close()
        #     continuePrompt(userName,userSurname)
    

def continuePrompt():
    print("we here " + userName + " " + userSurname)
    listOfAnswers1=["Y","YES","Yes","yes", "y"]
    listOfAnswers2=["N","NO","No","no","n"]
    userInput =input("Do you still want more lotto numbers?")
    if userInput == listOfAnswers1[0] or [1] or[2] or [3] or [4]:
        looper()
    elif userInput == listOfAnswers2[0] or [1] or [2] or[3] or [4]:
        print("Alright then "+ userName + "" + userSurname + ".")
        exit()
        


login()
initialize()
looper()
continuePrompt()