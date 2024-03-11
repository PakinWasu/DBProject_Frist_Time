import sqlite3

import insertdb 
import getdb
import updatedb
import genpk
sqlfile = 'DBlite.db'


def del_order_detail(id_order):
    try:
        sqliteConnection = sqlite3.connect(sqlfile)
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")
        sql_update_query = """DELETE from รายละเอียดการขาย where รหัสการขาย = ?"""
        cursor.execute(sql_update_query, (id_order,))
        sqliteConnection.commit()
        print("Record deleted successfully")

        cursor.close()

    except sqlite3.Error as error:
        print("Failed to delete reocord from a sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("sqlite connection is closed")
def del_payment(id_order):
    try:
        sqliteConnection = sqlite3.connect(sqlfile)
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")
        sql_update_query = """DELETE from การชำระ where รหัสการขาย = ?"""
        cursor.execute(sql_update_query, (id_order,))
        sqliteConnection.commit()
        print("Record deleted successfully")

        cursor.close()

    except sqlite3.Error as error:
        print("Failed to delete reocord from a sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("sqlite connection is closed")

def del_order(id_order):
    try:
        del_order_detail(id_order)
        del_payment(id_order)
        sqliteConnection = sqlite3.connect(sqlfile)
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")
        sql_update_query = """DELETE from การขาย where รหัสการขาย = ?"""
        cursor.execute(sql_update_query, (id_order,))
        sqliteConnection.commit()
        print("Record deleted successfully")

        cursor.close()

    except sqlite3.Error as error:
        print("Failed to delete reocord from a sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("sqlite connection is closed")

# del_order_detail('S00004')
# del_payment('S00004')
#del_order('S00004')