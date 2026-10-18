#Solución: Adivina el número:frio o caliente
#Autor: Adrián Herra Vargas
import random

# Entradas
numero_secreto = random.randint(1, 20)
contador = 0

# Proceso
while True:
    contador += 1
    intento = int(input("Intento: "))
    comparacion = abs(numero_secreto - intento)

    if comparacion == 0:
        pista = 'Acertó. Termina el juego.'
    elif comparacion == 1 or comparacion == 2:
        pista = 'Hirviendo: estás casi encima del número.'
    elif 3 <= comparacion <= 5:
        pista = 'Caliente: estás cerca.'
    elif 6 <= comparacion <= 10:
        pista = 'Tibio: vas por buen camino, pero falta.'
    else:
        pista = 'Frío: estás lejos.'

    if intento > numero_secreto:
        resultado = f"El número secreto es menor. {pista}"
    elif intento < numero_secreto:
        resultado = f"El número secreto es mayor. {pista}"
    else:
        resultado = f"Correcto. Adivinó en {contador} intentos."
        print(resultado)
        break

    print(resultado)