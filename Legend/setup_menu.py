""" This script is just a little shell menu to get the desired options for the game from
the player before launching. It determines the user's OS as being either Linux-y or Windows-y 
before entering the command to launch the tcod program. """

import os

def win_and_linux_reset():
    """ resets the terminal window for a Linux or Windows system """

    if os.sep == '/':

        os.system("reset")

    elif os.sep == '\\':

        os.system("cls")

def display_setup_menu():
    """ Display the interactive menu for the player """

    print("LEGENDARY ROGUELIKE\n")
    print("(P)lay\n")
    print("Play with (s)mall font\n")
    print("Play with (l)arge font\n")
    print("(Q)uit\n")

def win_and_linux_launch_str(font=None):
    """ gets the launch string for the desired options and returns it """

    if font:

        if font == "small":

            if os.sep == '/':
        
                return "python3 engine.py --font=small"

            elif os.sep == '\\':

                return "py engine.py --font=small"

        elif font == "large":

            if os.sep == '/':

                return "python3 engine.py --font=large"

            elif os.sep == '\\':

                return "py engine.py --font=large"

    if os.sep == '/':

        return "python3 engine.py"

    elif os.sep == '\\':

        return "py engine.py" 

win_and_linux_reset()

display_setup_menu()

launch_str = "echo Good-bye!"

while True:

    user_input = input("~: ")

    if user_input.upper() == 'P':
      
        launch_str = win_and_linux_launch_str()

        break

    elif user_input.lower() == 's':

        launch_str = win_and_linux_launch_str(font="small")

        break
        
    elif user_input.lower() == 'l':

        launch_str = win_and_linux_launch_str(font="large")

        break

    elif user_input.upper() == 'Q':

        break

    else:

        print("Invalid input! Try again.\n")

os.system(launch_str)
