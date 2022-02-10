import time
from ..main_menu import menu as m

def about_us():
        print("WELCOME TO SGshopingcart,\n @SGshopingcart IS AN ISO CERTIFIED APPLICATION.\n")
        print("SGshopingcart  is a piece of e-commerce software on a web server that allows visitors to an Internet site to select items for eventual purchase.\n")
        time.sleep(2)
        print("The software allows online shopping customers to accumulate a list of items for purchase.\n")
        time.sleep(2)
        print("At the point of sale, the software typically calculates a total for the order, including freight transport, paymentel and many more stuffs.\n The data is used in online marketing.\n")
        
        print("THANKS AND REGARDS,\n @SGshoppingcart\n \n")
        
        
        menu=input("Press Enter to go back to main menu and exit from Store..:")
        if menu=='':
             m.choices()