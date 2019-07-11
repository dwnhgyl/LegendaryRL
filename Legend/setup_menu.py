
import os

os.system("reset")

print("LEGENDARY ROGUELIKE\n")
print("(P)lay\n")
print("Play with (s)mall font\n")
print("Play with (l)arge font\n")
print("(Q)uit\n")

launching_game = "echo Good-bye!"

while True:

    user_input = input("~: ")

    if user_input.upper() == 'P':
       
        if os.sep == '/':

            launching_game = "python3 engine.py"

        elif os.sep == '\\':
 
            launching_game = "py engine.py" 

        break

    elif user_input.lower() == 's':

        if os.sep == '/':

            launching_game = "python3 engine.py --font=small"

        elif os.sep == '\\':
 
            launching_game = "py engine.py --font=small" 

        break
        
    elif user_input.lower() == 'l':

        if os.sep == '/':

            launching_game = "python3 engine.py --font=large"

        elif os.sep == '\\':
 
            launching_game = "py engine.py --font=large" 

        break

    elif user_input.upper() == 'Q':

        break

    else:

        print("Invalid input! Try again.\n")

os.system(launching_game)
