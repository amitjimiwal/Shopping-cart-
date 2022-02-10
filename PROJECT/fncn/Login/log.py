def Log():
    import mysql.connector as m
    import time
    from datetime import date
    import os
    from os import system
    import getpass
    from .. import session as s
    from ..crypt import encr
    from ..main_menu import menu
    mc = m.connect(host='localhost' , user='root' , password='toor' , database='shop',auth_plugin='mysql_native_password')
    cur = mc.cursor(buffered=True)
    while True:
        system('cls')
        print("------------------------------------------------------------------------------------------")
        #time.sleep(1)
        print("---------------------+_______________________________________________+--------------------")
        #time.sleep(1)
        print("---------------------| 1.                LOGIN                       |--------------------")
        print("---------------------| 2.         Register/Create Account            |--------------------")
        #time.sleep(1)
        print("---------------------+_______________________________________________+--------------------")
        #time.sleep(1)
        print("------------------------------------------------------------------------------------------\n")
        #time.sleep(1)
        x=int(input(':>'))
        if x==1:
            un = input('Enter Username :|')
            #ps = input('Enter Password :|')
            ps = getpass.getpass(prompt="Enter Password :|",stream=None)
            q = f"select * from user where username='{un}' and password = '{encr.enc(ps)}';"
            cur.execute(q)
            r = cur.rowcount
            if r == 1 :
                cur.execute(f"select uid from user where username='{un}' and password = '{encr.enc(ps)}';")
                uid = cur.fetchone()[0]
                print('Login successfull!!!')
                s.createsession(uid)
                if s.getusrdata('del'):
                    x =input('Delete Your Account ?? (Y/N)')
                    if x.capitalize() == 'Y':
                        s.deleteaccount()
			s.logout()
                time.sleep(2)
                print(f'Welcome!! {un}')
                menu.choices()
                break
            else:
                print('username or password incorrect!!!')
                time.sleep(2)
        if x==2:
            while True:
                un = input('Enter username :|')
                q = f"select * from user where username='{un}'"
                cur.execute(q)
                r = cur.rowcount
                if r!=0:
                    print('username already taken')
                    continue
                else:
                    ps = getpass.getpass(prompt="Enter Password :|",stream=None)
                    q = f'select * from user where admin = 0;'
                    cur.execute(q)
                    r = cur.rowcount
                    uid = r + 1
                    q = f"insert into user (uid , admin , username , password ,credits, since , last_purchase) values ({uid} , 0 , '{un}' , '{encr.enc(ps)}' , 0 , '{str(date.today())}' , null);"
                    cur.execute(q)
                    mc.commit()
                    print('created account successfully!!')
                    time.sleep(2)
                    break
