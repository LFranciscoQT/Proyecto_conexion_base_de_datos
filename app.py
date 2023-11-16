from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    try:
        #Conexion de base de datos SQLiet
        conexion = sqlite3.connect("database/mibdd")
        cursor = conexion.cursor()
        
        #Conexion para obtener los datos de la tabla
        cursor.execute("SELECT * FROM factura")
        data = cursor.fetchall()
        
        #Cerrar la conexion
        conexion.close()
        
        return render_template('index.html', data=data)
    
    except Exception as ex:
        return str(ex)
if __name__ == '__main__':
    app.run(debug=True)