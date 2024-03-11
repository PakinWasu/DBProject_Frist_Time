import sqlite3

sqlfile = 'DBlite.db'
def get_price(id_pro):
    try:
        sqliteConnection = sqlite3.connect(sqlfile)
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")
        sqlite_select_query = """SELECT ราคาต่อหน่วย 
                                FROM สินค้า 
                                WHERE รหัสสินค้า = ?;"""
        data = (id_pro)
        cursor.execute(sqlite_select_query,[data])
        record = cursor.fetchone()
        for i in record:
            price = i
        cursor.close()
        return price
    except sqlite3.Error as error:
        print("Failed to read single row from sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed") 
def get_value_pro(id_pro):
    try:
        sqliteConnection = sqlite3.connect(sqlfile)
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")
        sqlite_select_query = """SELECT สินค้าคงเหลือ 
                                FROM สินค้า 
                                WHERE รหัสสินค้า = ?;"""
        data = (id_pro)
        cursor.execute(sqlite_select_query,[data])
        record = cursor.fetchone()
        for i in record:
            value = i
        cursor.close()
        return value
    except sqlite3.Error as error:
        print("Failed to read single row from sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed")         
            
def get_totalprice(id_order):
    try:
        sqliteConnection = sqlite3.connect(sqlfile)
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")

        sqlite_select_query = """SELECT รายละเอียดการขาย.ราคาต่อหน่วย, รายละเอียดการขาย.จำนวน 
                                FROM รายละเอียดการขาย 
                                INNER JOIN การขาย 
                                ON รายละเอียดการขาย.รหัสการขาย = การขาย.รหัสการขาย
                                WHERE การขาย.รหัสการขาย = ?;"""
        data = (id_order)
        cursor.execute(sqlite_select_query,(data,))
        record = cursor.fetchall() 
        total_price = 0.0
        for i in record:
            price =i[0]
            value = i[1]
            rest_total_p = price * value
            total_price += rest_total_p
        cursor.close()
        return total_price
    except sqlite3.Error as error:
        print("Failed to read single row from sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed")  
    
def get_username(id_order):
    try:
        sqliteConnection = sqlite3.connect(sqlfile)
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")
        sqlite_select_query = """SELECT  ลูกค้า.username
                                    FROM ลูกค้า
                                    INNER JOIN การขาย
                                    ON การขาย.รหัสลูกค้า = ลูกค้า.รหัสลูกค้า WHERE การขาย.รหัสการขาย = ?;"""
        data = (id_order)
        cursor.execute(sqlite_select_query,[data])
        record = cursor.fetchone()
        for i in record:
            uname = i
        cursor.close()
        return uname
    except sqlite3.Error as error:
        print("Failed to read single row from sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed")    

def get_raw_idpro_valuepro_valueorderpro_statusorder(id_order):
    try:
        sqliteConnection = sqlite3.connect(sqlfile)
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")

        sqlite_select_query = """SELECT รายละเอียดการขาย.รหัสสินค้า,สินค้า.สินค้าคงเหลือ, รายละเอียดการขาย.จำนวน, การขาย.สถานะการขาย
                                    FROM สินค้า, การขาย, รายละเอียดการขาย
                                    INNER JOIN การชำระ
                                    ON รายละเอียดการขาย.รหัสสินค้า = สินค้า.รหัสสินค้า AND การขาย.รหัสการขาย = รายละเอียดการขาย.รหัสการขาย 
                                    AND การขาย.รหัสการขาย = การชำระ.รหัสการขาย WHERE การขาย.รหัสการขาย = ?"""
        data = (id_order)
        cursor.execute(sqlite_select_query,(data,))
        record = cursor.fetchall() 
        cursor.close()
        return record
    except sqlite3.Error as error:
        print("Failed to read single row from sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed") 
               
def get_last_row_product():
    try:
        sqliteConnection = sqlite3.connect(sqlfile)
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")
        sqlite_select_query = """SELECT รหัสสินค้า FROM สินค้า
                                    ORDER BY รหัสสินค้า DESC
                                    LIMIT 1
                                """
        cursor.execute(sqlite_select_query,)
        record = cursor.fetchone()
        for i in record:
            la = i
        cursor.close()
        return la
    except sqlite3.Error as error:
        print("Failed to read single row from sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed")  

