# Autor: Adrián Herra Vargas
# Programa Detector de número par/impar

#Entradas
try:
    numero = int(input("Ingrese el número: "))
    if numero < 1:
        print(f"\tError el número ingresado no es valido {numero}, ingrese un número mayor que 0")
except ValueError:
    print(f"\nFormato de número invalido, favor ingrese un número entero valido")
    numero = -1
    
#Procesos
  
if numero < 1:
    resultado = "\tNo fue posible realizar la detección, intente de nuevo"
else:
    formato = numero % 2 == 0
    if formato:
        resultado = f"El número {numero} es par"
    else:
        resultado = f"El número {numero} es par"

#Salida  
print("-" * 70, '\n')
print(resultado)
