def descomponer_en_factores_primos(numero):
    factores_primos = []
    divisor = 2
    while divisor <= numero:
        if numero % divisor == 0:
            factores_primos.append(divisor)
            numero = numero / divisor
        else:
            divisor += 1

    return factores_primos

        
def main():
    while True:
        numero = int(input("Ingrese un número entero positivo: "))
        
        
        if numero > 0:
        
            factores_primos = descomponer_en_factores_primos(numero)
            print("Los factores primos de", numero, "son:", factores_primos)
            break

        else:
            print("El número debe ser positivo.")
            
if __name__ == "__main__":
    main()