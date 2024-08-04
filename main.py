from dominio.dominio import Planeta
from servicio.planetaService import PlanetaService

def main():
    planeta_service = PlanetaService()

    while True:
        print("""
               --- MENU ---
               1. Crear planeta
               2. Consultar planetas
               3. Actualizar planeta
               4. Eliminar planeta
               5. Salir
        """)

        opcion = int(input("Seleccione una opción: "))
        if opcion == 1:
            nombre = input("Ingrese el nombre del planeta: ")
            tipo = input("Ingrese el tipo de planeta (Rocoso, Gaseoso, etc.): ")
            radio = float(input("Ingrese el radio del planeta: "))
            distancia_Sol = float(input("Ingrese la distancia al sol del planeta: "))
            instancia_planeta = Planeta(None, nombre, tipo, radio, distancia_Sol)
            planeta_service.crear(instancia_planeta)
        elif opcion == 2:
            nombre = input("Ingrese el nombre del planeta que desea consultar: ")
            planetas = planeta_service.leer(nombre if nombre.strip() else None)
            for planeta in planetas:
                print(vars(planeta))
        elif opcion == 3:
            id = int(input("Ingrese el id del planeta que desea actualizar: "))
            nombre = input("Ingrese el nuevo nombre del planeta: ")
            tipo = input("Ingrese el nuevo tipo de planeta (Rocoso, Gaseoso, etc.): ")
            radio = float(input("Ingrese el nuevo radio del planeta: "))
            distancia_Sol = float(input("Ingrese la nueva distancia al sol del planeta: "))
            instancia_planeta = Planeta(id, nombre, tipo, radio, distancia_Sol)
            planeta_service.actualizar(id, instancia_planeta)
        elif opcion == 4:
            id = int(input("Ingrese el id del planeta que desea eliminar: "))
            planeta_service.borrar(id)
        elif opcion == 5:
            print("Bye")
            break

if __name__ == "__main__":
    main()
    