# Autor: Adrián Herra Vargas
# Programa Clasificador de edad

#Entradas
try:
    edad = int(input("Ingrese la edad: "))
    if edad < 1:
        print(f"\tError la edad ingresada no es valida {edad}, digite del 1 a 120")
except ValueError:
    print(f"\tError formato invalido, ingrese una edad valida")
    edad = -1
    
#Procesos
  
if edad < 1:
    resultado = "\tNo fue posible clasificar la edad..!"
else:
    if edad < 18:
        resultado = f"La edad ingresada {edad} es de una persona: Menor de edad"
    elif edad >= 65:
        resultado = f"La edad ingresada {edad} es de una persona: Adulto(a) mayor"
    else:
        resultado = f"La edad ingresada {edad} es de una persona: Adulto(a)"

#Salida  
print("-" * 70, '\n')
print(resultado)

