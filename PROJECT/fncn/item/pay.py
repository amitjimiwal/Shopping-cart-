import time
from ..main_menu import menu as m
from ..creds import accreds as a
import mysql.connector as ma
from .. import session as s
mc = ma.connect(host='localhost' , user='root' , password='toor' , database='shop',auth_plugin='mysql_native_password')
cur = mc.cursor(buffered=True)
def purchase(aa,z="null"):
  uid = s.getusrid()
  q = f'select credits from user where uid = {uid};'
  cur.execute(q)
  w = cur.fetchone()[0]
  if aa > w :
    x = input('Insufficient funds in your account , wanna add more ??(Y/N) |')
    if x.capitalize() == 'Y' :
      print(f'{aa - w} amount will be added to your account ! :)')
      mm = input('Wanna change amount ?? (Y/N)')
      if mm.capitalize() == 'Y':
        mz = int(input('Enter Amount :| '))
        a.addcreds(mz)
      else:
        a.addcreds(aa - w)
    else:
      print('Payment Cancelled')
      m.choices()
  uq=f"UPDATE `user` SET `credits` = `credits` - {aa}, `last_purchase` = '{z}' WHERE `user`.`uid` = {uid};"
  cur.execute(uq)
  s.defusrdata('cart',[])
  s.defusrdata('bill',0)
  mc.commit()
def payment():
  print("Select your payment method:\n")
  print(">> 1.Debit card/Credit card..")
  print(">> 2.Paytm..")
  select=int(input("Enter your choice Number:.."))
  if select==1:
        name=input("Enter your name:\n ") 
        bank=input("Enter The Bank of Credit/Debit card in Capital letter.")
        if bank.capitalize() in('Axis','Sbi','Hdfc','Canara','Icici'):
            pay=int(input("Enter Your 6 digit card Number:"))
  
            pin=int(input("Enter four digit pin:"))
            if len(str(pay))==6 and len(str(pin))==4:
                print("\n")
                print("Payment Successful.")
                print("============================================================")
                
            else:
                print("pin or card number is invalid.")
                payment()
        else:
                print(" Sorry, The Bank name YOU entered is not registered with us.")
                print("ERROR!!!!!.......\n")
                print("=============================================================")
                payment()
                
                
                    
                        
                
  elif select==2:
             z=(input("Enter your username:"))              #Entering the username 
             id=int(input("ENTER YOUR 6 DIGIT PAYTM ID:"))
             pas=int(input("ENTER YOUR 3 DIGIT PASSWORD:"))
             if len(str(id))==6 and len(str(pas))==3:
                     print("PAYMENT SUCCESSFULLY DONE.")
                     
                     

        
def adress():
  address=input("Enter your residental adress along with your city:")
  
  state=input("Enter State:")           
  print("Your item will be delieverd as soon as possible.\n")
  print("--------------------------------------------------------------")