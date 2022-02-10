import time
from ..main_menu import menu as m
from ..item import pay as p
def donate ():
    print ("Loading..... PLEASE WAIT!!")
    time.sleep(2)
    print("--------------------------------------------------------------")
    amt=int(input("Enter the amount you want to donate:"))
    p.payment()
    if amt>0:
      print("THanks for donating {} on @SGshoppingcart.com.\n".format(amt))
      print("------------------------------------------------------------")
      menu=input("Press Enter to go back to main menu and exit from Store..:")
      if menu=='':
           m.choices()
    else:
      print("Invalid amount.")
      donate()  