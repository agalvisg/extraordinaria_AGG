

class Carro():
    
    def __init__(self, nombre="", vel_max=float, aceleracion=float, posicion=float(0), velocidad=float(0)):
        self.nombre = nombre
        self.vel_max = vel_max
        self.aceleracion = aceleracion
        self.posicion = posicion
        self.velocidad = velocidad
    
    def mover(self, tiempo):
        # Calcula la nueva velocidad del coche
        nueva_velocidad = self.velocidad + self.aceleracion * tiempo
        
        # Verifica si la nueva velocidad supera la velocidad máxima
        if nueva_velocidad > self.vel_max:
            nueva_velocidad = self.vel_max
        
        # Calcula la distancia recorrida durante el tiempo transcurrido
        distancia_recorrida = (self.velocidad + nueva_velocidad) / 2 * tiempo
        
        # Actualiza la posición del coche
        self.posicion += distancia_recorrida
        
        # Actualiza la velocidad del coche
        self.velocidad = nueva_velocidad

class Carrera(Carro): 
    def __init__(self):
        self.carros=[]

    def agregar_carro(self, carro):
        self.carros.append(carro)


    def iniciar_carrera(self, duracion, intervalo):
        tiempo_total = 0
        while tiempo_total < duracion:
            for carro in self.carros:
                Carro.mover(carro,intervalo)
                self.mostrar_posiciones()
                tiempo_total += intervalo
                self.mostrar_resultados_finales()

    def mostrar_posiciones(self):
        carro = Carro
        for carro in self.carros:
            print(f"El carro {Carro.nombre} se encuentra en la posición {Carro.posicion}")
    
    def mostrar_resultados_finales(self):
        print("\nResultados finales:")
        for carro in self.carros:
            print(f"El carro {Carro.nombre} se encuentra en la posición {Carro.posicion:.2f}")

