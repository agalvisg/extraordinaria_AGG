class Tarea:
    def __init__(self, titulo, descripcion=""):
        self.titulo = titulo
        self.descripcion = descripcion

    def __str__(self):
        return f"Título: {self.titulo}\nDescripción: {self.descripcion}\n"
class GestorDeTareas:
    def __init__(self):
        self.tareas = []

    def agregar_tarea(self, titulo, descripcion=""):
        nueva_tarea = Tarea(titulo, descripcion)
        self.tareas.append(nueva_tarea)
        print("Tarea agregada exitosamente.\n")

    def eliminar_tarea(self, titulo):
        for tarea in self.tareas:
            if tarea.titulo == titulo:
                self.tareas.remove(tarea)
                print("Tarea eliminada exitosamente.\n")
                return
        print("Tarea no encontrada.\n")

    def mostrar_tareas(self):
        if not self.tareas:
            print("No hay tareas en la lista.\n")
        else:
            for tarea in self.tareas:
                print(tarea)
    def mostrar_menu():
        print("Gestor de Tareas")
        print("1. Agregar tarea")
        print("2. Eliminar tarea")
        print("3. Mostrar tareas")
        print("4. Salir")

def main():
    gestor = GestorDeTareas()

    while True:
        GestorDeTareas.mostrar_menu()
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            titulo = input("Ingresa el título de la tarea: ")
            descripcion = input("Ingresa la descripción de la tarea (opcional): ")
            gestor.agregar_tarea(titulo, descripcion)
        elif opcion == "2":
            titulo = input("Ingresa el título de la tarea a eliminar: ")
            gestor.eliminar_tarea(titulo)
        elif opcion == "3":
            gestor.mostrar_tareas()
        elif opcion == "4":
            print("Saliendo del gestor de tareas.")
            break
        else:
            print("Opción no válida. Por favor, selecciona una opción del 1 al 4.\n")

if __name__ == "__main__":
    main()
