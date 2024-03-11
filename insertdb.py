import sqlite3
import random
import datetime
import getdb 
import genpk
import updatedb
sqlfile = 'DBlite.db'

def convertToBinaryData(filename):
    # Convert digital data to binary format
    with open(filename, 'rb') as file:
        blobData = file.read()
    return blobData

def insert_product(proname, photo, value_pro,disciption,price,id_brand,id_type):
    try:
        sqliteConnection = sqlite3.connect(sqlfile)
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")
        sqlite_insert_blob_query = """ INSERT INTO 'สินค้า'
                                  ('รหัสสินค้า','ชื่อสินค้า', 'รูปสินค้า', 'สินค้าคงเหลือ','รายละเอียดสินค้า','ราคาสินค้าต่อหน่วย','รหัสยี่ห้อสินค้า','รหัสประเภทสินค้า') VALUES (?, ?, ?, ?, ?, ?, ?,?)"""

        photo = convertToBinaryData(photo)
        # Convert data into tuple format
        id_pro = genpk.gen_pk_nvar6(getdb.get_last_row_product())
        data_tuple = (id_pro,proname, photo, value_pro,disciption,price,id_brand,id_type)
        cursor.execute(sqlite_insert_blob_query, data_tuple)
        sqliteConnection.commit()
        print("Product insert successfully as a BLOB into a table")
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to insert product data into sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("the sqlite connection is closed")


