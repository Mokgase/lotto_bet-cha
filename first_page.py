import random

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
            print("lets try again")
            initialize()


    #  appender = "animeGenre.txt"
    #  file = open(appender, "a")
    #     title = input("Enter the anime you want to add to your list: ")
    #     file.write(title + "\n")
    #     file.close()

def looper():        
    theList = []
    for i in range(6):
        theList.append(random.randint(1,59))
        finalStrList = ' '.join(map(str,theList))
        print(finalStrList)
        appender = "lottoList.txt"
        file=open(appender, 'w')
        print ("here are the lucky lotto picks")
        # the issue
        file.write(finalStrList)
        file.write('\n')
        file.close()
    continuePrompt()


    

def continuePrompt():
    userInput =input("Do you still want more lotto numbers?: ")
    if userInput == "Y" or "YES" or "Yes" or "yes" or "y":
        print("okay here goes...")  
        looper()
    else:
        print(f"Alright then {userName} {userSurname}...")
        options()
        
def options():
    # Array to hold items
    moreOptionsArray = ["HELP","CLEAR","KILL","DISPLAY"]
    
    # Allow user to clear txt file
    theClearer = 'lottoList.txt'
    optionsInput = input("If there's anything more you want to do press Enter: ")
    if optionsInput == "":
        print("HELP - Displays extra functions of the program \n CLEAR - Clears all the data held within the file KILL - Kills the whole program \n DISPLAY- Displays all the numbers inside the file")
        

        # with open(theClearer, 'w') as file:
        #     file.truncate(0)
        #     print(f"Contents of {theClearer} cleared successfully...")
        #     continuePrompt()
    elif optionsInput == "N" or "YES" or "Yes" or "yes" or "y":
        print(f"Goodbye {userName} {userSurname}.")
        exit()
    
    # allow user to print numbers
    # allow user to kill program also

        
login()
initialize()
# looper()
# continuePrompt()