from race import Carrera
from race import Carro
def main():
    # Crear instancias de carros
    carro1 = Carro("Carro1", 100,3.8)
    carro2 = Carro("Carro2", 120,3.85)
    carro3 = Carro("Carro3", 90,3.7)

    # Crear una instancia de la carrera
    race = Carrera()

    # Añadir los carros a la carrera
    race.agregar_carro(carro1)
    race.agregar_carro(carro2)
    race.agregar_carro(carro3)

    # Simular la carrera
    race.iniciar_carrera(800,3)

    # Mostrar los resultados finales
    race.mostrar_resultados_finales()

if __name__ == "__main__":
    main()