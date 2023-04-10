import random

valid_commands =['','help','clear','kill' ,'display']
theList = []
def get_user_name():
    name = input("Enter your name:")
    while len(name)== 0:
        name = input("Please enter your name: ")
    surname = input("Enter you surname:")
    while len(surname)== 0:
        surname = input("Please enter your surname: ")
    return name & surname

def initialize(name):
    while True :
        prompt = input(f'{name}, please press Enter to begin.')
        command = input(prompt)
        while len(command) == 0 or not valid_command(command):
            output(f'{name}, Please press Enter to begin, not "{command}"')
            command = input(prompt)
        return command.lower()
    
        # if userInput == "":
        #     looper()
        # else:
        #     print("lets try again")
        #     initialize()


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

def continuePrompt(name,surname):
    prompt = '' + name + 'Do you still want more lotto numbers generated again?: '
    command = input(prompt)
    while len(command) == 0 or not valid_commands(command):
        output(name,"Sorry, I did not understand '"+command+"'.")
        command = input(prompt)
    return command.lower()
    # continueInput =input(" ")
    # if continueInput == "Y" or "YES" or "Yes" or "yes" or "y":
    #     print("okay here goes...")  
        
    # elif continueInput == "N" or "NO" or "No" or "no" or "n":
    #     print(f"Okay then {name} {surname}")
    #     return options()
    # else:
    #     print(f"Alright then {name} {surname}...Goodbye ;-)")
    #     exit()

def output(name,message):
    print(''+name+":"+ message)
        
def do_help():
    """
    Provides help information to the user
    :return: (True, help text) to indicate number generation can continue after this command was handled
    """
    return True, """I can understand these commands:
HELP - Displays extra functions of the program
CLEAR - Clears all the data held within the file
KILL - Kills the whole program
DISPLAY- Displays all the numbers inside the file
"""
def options(name,surname):
    # Array to hold items
    moreOptionsArray = ["HELP","CLEAR","KILL","DISPLAY"]
    
    # Allow user to clear txt file
    theClearer = 'lottoList.txt'
    optionsInput = input("If there's anything more you want to do press Enter: ")
    if optionsInput == "":
        print(" \n   \n ")
        

        # with open(theClearer, 'w') as file:
        #     file.truncate(0)
        #     print(f"Contents of {theClearer} cleared successfully...")
        #     continuePrompt()
    elif optionsInput == "N" or "YES" or "Yes" or "yes" or "y":
        print(f"Goodbye {name} {surname}.")
        exit()
    
    # allow user to print numbers
    # allow user to kill program also
def valid_command(command):
    """
Returns a boolean indicating if the robot can understand the command or not
Also checks if there is an argument to the command, and if it a valid int
"""

# (command_name, arg1) = split_command_input(command)

# if command_name.lower() == 'help':
#     if len(arg1.strip()) == 0:
#         return True
#     elif (arg1.lower().find('silent') > -1 or arg1.lower().find('reversed') > -1) and len(arg1.lower().replace('silent', '').replace('reversed','').strip()) == 0:
#         return True
#     else:
#         range_args = arg1.replace('silent', '').replace('reversed','')
#         if is_int(range_args):
#             return True
#         else:
#             range_args = range_args.split('-')
#             return is_int(range_args[0]) and is_int(range_args[1]) and len(range_args) == 2
# else:
#     return command_name.lower() in valid_commands and (len(arg1) == 0 or is_int(arg1))

def call_command(command_name):
    if command_name == 'help':
        return do_help()



if __name__ == "__main__":
    get_user_name()
    

    

# # list of valid command names
# valid_commands = ['off', 'help', 'replay', 'forward', 'back', 'right', 'left', 'sprint']
# move_commands = valid_commands[3:]

# history = []


# def get_command(robot_name):
#     """
#     Asks the user for a command, and validate it as well
#     Only return a valid command
#     """

#     prompt = ''+robot_name+': What must I do next? '
#     command = input(prompt)
#     while len(command) == 0 or not valid_command(command):
        # output(robot_name, "Sorry, I did not understand '"+command+"'.")
#         command = input(prompt)

#     return command.lower()


# def split_command_input(command):
#     """
#     Splits the string at the first space character, to get the actual command, as well as the argument(s) for the command
#     :return: (command, argument)
#     """
#     args = command.split(' ', 1)
#     if len(args) > 1:
#         return args[0], args[1]
#     return args[0], ''


# def is_int(value):
#     """
#     Tests if the string value is an int or not
#     :param value: a string value to test
#     :return: True if it is an int
#     """
#     try:
#         int(value)
#         return True
#     except ValueError:
#         return False


# def valid_command(command):
#     """
#     Returns a boolean indicating if the robot can understand the command or not
#     Also checks if there is an argument to the command, and if it a valid int
#     """

#     (command_name, arg1) = split_command_input(command)

#     if command_name.lower() == 'replay':
#         if len(arg1.strip()) == 0:
#             return True
#         elif (arg1.lower().find('silent') > -1 or arg1.lower().find('reversed') > -1) and len(arg1.lower().replace('silent', '').replace('reversed','').strip()) == 0:
#             return True
#         else:
#             range_args = arg1.replace('silent', '').replace('reversed','')
#             if is_int(range_args):
#                 return True
#             else:
#                 range_args = range_args.split('-')
#                 return is_int(range_args[0]) and is_int(range_args[1]) and len(range_args) == 2
#     else:
#         return command_name.lower() in valid_commands and (len(arg1) == 0 or is_int(arg1))


