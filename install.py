import mysql.connector as m


price_dic = { "rice": 50, "dal": 40, "tea":60, "sugar":30, "biscuit":60, "tedhe medhe":10, "wheat":25, "shampoo":70, "soap":20, "apple":90, "mango":30, "orange":30, "bannana":25, "redmi note 6 pro":6500, "oneplus":45000, "perfume:":100, "ketchup":125, "jam":124, "cheese":20, "ghee":350, "iphone 11 pro":1000000, "ganja":50, "royalstag":254, "ktm":35000, "fortuner":100000, "harley davidson":150000, "rollsroyce":200000, "bughati":1256400}
mc = m.connect(host='localhost' , user='root' , password='toor' , database='shop',auth_plugin='mysql_native_password')
cur = mc.cursor(buffered=True)
x=input('Table products exists? (Y/N)')
if x.capitalize() == 'N':
    cur.execute('create table products(name varchar(20) , price int)')
else:
    cur.execute('drop table products')
    cur.execute('create table products(name varchar(20) , price int)')
for i in price_dic:
    cur.execute(f'insert into products(name , price) values("{i}" , {price_dic[i]})')
    print(f'added item "{i}" with price as {price_dic[i]} in table products')
print('Successfully Created Table Products')
x=input('Table user exists? (Y/N)')
if x.capitalize() == 'N':
    pk="ALTER TABLE `user` ADD PRIMARY KEY(`uid`);"
    cur.execute('create table user(uid int, admin int, username varchar(100), password varchar(100),credits int, since varchar(100), last_purchase varchar(100))')
    cur.execute(pk)
else:
    cur.execute('drop table user')
    cur.execute('create table user(uid int, admin int, username varchar(100), password varchar(100),credits int, since varchar(100), last_purchase varchar(100))')
    cur.execute(pk)
print('Successfully Created Table User')
x=input('Press Enter to Exit :(><) ')