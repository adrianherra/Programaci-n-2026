# Autor: Adrián Herra Vargas
# Programa Calculadora de Propina Inteligente

#Entradas
nombre_cliente = input("Ingrese el nombre del cliente: ").upper().strip() 
try:
    saldo_cuenta = float(input("Ingrese el monto de la cuenta: "))
    if saldo_cuenta < 1:
        print(f"\tError el saldo es incorrecto {saldo_cuenta} ")
except ValueError:
    print(f"\nMonto ingresado invalido {saldo_cuenta}, favor ingrese un cantidad valida")
    saldo_cuenta = -1
try:  
    porcentaje_propina = int(input("Ingrese el porcentaje de la propina: "))
    if porcentaje_propina < 1:
        print(f"\tPorcentaje de propina invalida {porcentaje_propina}, digite del 1 a 100")
except ValueError:
    print(f"\tMonto ingresado invalido {porcentaje_propina}, digite del 1 a 100")
    porcentaje_propina = -1    
#Procesos
  
if not nombre_cliente or saldo_cuenta < 1 or porcentaje_propina < 1:
    resultado = "\tDatos erroneos, no es posible mostrar el resultado de la propina..!"
else:
    propina = saldo_cuenta * (porcentaje_propina / 100)
    saldo_total = saldo_cuenta + propina
    resultado = f"La propina del cliente {nombre_cliente} es ¢{propina} \nEl saldo total a pagar seria de: ¢{saldo_total}"

#Salida  
print("-" * 50, '\n')
print(resultado)