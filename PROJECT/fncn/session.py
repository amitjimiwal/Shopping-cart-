import os
import sys
import pickle
import getpass
import mysql.connector as ma
import pathlib
from .crypt import encr as e
from os import system
mc = ma.connect(host='localhost' , user='root' , password='toor' , database='shop',auth_plugin='mysql_native_password')
cur = mc.cursor(buffered=True)
def createsession(uid):
    cd = pathlib.Path().absolute()
    os.makedirs(os.path.join(cd , "data"), exist_ok = True)
    fts = open('data\\sessions.dll','w+')
    fts.write(f'{uid}')
    fts.close()
    try:
        fts = open(f'data\\{uid}\\userdata.dll','rb')
    except FileNotFoundError:
        usrdata(uid)
    else:
        fts.close()
def logout():
    fts = open('data\\sessions.dll','w+')
    fts.write('')
    fts.close()
def usrdata(uid):
    cd = pathlib.Path().absolute()
    z = f'data\\{uid}'
    os.makedirs(os.path.join(cd , z ), exist_ok = True)
    fts = open(f'data\\{uid}\\userdata.dll','wb+')
    q = {'cart': [],'bill':0}
    pickle.dump(q , fts)
    fts.close()
def getusrdata(param):
    fts = open(f'data\\{getusrid()}\\userdata.dll','rb+')
    to = pickle.load(fts)
    fts.close()
    try:
        reqo = to[param]
    except:
        reqo = False
    return reqo
def defusrdata(param , val):
    fts = open(f'data\\{getusrid()}\\userdata.dll','rb+')
    to = pickle.load(fts)
    fts.close()
    to[param] = val
    fts = open(f'data\\{getusrid()}\\userdata.dll','wb+')
    pickle.dump(to , fts)
    fts.close()
def getusrid():
    fts = open('data\\sessions.dll','r+')
    uid = fts.read()
    fts.close()
    uid = int(uid.strip(' '))
    return uid
def changepass():
    uq=f"UPDATE `user` SET `password` = '{e.enc(getpass.getpass('Enter New Password :|'))}' WHERE `user`.`uid` = {getusrid()} and `user`.`password` = '{e.enc(getpass.getpass('Enter Old Password :|'))}';"
    cur.execute(uq)
    print('Password Changed ,if you entered correct old passsword !!!!')
    mc.commit()
def deleteaccount():
    q = f'DELETE from user where `user`.`uid` = {getusrid()}'
    cur.execute(q)
    mc.commit()