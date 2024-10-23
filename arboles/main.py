class Nodo:
    def __init__(self, nombre, tipo="directorio"):
        self.nombre = nombre
        self.tipo = tipo  # Puede ser "directorio" o "archivo"
        self.left = None
        self.right = None
        self.padre = None  # Para mantener referencia al nodo padre (retroceder)

class ArbolBinario:
    def __init__(self):
        self.raiz = Nodo("main")  # El directorio principal es "main"
        self.cursor = self.raiz   # El cursor comienza en la raíz
        self.ruta = "main$"       # Ruta inicial

    def mover_cursor(self, nombre_directorio):
        """ Mueve el cursor al subdirectorio si existe """
        if self.cursor.left and self.cursor.left.nombre == nombre_directorio:
            self.cursor = self.cursor.left
            self.ruta += f"/{nombre_directorio}$"  # Actualiza la ruta
        elif self.cursor.right and self.cursor.right.nombre == nombre_directorio:
            self.cursor = self.cursor.right
            self.ruta += f"/{nombre_directorio}$"  # Actualiza la ruta
        else:
            print(f"Directorio '{nombre_directorio}' no encontrado.")

    def retroceder_cursor(self):
        """ Retrocede al directorio padre """
        if self.cursor.padre:
            self.cursor = self.cursor.padre
            # Remover el último directorio de la ruta
            self.ruta = self.ruta[:self.ruta.rfind("/")] + "$"
        else:
            print("Ya estás en el directorio raíz (main).")

    def agregar_nodo(self, nombre, tipo="directorio"):
        """ Agrega un nodo (directorio o archivo) al árbol """
        nuevo_nodo = Nodo(nombre, tipo)
        nuevo_nodo.padre = self.cursor  # El nodo nuevo tiene como padre el nodo actual

        if self.cursor.left is None:
            self.cursor.left = nuevo_nodo
        elif self.cursor.right is None:
            self.cursor.right = nuevo_nodo
        else:
            print(f"No se puede agregar más de dos elementos en '{self.cursor.nombre}'.")

    def eliminar_nodo(self, nombre):
        """ Elimina un nodo (directorio o archivo) por su nombre """
        if self.cursor.left and self.cursor.left.nombre == nombre:
            self.cursor.left = None
            print(f"Nodo '{nombre}' eliminado.")
        elif self.cursor.right and self.cursor.right.nombre == nombre:
            self.cursor.right = None
            print(f"Nodo '{nombre}' eliminado.")
        else:
            print(f"Nodo '{nombre}' no encontrado en el directorio actual.")

    def contar_nodos(self, nodo):
        """ Cuenta el número de nodos en el árbol recursivamente """
        if nodo is None:
            return 0
        return 1 + self.contar_nodos(nodo.left) + self.contar_nodos(nodo.right)

    def listar_contenido(self):
        """ Lista los archivos y directorios dentro del directorio actual """
        if self.cursor.left:
            print(f"{self.cursor.left.nombre} ({self.cursor.left.tipo})")
        if self.cursor.right:
            print(f"{self.cursor.right.nombre} ({self.cursor.right.tipo})")
        if not self.cursor.left and not self.cursor.right:
            print("(Vacío)")

    def mostrar_arbol(self, nodo=None, nivel=0):
        """ Muestra el árbol de directorios de forma gráfica """
        if nodo is None:
            nodo = self.raiz
        indentacion = "    " * nivel  # Aumenta la indentación para cada nivel
        print(f"{indentacion}- {nodo.nombre} ({nodo.tipo})")
        if nodo.left:
            self.mostrar_arbol(nodo.left, nivel + 1)  # Recurre por la izquierda
        if nodo.right:
            self.mostrar_arbol(nodo.right, nivel + 1)  # Recurre por la derecha

    def buscar_y_mostrar_ruta(self, nodo, nombre_buscar, ruta_actual="main"):
        if nodo is None:
            return False  # Si llegamos a un nodo nulo, no lo encontramos
        
        nueva_ruta = f"{ruta_actual}/{nodo.nombre}"

        if nodo.nombre == nombre_buscar:
            print(f"Ruta encontrada: {nueva_ruta}")
            self.mostrar_arbol_con_ruta(self.raiz, nombre_buscar)
            return True

        # Buscar en el subárbol izquierdo y derecho
        if self.buscar_y_mostrar_ruta(nodo.left, nombre_buscar, nueva_ruta):
            return True
        
        if self.buscar_y_mostrar_ruta(nodo.right, nombre_buscar, nueva_ruta):
            return True
        
        return False  # No encontrado en este nodo ni en sus subárboles 

    def mostrar_arbol_con_ruta(self, nodo, nombre_buscar, nivel=0, es_ruta=False):
        """ Muestra el árbol resaltando la ruta del nodo encontrado """
        if nodo is None:
            return
        
        indentacion = "    " * nivel  # Aumenta la indentación para cada nivel
        
        # Determinar si el nodo actual está en la ruta
        if nodo.nombre == nombre_buscar:
            es_ruta = True
        
        if es_ruta:
            print(f"{indentacion}- [{nodo.nombre}] (ruta encontrada)")
        else:
            print(f"{indentacion}- {nodo.nombre} ({nodo.tipo})")

        # Recurre por los subárboles
        self.mostrar_arbol_con_ruta(nodo.left, nombre_buscar, nivel + 1, es_ruta)
        self.mostrar_arbol_con_ruta(nodo.right, nombre_buscar, nivel + 1, es_ruta)

# Función principal que emula una terminal de Linux
def terminal():
    arbol = ArbolBinario()
    
    while True:
        comando = input(f"{arbol.ruta} ").strip().split()

        if len(comando) == 0:
            continue  # Si no se introduce nada, continua
        
        if comando[0] == "mkdir" and len(comando) == 2:
            # Crear un directorio
            arbol.agregar_nodo(comando[1], "directorio")
        elif comando[0] == "touch" and len(comando) == 2:
            # Crear un archivo
            arbol.agregar_nodo(comando[1], "archivo")
        elif comando[0] == "cd" and len(comando) == 2:
            # Cambiar a un subdirectorio
            if comando[1] == "..":
                arbol.retroceder_cursor()
            else:
                arbol.mover_cursor(comando[1])
        elif comando[0] == "ls":
            # Listar contenido del directorio actual
            arbol.listar_contenido()
        elif comando[0] == "rm" and len(comando) == 2:
            # Eliminar un nodo
            arbol.eliminar_nodo(comando[1])
        elif comando[0] == "tree":
            # Mostrar el árbol de directorios gráficamente
            arbol.mostrar_arbol()
        elif comando[0] == "find" and len(comando) == 2:
            # Buscar un archivo o directorio y mostrar su ruta gráfica
            encontrado = arbol.buscar_y_mostrar_ruta(arbol.raiz, comando[1])
            if not encontrado:
                print(f"'{comando[1]}' no encontrado en el árbol.")
        elif comando[0] == "count":
            # Contar el número de nodos en el árbol
            total_nodos = arbol.contar_nodos(arbol.raiz)
            print(f"Número total de nodos: {total_nodos}")
        elif comando[0] == "exit":
            # Salir del programa
            print("Saliendo...")
            break
        else:
            print("Comando no reconocido.")

# Ejecutar la terminal simulada
if __name__ == "__main__":
    terminal()
