import sqlite3
import datetime
import getdb 

sqlfile = 'DBlite.db'
def convertToBinaryData(filename):
    # Convert digital data to binary format
    with open(filename, 'rb') as file:
        blobData = file.read()
    return blobData

def update_minus_value_product (id_order):
    try:
        sqliteConnection = sqlite3.connect(sqlfile)
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")
        sql_update_query = """Update สินค้า set สินค้าคงเหลือ = ? where รหัสสินค้า = ?"""
        for i in getdb.get_raw_idpro_valuepro_valueorderpro_statusorder(id_order):
            if i[3] == 'ชำระเสร็จสิ้น':
                data = (i[1]-i[2], i[0])
                cursor.execute(sql_update_query, data)
                sqliteConnection.commit()
                print("Record Updated successfully")               
        cursor.close()
    except sqlite3.Error as error:
        print("Failed to update sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The sqlite connection is closed")


def update_vertify_payment (id_order):
    try:
        sqliteConnection = sqlite3.connect(sqlfile)
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")

        sql_update_query = """Update การขาย set สถานะการขาย = ? where รหัสการขาย = ?"""
        
        status = 'ชำระเสร็จสิ้น'
        data = (status, id_order)
        cursor.execute(sql_update_query, data)
        sqliteConnection.commit()
        print("Record Updated successfully")
        cursor.close()
        update_minus_value_product(id_order)

    except sqlite3.Error as error:
        print("Failed to update sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The sqlite connection is closed")
            
def update_price_of_product (id_pro,price):
    try:
        sqliteConnection = sqlite3.connect(sqlfile)
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")

        sql_update_query = """Update สินค้า set ราคาต่อหน่วย = ? where รหัสสินค้า = ?"""
        
        
        data = (price, id_pro)
        cursor.execute(sql_update_query, data)
        sqliteConnection.commit()
        print("Record Updated successfully")
        cursor.close()
    except sqlite3.Error as error:
        print("Failed to update sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The sqlite connection is closed")
            
            
def update_plus_value_product (id_pro,plus):
    try:
        value = getdb.get_value_pro(id_pro)
        sqliteConnection = sqlite3.connect(sqlfile)
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")
        sql_update_query = """Update สินค้า set สินค้าคงเหลือ = ? where รหัสสินค้า = ?"""

        value_plus = value + plus
        data = (value_plus,id_pro)
        cursor.execute(sql_update_query, data)
        sqliteConnection.commit()
        print("Record Updated successfully")               
        cursor.close()
    except sqlite3.Error as error:
        print("Failed to update sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The sqlite connection is closed")
def update_datetime_order (id_order):
    try:
        sqliteConnection = sqlite3.connect(sqlfile)
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")
        sql_update_query = """Update การขาย set วันเวลาที่สั่ง  = ? where รหัสการขาย = ?"""

        
        data = (datetime.datetime.now(),id_order)
        cursor.execute(sql_update_query, data)
        sqliteConnection.commit()
        print("Record Updated successfully")               
        cursor.close()
    except sqlite3.Error as error:
        print("Failed to update sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The sqlite connection is closed")

def update_slip_payment (id_order,bank,photo_payment):
    try:
        sqliteConnection = sqlite3.connect(sqlfile)
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")
        sql_update_query = """Update การชำระ set ชื่อธนาคาร  = ?,วันเวลาที่ชำระ = ? ,หลักฐานการชำระ = ?,ยอดชำระ = ? where รหัสการขาย = ?"""
        photo_payment = convertToBinaryData(photo_payment)
        time_pay = datetime.datetime.now()
        total_price = getdb.get_totalprice(id_order)

        data = (bank,time_pay,photo_payment,total_price,id_order)
        cursor.execute(sql_update_query, data)
        sqliteConnection.commit()
        print("Record Updated successfully")               
        cursor.close()
    except sqlite3.Error as error:
        print("Failed to update sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The sqlite connection is closed")        


# update_plus_value_product('P00001',1)        
# update_datetime_order('S00001')