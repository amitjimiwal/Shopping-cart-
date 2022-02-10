import time
from ..main_menu import menu as m

def bonus():
        print("--------------------------------------------------------------")
        print("You will get only 2 chances.\n")
        import random
        
        
        win=random.randint(1,19)
        attempt=1
        while attempt<3:
                chance=int(input("Enter a number b/w 1 -20:.."))
                if chance<20 and chance>=1:
                   if chance==win:
                      print(" HURRAH,!!.......WON...!!!")
                      print("YOU won {} BONUS.\n CONGRATULATIONS!!!!".format(random.randint(20000,30000)))
                   else:
                        print("LOOSE!......\n")
                        
                else:
                        print("ENTER NUMBER B/W 1-20 ONLY.\n YOUR {} CHANCE IS SPEND UP.".format(attempt))
                attempt=attempt+1
        menu=input("Press Enter to go back to main menu and exit from Store..:")
        if menu=='':
             m.choices() 