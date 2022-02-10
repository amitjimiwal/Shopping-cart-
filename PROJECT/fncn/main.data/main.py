import time

price_dic = { "rice": 50, "dal": 40, "tea":60, "sugar":30, "biscuit":60, "tedhe medhe":10, "wheat":25, "shampoo":70, "soap":20, "apple":90, "mango":30, "orange":30, "bannana":25, "redmi note 6 pro":6500, "oneplus":45000, "perfume:":100, "ketchup":125, "jam":124, "cheese":20, "ghee":350, "iphone 11 pro":1000000, "ganja":50, "royalstag":254, "ktm":35000, "fortuner":100000, "harley davidson":150000, "rollsroyce":200000, "bughati":1256400}

  
def itempurchase():
  print ("Loading..... PLEASE WAIT!!\n")
  time.sleep(2)
  print("==================================================================")
  print("Following Items available in our shop along with our price\n")
  for dic in price_dic:
        print(dic,":",price_dic[dic])
  time.sleep(3)
  bill=0
  i=0
  
  num_items=100
  list_items=[]
  while num_items>0:
     print("-------------------------------------------------------------")
    
     item=input("ENTER THE ITEM YOU WANT TO PURCHASE.**One at a time**::").lower()
                  
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
             choices()
     elif wish=='n':
         if bill!=0:
                 
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
                adress()
                print("\n")
                time.sleep(2)
                print("=================Payment info=================")
                payment()

                print("THanks for Shopping With us.\n @AJshopingcart.com \n \n")
                print("===============================================================\n")
         menu=input("Press Enter to go back to main menu and exit from Store..:")
         if menu=='':
             choices()
         else:
            menu=input("Press Enter to go back to main menu and exit from Store..:")
            if menu=='':
              choices()
         



     break
     
             
             
     
def payment():
  print("Select your payment method:\n")
  print(">> 1.Debit card/Credit card..")
  print(">> 2.Paytm..")
  select=int(input("Enter your choice Number:.."))
  if select==1:
        name=input("Enter your name:\n ") 
        bank=input("Enter The Bank of Credit/Debit card in Capital letter.")
        if bank in('AXIS','SBI','HDFC','CANARA','ICICI'):
            pay=int(input("Enter Your 6 digit card Number:"))
  
            pin=int(input("Enter four digit pin:"))
            if pay>100000 and pin>=1000:
                print("\n")
                print("Payment Successful.")
                print("============================================================")
                
            else:
                print("pin or card number is invalid.")
                payment()
        else:
                print(" Sorry, The Bank name YOU entered is not registered with us.")
                print("EROOR!!!!!.......\n")
                print("=============================================================")
                payment()
                
                
                    
                        
                
  elif select==2:
             z=(input("Enter your username:"))              #Entering the username 
             id=int(input("ENTER YOUR 6 DIGIT PAYTM ID:"))
             pas=int(input("ENTER YOUR THREE DIGIT PASSWORD:"))
             if len(str(id))==6 and len(str(pas))==3:
                     print("PAYMENT SUCCESSFULLY DONE.")
                     
                     

        
def adress():
  address=input("Enter your residental adress along with your city:")
  
  state=input("Enter State:")           
  print("Your item will be delieverd as soon as possible.\n")
  print("--------------------------------------------------------------")
  
        
def donate ():
    print ("Loading..... PLEASE WAIT!!")
    time.sleep(2)
    print("--------------------------------------------------------------")
    amt=int(input("Enter the amount you want to donate:"))
    if amt>0:
      print("THanks for donating {} on @SGshoppingcart.com.\n".format(amt))
      print("------------------------------------------------------------")
      menu=input("Press Enter to go back to main menu and exit from Store..:")
      if menu=='':
           choices()
    else:
      print("Invalid amount.")
      donate()  
   

    
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
             choices()
        
        
        
def complaint():
    print ("Loading..... PLEASE WAIT!!")
    time.sleep(2)
    comp=input("Enter Your complaint:")
    time.sleep(3)
    print("\n")
    print ("We have taken your complaint.\n We will take positive steps towards it.\n")
    print("THanks.\n@SGshoppingcart.com\n" )
    print("=============================================================\n")
    menu=input("Press Enter to go back to main menu and exit from Store..:")
    if menu=='':
             choices()
    
    
def other():
    print ("Loading..... PLEASE WAIT!!")
    print("--------------------------------------------------------------")
    time.sleep (3)
    print ("Content yet to be added")
    time.sleep(2)
    choices()
   
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
             choices()        

def welcome():
        
       print("------------------------------------------------------------------------------------------")
       time.sleep(1)
       print("------------------------------------------------------------------------------------------")
       time.sleep(1)
       print("                           WELCOME TO SGshoppingcart.com SHOP                             ")
       print("                  HERE YOU WILL GET YOUR DAILYUSE ITEMS AT A CHEAP RATE"                   )
       time.sleep(1)
       print("------------------------------------------------------------------------------------------")
       time.sleep(1)
       print("------------------------------------------------------------------------------------------\n")
       time.sleep(1)



            
                
        
        
def choices():
        print("============================    CHOOSE FROM BELOW OPTION:     ============================\n")
        print("  #    >> 1. Item Purchase                       #")
        print("  #    >> 2. Complain                            #")
        print("  #    >> 3. Donate                              #")
        print("  #    >> 4. About @SGshoppingcart               #")
        print("  #    >> 5. Any Other                           #")
        print("  #    >> 6. Earn Bonus.                         #")
        print("  #    >> 7. Exit from the store.                #\n")
        
        
        time.sleep(2)
        choice=int(input("ENTER YOUR CHOICE:(Option number)::"))
        time.sleep(2)
        if choice==1:
          itempurchase()
        elif choice==2:
          complaint()
        elif choice==3:
          donate()
        elif choice==4:
                about_us()
        elif choice==7:
           print("EXITTING FROM OUR STORE.\n")
           print("EXITED.\n")
           print("THANKS \n @SGshoppingcart")
        elif choice==6:
                bonus()
        elif choice >7:
           print('Please enter Valid choice')
        else:
          other()   
          
          
      
welcome()   
choices()
