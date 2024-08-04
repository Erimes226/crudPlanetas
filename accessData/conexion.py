import mysql.connector 


class Conexion:

    @staticmethod
    def obtener_conexion():
        try:
            conexion = mysql.connector.connect(
                host="localhost",          
                user="root",               
                password="admin",          
                database="sistema_solar",  
                port="3307"                
            )
            print("Conexión correcta :D ")
            return conexion
        except mysql.connector.Error as error:
            print(f"Error al conectarse en la base de datos: {error}")
            return None

    