# def output(name, message):
#     print(''+name+": "+message)


# def do_help():
#     """
#     Provides help information to the user
#     :return: (True, help text) to indicate robot can continue after this command was handled
#     """
#     return True, """I can understand these commands:
# OFF  - Shut down robot
# HELP - provide information about commands
# FORWARD - move forward by specified number of steps, e.g. 'FORWARD 10'
# BACK - move backward by specified number of steps, e.g. 'BACK 10'
# RIGHT - turn right by 90 degrees
# LEFT - turn left by 90 degrees
# SPRINT - sprint forward according to a formula
# REPLAY - replays all movement commands from history [FORWARD, BACK, RIGHT, LEFT, SPRINT]
# """


# def get_commands_history(reverse, relativeStart, relativeEnd):
#     """
#     Retrieve the commands from history list, already breaking them up into (command_name, arguments) tuples
#     :param reverse: if True, then reverse the list
#     :param relativeStart: the start index relative to the end position of command, e.g. -5 means from index len(commands)-5; None means from beginning
#     :param relativeEnd: the start index relative to the end position of command, e.g. -1 means from index len(commands)-1; None means to the end
#     :return: return list of (command_name, arguments) tuples
#     """

#     commands_to_replay = [(name, args) for (name, args) in list(map(lambda command: split_command_input(command), history)) if name in move_commands]
#     if reverse:
#         commands_to_replay.reverse()

#     range_start = len(commands_to_replay) + relativeStart if (relativeStart is not None and (len(commands_to_replay) + relativeStart) >= 0) else 0
#     range_end = len(commands_to_replay) + relativeEnd if  (relativeEnd is not None and (len(commands_to_replay) + relativeEnd) >= 0 and relativeEnd > relativeStart) else len(commands_to_replay)
#     return commands_to_replay[range_start:range_end]


# def do_replay(robot_name, arguments):
#     """
#     Replays historic commands
#     :param robot_name:
#     :param arguments a string containing arguments for the replay command
#     :return: True, output string
#     """

#     silent = arguments.lower().find('silent') > -1
#     reverse = arguments.lower().find('reversed') > -1
#     range_args = arguments.lower().replace('silent', '').replace('reversed', '')

#     range_start = None
#     range_end = None

#     if len(range_args.strip()) > 0:
#         if is_int(range_args):
#             range_start = -int(range_args)
#         else:
#             range_args = range_args.split('-')
#             range_start = -int(range_args[0])
#             range_end = -int(range_args[1])

#     commands_to_replay = get_commands_history(reverse, range_start, range_end)

#     for (command_name, command_arg) in commands_to_replay:
#         (do_next, command_output) = call_command(command_name, command_arg, robot_name)
#         if not silent:
#             print(command_output)
#             world.show_position(robot_name)

#     return True, ' > '+robot_name+' replayed ' + str(len(commands_to_replay)) + ' commands' + (' in reverse' if reverse else '') + (' silently.' if silent else '.')


# def call_command(command_name, command_arg, robot_name):
#     if command_name == 'help':
#         return do_help()
#     elif command_name == 'forward':
#         return world.do_forward(robot_name, int(command_arg))
#     elif command_name == 'back':
#         return world.do_back(robot_name, int(command_arg))
#     elif command_name == 'right':
#         return world.do_right_turn(robot_name)
#     elif command_name == 'left':
#         return world.do_left_turn(robot_name)
#     elif command_name == 'sprint':
#         return world.do_sprint(robot_name, int(command_arg))
#     elif command_name == 'replay':
#         return do_replay(robot_name, command_arg)
#     return False, None


# def handle_command(robot_name, command):
#     """
#     Handles a command by asking different functions to handle each command.
#     :param robot_name: the name given to robot
#     :param command: the command entered by user
#     :return: `True` if the robot must continue after the command, or else `False` if robot must shutdown
#     """

#     (command_name, arg) = split_command_input(command)

#     if command_name == 'off':
#         return False
#     else:
#         (do_next, command_output) = call_command(command_name, arg, robot_name)

#     print(command_output)
#     world.show_position(robot_name)
#     add_to_history(command)

#     return do_next


# def add_to_history(command):
#     """
#     Adds the command to the history list of commands
#     :param command:
#     :return:
#     """
#     history.append(command)


# def robot_start():
#     """This is the entry point for starting my robot"""

#     global history

#     robot_name = get_robot_name()
#     output(robot_name, "Hello kiddo!")
#     world.reset()
#     list_obstacles = obst.get_obstacles()
 
    
#     if "turtle" in sys.argv:
#         if len(list_obstacles) > 0:    
#             obst.show_postions()
#             world.drawing_obstacles(list_obstacles) 
#     else:
#         if len(list_obstacles) > 0:
#             obst.show_postions()
        
#     history = []

#     command = get_command(robot_name)
#     while handle_command(robot_name, command):
#         command = get_command(robot_name)

#     output(robot_name, "Shutting down..")





# if __name__ == "__main__":
#     robot_start()
    