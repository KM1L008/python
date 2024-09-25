from Funciones import lista

class Ejecutable:
    def __init__(self):
        self.tareas = lista()
        self.menu()

    def menu(self):
        print("\nBienvenido al organizador de tareas de Python.\nAquí podrás agregar tus tareas, además de destinar tareas importantes\n")
        
        while True:
            print("Mis tareas:")
            print("1. Añadir nueva tarea\n2. Escoger tarea\n3. Cerrar programa")
            des = int(input("-> "))

            if des == 1:
                tarea = input("Introduce la nueva tarea: ")
                self.tareas.añadir_tarea(tarea)
            elif des == 2:
                self.tareas.seleccionar_tarea()
            elif des == 3:
                print("Cerrando el programa...")
                break
            else:
                print("Opción no válida. Por favor, elige de nuevo.")

if __name__ == "__main__":
    Ejecutable()
