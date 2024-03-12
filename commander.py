import sqlite3
import random
import datetime
import insertdb 
import getdb
import updatedb
import genpk
import deldb
sqlfile = 'DBlite.db'

# insertdb.insert_order('C00001')

# insertdb.insert_orderdetail('S00009','P00001',2)
 
# updatedb.update_slip_payment('S00009','MYMO','D:\DBProject_Frist_Time\picpro\slip3.jpg')
# updatedb.update_vertify_payment('S00009')


# updatedb.update_price_of_product('P00001','958')
#updatedb.update_plus_value_product('P00001',5)
deldb.del_order('S00010')