import sqlite3

try:
    conexion=sqlite3.connect('database/mibdd')
    cursor=conexion.cursor()
    cursor.execute("CREATE TABLE factura (nombre Varchar(50),venta INTEGER)")
except Exception as ex:
    print(ex)