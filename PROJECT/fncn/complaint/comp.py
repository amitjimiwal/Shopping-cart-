import time
from ..main_menu import menu as m

def complaint():
    print ("Loading..... PLEASE WAIT!!")
    time.sleep(2)
    comp=input("Enter Your complaint:")
    time.sleep(3)
    print("\n")
    print ("We have taken your complaint.\n We will take positive steps towards it.\n")
    print("Thanks.\n@SGshoppingcart.com\n" )
    print("=============================================================\n")
    while True:
        menu=input("Press Enter to go back to main menu and exit from Store..:")
        if menu=='':
                m.choices()
                break
        else:
            print('Please provide correct Input')
            continue