def insert_order(id_customer):
    try:
        sqliteConnection = sqlite3.connect(sqlfile)
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")

        # insert developer detail
        sqlite_insert_with_param = """INSERT INTO 'การขาย'
                          ('รหัสการขาย','รหัสพนักงาน','รหัสลูกค้า','วันเวลาที่สั่ง',สถานะการขาย) 
                          VALUES (?, ?, ?, ?, ?);"""
        id_order = genpk.gen_pk_nvar6(getdb.get_last_row_order())
        ran = random.choice(getdb.get_id_employee())
        id_admin = ran
        status = 'รอชำระ'
        date_time = datetime.datetime.now() 
        data_tuple = (id_order,id_admin,id_customer, date_time,status)
        cursor.execute(sqlite_insert_with_param, data_tuple)
        sqliteConnection.commit()
        print("Order insert successfully \n")
        cursor.close()
        insert_payment(id_order)
    except sqlite3.Error as error:
        print("Error while working with SQLite", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("sqlite connection is closed")
            
            
            
def insert_orderdetail(id_order,id_pro,value_order_product):
    try:
        sqliteConnection = sqlite3.connect(sqlfile)
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")

        # insert developer detail
        sqlite_insert_with_param = """INSERT INTO 'รายละเอียดการขาย'
                          ('รหัสรายละเอียดการขาย','ราคาต่อหน่วย','จำนวน','รหัสการขาย',รหัสสินค้า) 
                          VALUES (?, ?, ?, ?, ?);"""
        id_orderdetail =genpk.gen_pk_nvar6(getdb.get_last_row_orderdetail())     
        price = getdb.get_price(id_pro)

        data_tuple = (id_orderdetail,price,value_order_product,id_order,id_pro)
        cursor.execute(sqlite_insert_with_param, data_tuple)
        sqliteConnection.commit()
        print("Order detail insert successfully \n")
        cursor.close()
        updatedb.update_datetime_order(id_order)
        updatedb.update_price_payment(id_order)
    except sqlite3.Error as error:
        print("Error while working with SQLite", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("sqlite connection is closed")
            
def insert_payment(id_order):
    try:
        sqliteConnection = sqlite3.connect(sqlfile)
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")
        sqlite_insert_blob_query = """ INSERT INTO 'การชำระ'
                                  ('รหัสการชำระ','รหัสการขาย', 'ยอดชำระ','username') VALUES (?, ?, ?, ?)"""

        total_price = getdb.get_totalprice(id_order)
        username = getdb.get_username(id_order)
        id_payment = genpk.gen_pk_nvar6(getdb.get_last_row_payment())
        # Convert data into tuple format
        data_tuple = (id_payment,id_order,total_price,username)
        cursor.execute(sqlite_insert_blob_query, data_tuple)
        sqliteConnection.commit()
        print("Payment insert successfully as a BLOB into a table")
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to insert product data into sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("the sqlite connection is closed")
            
            
def insert_customer(name,lastname,username,password,mail,tel,adderss,bday,bmonth,byear):
    try:
        sqliteConnection = sqlite3.connect(sqlfile)
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")
        # insert developer detail
        sqlite_insert_with_param = """INSERT INTO 'ลูกค้า'
                          ('รหัสลูกค้า','ชื่อจริง','นามสกุล','username','password','อีเมล','เบอร์โทรศัพท์','ที่อยู่','วันเดือนปีเกิด') 
                          VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);"""
        id_cus = genpk.gen_pk_nvar6(getdb.get_last_row_customer())
        brith_day = datetime.date(byear,bmonth,bday)
        data_tuple = (id_cus,name,lastname,username,password,mail,tel,adderss,brith_day)
        cursor.execute(sqlite_insert_with_param, data_tuple)
        sqliteConnection.commit()
        print("Customer insert successfully \n")
        cursor.close()
    except sqlite3.Error as error:
        print("Error while working with SQLite", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("sqlite connection is closed")
            
def insert_employee(name,lastname,tel,username,password):
    try:
        sqliteConnection = sqlite3.connect(sqlfile)
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")

        # insert developer detail
        sqlite_insert_with_param = """INSERT INTO 'พนักงาน'
                          ('รหัสพนักงาน','ชื่อจริง','นามสกุล','เบอร์โทรศัพท์','username','password') 
                          VALUES (?, ?, ?, ?, ?, ?);"""

        id_emp = genpk.gen_pk_nvar4(getdb.get_last_row_employee())

        data_tuple = (id_emp,name,lastname,tel,username,password)
        cursor.execute(sqlite_insert_with_param, data_tuple)
        sqliteConnection.commit()
        print("Employee insert successfully \n")
        cursor.close()

    except sqlite3.Error as error:
        print("Error while working with SQLite", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("sqlite connection is closed")
            
def insert_probrand(name_brnd):
    try:
        sqliteConnection = sqlite3.connect(sqlfile)
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")

        # insert developer detail
        sqlite_insert_with_param = """INSERT INTO 'ยี่ห้อ'
                          ('รหัสยี่ห้อสินค้า','ชื่อยี่ห้อสินค้า') 
                          VALUES (?, ?);"""

        id_brand = genpk.gen_pk_nvar4(getdb.get_last_row_brand())

        data_tuple = (id_brand,name_brnd)
        cursor.execute(sqlite_insert_with_param, data_tuple)
        sqliteConnection.commit()
        print("Product brand insert successfully \n")
        cursor.close()

    except sqlite3.Error as error:
        print("Error while working with SQLite", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("sqlite connection is closed")
def insert_protype(name_type):
    try:
        sqliteConnection = sqlite3.connect(sqlfile)
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")

        # insert developer detail
        sqlite_insert_with_param = """INSERT INTO 'ประเภทสินค้า'
                          ('รหัสประเภทสินค้า','ชื่อประเภทสินค้า') 
                          VALUES (?, ?);"""

        id_type = genpk.gen_pk_nvar4(getdb.get_last_row_type())

        data_tuple = (id_type,name_type)
        cursor.execute(sqlite_insert_with_param, data_tuple)
        sqliteConnection.commit()
        print("Product type insert successfully \n")
        cursor.close()

    except sqlite3.Error as error:
        print("Error while working with SQLite", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("sqlite connection is closed")
            
            
            
#insert_customer('Somnamna','Narak','Somjai','sasake','sasemekyou@gmail.com','0992348097','Bankok',9,8,2002)
# insert_employee('ณัทชพล','แดงฉ่ำ','0998765743','nutnut','dango124')
# insert_probrand('VS')
# insert_protype('รองเท้าวิ่ง')