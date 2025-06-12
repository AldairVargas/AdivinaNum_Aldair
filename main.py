import random

def adivina_num():
    while True:
        print("¡Bienvenido al juego Adivina el Número!")
        print("1. Jugar")
        print("2. Salir")
        opcion = int(input("Elige una opción: "))

        if opcion == 2:
            print("Gracias por jugar. ¡Hasta luego!")
            break
        elif opcion == 1:
            numero_secreto = random.randint(1, 100)
            contador_intentos = 0
            adivinado = False

            print("He generado un número entre 1 y 100. ¡Intenta adivinarlo!")

            while not adivinado:
                intento = int(input("Ingresa tu intento: "))
                contador_intentos += 1

                if intento < numero_secreto:
                    print("El número es mayor. Intenta de nuevo.")
                elif intento > numero_secreto:
                    print("El número es menor. Intenta de nuevo.")
                else:
                    adivinado = True
                    print(f"¡Felicidades! Has adivinado el número en {contador_intentos} intentos.")
        else:
            print("Opción no válida. Por favor, elige 1 o 2.")

adivina_num()

#confirmacion con jira