def get_last_row_brand():
    try:
        sqliteConnection = sqlite3.connect(sqlfile)
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")
        sqlite_select_query = """SELECT รหัสยี่ห้อสินค้า FROM ยี่ห้อ
                                    ORDER BY รหัสยี่ห้อสินค้า DESC
                                    LIMIT 1
                                """
        cursor.execute(sqlite_select_query,)
        record = cursor.fetchone()
        for i in record:
            la = i
        cursor.close()
        return la
    except sqlite3.Error as error:
        print("Failed to read single row from sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed")  

def get_last_row_type():
    try:
        sqliteConnection = sqlite3.connect(sqlfile)
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")
        sqlite_select_query = """SELECT รหัสประเภทสินค้า FROM ประเภทสินค้า
                                    ORDER BY รหัสประเภทสินค้า DESC
                                    LIMIT 1
                                """
        cursor.execute(sqlite_select_query,)
        record = cursor.fetchone()
        for i in record:
            la = i
        cursor.close()
        return la
    except sqlite3.Error as error:
        print("Failed to read single row from sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed")  
        
def get_last_row_customer():
    try:
        sqliteConnection = sqlite3.connect(sqlfile)
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")
        sqlite_select_query = """SELECT รหัสลูกค้า FROM ลูกค้า
                                    ORDER BY รหัสลูกค้า DESC
                                    LIMIT 1
                                """
        cursor.execute(sqlite_select_query,)
        record = cursor.fetchone()
        for i in record:
            la = i
        cursor.close()
        return la
    except sqlite3.Error as error:
        print("Failed to read single row from sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed")  
def get_last_row_orderdetail():
    try:
        sqliteConnection = sqlite3.connect(sqlfile)
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")
        sqlite_select_query = """SELECT รหัสรายละเอียดการขาย FROM รายละเอียดการขาย
                                    ORDER BY รหัสรายละเอียดการขาย DESC
                                    LIMIT 1
                                """
        cursor.execute(sqlite_select_query,)
        record = cursor.fetchone()
        for i in record:
            la = i
        cursor.close()
        return la
    except sqlite3.Error as error:
        print("Failed to read single row from sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed")  
def get_last_row_employee():
    try:
        sqliteConnection = sqlite3.connect(sqlfile)
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")
        sqlite_select_query = """SELECT รหัสพนักงาน FROM พนักงาน
                                    ORDER BY รหัสพนักงาน DESC
                                    LIMIT 1
                                """
        cursor.execute(sqlite_select_query,)
        record = cursor.fetchone()
        for i in record:
            la = i
        cursor.close()
        return la
    except sqlite3.Error as error:
        print("Failed to read single row from sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed") 
            
def get_last_row_order():
    try:
        sqliteConnection = sqlite3.connect(sqlfile)
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")
        sqlite_select_query = """SELECT รหัสการขาย FROM การขาย
                                    ORDER BY รหัสการขาย DESC
                                    LIMIT 1
                                """
        cursor.execute(sqlite_select_query,)
        record = cursor.fetchone()
        for i in record:
            la = i
        cursor.close()
        return la
    except sqlite3.Error as error:
        print("Failed to read single row from sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed")   
            
def get_last_row_payment():
    try:
        sqliteConnection = sqlite3.connect(sqlfile)
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")
        sqlite_select_query = """SELECT รหัสการชำระ FROM การชำระ
                                    ORDER BY รหัสการชำระ DESC
                                    LIMIT 1
                                """
        cursor.execute(sqlite_select_query,)
        record = cursor.fetchone()
        for i in record:
            la = i
        cursor.close()
        return la
    except sqlite3.Error as error:
        print("Failed to read single row from sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed")  
            
def get_id_employee():
    try:
        sqliteConnection = sqlite3.connect(sqlfile)
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")

        sqlite_select_query = """SELECT รหัสพนักงาน FROM พนักงาน;"""
        cursor.execute(sqlite_select_query)
        record = cursor.fetchall() 
        emp = []
        for i in record:
            emp.append(i[0])
        cursor.close()
        
        return emp
    except sqlite3.Error as error:
        print("Failed to read single row from sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed")  
#print(get_last_row_payment())


# print(get_value_pro('P00001'))
#get_raw_idpro_valuepro_valueorderpro_statusorder('S1')

    