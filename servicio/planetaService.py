from abc import ABC, abstractmethod
from accessData.conexion import Conexion
from dominio.dominio import Planeta
from servicio.logService import LogService

class BaseDatos(ABC):
    @abstractmethod
    def crear(self, datos):
        pass

    @abstractmethod
    def leer(self, nombre):
        pass

    @abstractmethod
    def actualizar(self, id, datos):
        pass

    @abstractmethod
    def borrar(self, id):
        pass


class PlanetaService(BaseDatos):
    def __init__(self):
        self.connection = None
        self.cursor = None
        self.registro = LogService()

    def crear(self, datos):
        self.registro.logger(f"Creando el planeta: {datos.nombre}")
        self.connection = Conexion.obtener_conexion()
        self.cursor = self.connection.cursor()
        
        try:
            sql = "INSERT INTO planeta (nombre, tipo, radio, distancia_sol) VALUES (%s, %s, %s, %s)"
            valores = (datos.nombre, datos.tipo, datos.radio, datos.distanciaSol)
            self.cursor.execute(sql, valores)
            self.connection.commit()
            print("Planeta creado exitosamente.")
        except Exception as error:
            print("Error al insertar:", error)
            self.connection.rollback()
        finally:
            self.cursor.close()
            self.connection.close()

    def leer(self, nombre=None):
        self.registro.logger("Se ingresó al método leer")

        self.connection = Conexion.obtener_conexion()
        self.cursor = self.connection.cursor()

        try:
            sql = "SELECT * FROM planeta"
            self.cursor.execute(sql)

            lista = []

            for (id, nombre, tipo, radio, distanciaSol) in self.cursor:
                lista.append(Planeta(id, nombre, tipo, radio, distanciaSol))

            return lista

        except Exception as err:
            print("Error en la ejecución de la consulta:", err)
            self.connection.rollback()

        finally:
            self.cursor.close()
            self.connection.close()

    def actualizar(self, id, datos):
        self.registro.logger(f"Actualizando el planeta: {datos.nombre}")
        self.connection = Conexion.obtener_conexion()
        self.cursor = self.connection.cursor()

        try:
            sql = "UPDATE planeta SET nombre=%s, tipo=%s, radio=%s, distancia_sol=%s WHERE id=%s"
            valores = (datos.nombre, datos.tipo, datos.radio, datos.distanciaSol, id)
            self.cursor.execute(sql, valores)
            self.connection.commit()
            print("Planeta actualizado exitosamente.")
        except Exception as err:
            print("Error al actualizar:", err)
            self.connection.rollback()
        finally:
            self.cursor.close()
            self.connection.close()

    def borrar(self, id):
        self.registro.logger(f"Eliminando el planeta con id: {id}")
        self.connection = Conexion.obtener_conexion()
        self.cursor = self.connection.cursor()

        try:
            sql = "DELETE FROM planeta WHERE id=%s"
            self.cursor.execute(sql, (id,))
            self.connection.commit()
            print("Planeta eliminado exitosamente.")
        except Exception as err:
            print("Error al eliminar:", err)
            self.connection.rollback()
        finally:
            self.cursor.close()
            self.connection.close()