from Nodo import nodo_tarea

class lista:
    def __init__(self):
        self.cabeza = None

    def mostrar(self):
        actual = self.cabeza
        while actual:
            print(actual.tarea)
            actual = actual.siguiente

    def añadir_tarea(self, txtTarea):
        tarea_nueva = tarea(txtTarea, True)
        if not self.cabeza:    
            self.cabeza = tarea_nueva
        else: 
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = tarea_nueva
    
    def seleccionar_tarea(self, pos):
        actual = self.cabeza
        cont = 0
        while actual:
            if cont == pos:
                print(f"Tarea número {pos}: \n{actual.tarea} \n\n1. Marcar como completado\n2. Modificar la tarea")
                des = int(input("-> "))
                if des == 1:
                    actual.estado = True
                    print("La tarea ha sido marcada como completada.")
                elif des == 2:
                    txtTarea = input(f"Nueva descripción de la tarea (actual: {actual.tarea}): ") or actual.tarea
                    actual.tarea = txtTarea
                    print("La tarea ha sido modificada correctamente.")
                else:
                    print("Opción no válida.")
                return
            actual = actual.siguiente
            cont += 1
        return "Tarea no encontrada"