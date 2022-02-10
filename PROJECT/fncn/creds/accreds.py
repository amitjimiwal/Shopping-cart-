from ..main_menu import menu
from ..item import pay as p
import mysql.connector as m
mc = m.connect(host='localhost' , user='root' , password='toor' , database='shop',auth_plugin='mysql_native_password')
cur = mc.cursor(buffered=True)
def addcreds(z=0):
    if z == 0:
        x = int(input("Enter amount to Add"))
    else:
        x = z
    p.payment()
    p.purchase(-x,'Added creds')
    print(f'{x} amount is added into your account')
    