import time
from ..item import itm
from ..about_us import abt
from ..bonus import b
from ..complaint import comp
from ..donate import don
from ..creds import accreds as a
from .. import session as s
from ..item import pay as p
from ..decor import decor as d 
from ..other import o
def choices():
        print("============================    CHOOSE FROM BELOW OPTION:     ============================\n")
        print("  #    >> 1.  Item Purchase                       #")
        print("  #    >> 2.  Complain                            #")
        print("  #    >> 3.  Donate                              #")
        print("  #    >> 4.  About @SGshoppingcart               #")
        print("  #    >> 5.  Any Other                           #")
        print("  #    >> 6.  Earn Bonus.                         #")
        print("  #    >> 7.  Add creds to your account           #")
        print("  #    >> 8.  Change Account Password             #")
        print("  #    >> 9.  Delete Account                      #")
        print("  #    >> 10. Get Cart Info                       #")
        print("  #    >> 11. Exit from the store.      (Log_Out) #\n")
        
        
        time.sleep(2)
        choice=int(input("ENTER YOUR CHOICE:(Option number)::"))
        time.sleep(2)
        if choice==1:
          itm.itempurchase()
        elif choice==2:
          comp.complaint()
        elif choice==3:
          don.donate()
        elif choice==4:
          abt.about_us()
        elif choice==11:
           print("EXITTING FROM OUR STORE.\n")
           s.logout()
           print("EXITED.\n")
           print("THANKS \n @SGshoppingcart")
        elif choice==6:
          b.bonus()
        elif choice==7:
           a.addcreds()
           choices()
        elif choice==8:
           s.changepass()
           choices()
        elif choice==10:
           print('\nCart')
           print(s.getusrdata('cart'))
           print('\nBill')
           print(s.getusrdata('bill'))
           print('\n')
           x = input('Purchasae (P) Clear Cart (C) :|')
           if x.capitalize() == 'P':
             p.purchase(s.getusrdata('bill'),d.ats(s.getusrdata('cart')))
           elif x.capitalize() == 'C' :
             s.defusrdata('cart',[])
             s.defusrdata('bill',0)
           else:
             print('=================================================')
             time.sleep(1)
             choices()
        elif choice==9:
          x = input('Are you sure u want to delet account ?? (Y/N)')
          if x.capitalize() == 'Y':
            print('Re-Login to Delete Account !!')
            s.defusrdata('del',True)
        elif choice >11:
           print('Please enter Valid choice')
        else:
          o.other()