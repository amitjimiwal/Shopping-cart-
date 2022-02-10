import time
import getpass
from ..main_menu import menu as m
from . import pay as p
from ..decor import decor as d 
from .. import session as s
import mysql.connector as mcon
mc = mcon.connect(host="127.0.0.1",username="root",password="toor",database="shop",auth_plugin='mysql_native_password')
cur = mc.cursor()
price_dic = { "rice": 50, "dal": 40, "tea":60, "sugar":30, "biscuit":60, "tedhe medhe":10, "wheat":25, "shampoo":70, "soap":20, "apple":90, "mango":30, "orange":30, "bannana":25, "redmi note 6 pro":6500, "oneplus":45000, "perfume:":100, "ketchup":125, "jam":124, "cheese":20, "ghee":350, "iphone 11 pro":1000000, "ganja":50, "royalstag":254, "ktm":35000, "fortuner":100000, "harley davidson":150000, "rollsroyce":200000, "bughati":1256400}

def itempurchase():
  print ("Loading..... PLEASE WAIT!!\n")
  time.sleep(2)
  cur.execute('select * from products;')
  res = cur.fetchall()
  print("==================================================================")
  print("Following Items available in our shop along with our price\n")
  d.decor(res)
  time.sleep(3)
  bill= s.getusrdata('bill')
  i=0
  
  num_items=100
  list_items=s.getusrdata('cart')
  while num_items>0:
     print("-------------------------------------------------------------")
    
     item=input("ENTER THE ITEM YOU WANT TO PURCHASE.**One at a time**:: ").lower()
                  
     if item in price_dic:
      quantity=int(input("ENTER THE QUANTITY OF THE ITEM .:\n"))
      print("Added {} to your Cart and updated Your bill.\n".format(item))
      print("-------------------------------------------------------------")
      bill=bill  +quantity*price_dic[item]
      list_items.append(item)
      num_items=num_items+1
      i=i+1
     else:
       print("-----------------------------------------------------------")
       print("WE DONT HAVE THIS ITEM AS OF NOW.")
      
       print("-----------------------------------------------------------")
     wish=input("DO YOU WANT TO PURCHASE ANOTHER ITEM. ENTER y/n: ").lower()
     if wish=='y':
       continue
     elif wish !='y' and wish!= 'n':
             time.sleep(2)
             print("======================================================\n")
             print("ERROR.....!!!!!")
             m.choices()
     elif wish=='n':
         if bill!=0:
                s.defusrdata('cart',list_items)
                s.defusrdata('bill',bill)
                time.sleep(2)
                print("------------------------------------------------------------------")

                print("     YOU CAN SIT BACK FOR A WHILE TILL WE GENERATE YOUR BILL.   \n   ")
                time.sleep(3)
                print("------------------------------------------------------------------")

                print("FOLLOWING ARE THE ITEMS YOU HAVE PURCHASED:\n{} and the count of the items is {}.\n".format(list_items,i))
                print("===============================================================")
                time.sleep(4)
                print("YOU NEED TO PAY {} FOR THE ITEM PURCHASED.\n".format(bill))
                print("===============================================================\n")
                print("\n")
                print("===============Delievery info===============\n")
                p.adress()
                print("\n")
                time.sleep(2)
                print("=================Payment info=================")
                p.purchase(bill,d.ats(list_items))

                print("THanks for Shopping With us.\n @SGshopingcart.com \n \n")
                print("===============================================================\n")
         menu=getpass.getpass("Press Enter to go back to main menu and exit from Store..:")
         m.choices()
         
         



     break