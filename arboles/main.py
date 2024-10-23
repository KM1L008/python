class Nodo:
    def __init__(self, nombre, tipo="directorio"):
        self.nombre = nombre
        self.tipo = tipo  # Puede ser "directorio" o "archivo"
        self.left = None
        self.right = None

class ArbolBinario:
    def __init__(self):
        self.raiz = Nodo("main")  # El directorio principal es "main"
        self.cursor = self.raiz   # El cursor comienza en la raíz

    def mover_cursor(self, nombre_directorio):
        """ Mueve el cursor al subdirectorio si existe """
        if self.cursor.left and self.cursor.left.nombre == nombre_directorio:
            self.cursor = self.cursor.left
        elif self.cursor.right and self.cursor.right.nombre == nombre_directorio:
            self.cursor = self.cursor.right
        else:
            print(f"Directorio '{nombre_directorio}' no encontrado.")

    def retroceder_cursor(self):
        """ Vuelve el cursor a la raíz (main) """
        self.cursor = self.raiz

    def agregar_nodo(self, nombre, tipo="directorio"):
        """ Agrega un nodo (directorio o archivo) al árbol """
        nuevo_nodo = Nodo(nombre, tipo)

        if self.cursor.left is None:
            self.cursor.left = nuevo_nodo
        elif self.cursor.right is None:
            self.cursor.right = nuevo_nodo
        else:
            print(f"No se puede agregar más de dos elementos en '{self.cursor.nombre}'.")

    def mostrar_directorio(self, nodo=None, nivel=0):
        """ Muestra la estructura del directorio (árbol) """
        if nodo is None:
            nodo = self.raiz

        print("  " * nivel + f"- {nodo.nombre} ({nodo.tipo})")

        if nodo.left:
            self.mostrar_directorio(nodo.left, nivel + 1)
        if nodo.right:
            self.mostrar_directorio(nodo.right, nivel + 1)

# Ejemplo de uso
if __name__ == "__main__":
    arbol = ArbolBinario()

    # Agregamos dos directorios a 'main'
    arbol.agregar_nodo("Documentos", "directorio")
    arbol.agregar_nodo("Videos", "directorio")

    # Movemos el cursor a 'Documentos' y agregamos archivos
    arbol.mover_cursor("Documentos")
    arbol.agregar_nodo("archivo1.txt", "archivo")
    arbol.agregar_nodo("archivo2.txt", "archivo")

    # Volvemos al directorio 'main'
    arbol.retroceder_cursor()

    # Movemos el cursor a 'Videos' y agregamos un archivo
    arbol.mover_cursor("Videos")
    arbol.agregar_nodo("video1.mp4", "archivo")

    # Mostramos la estructura del directorio
    arbol.mostrar_directorio()
