# Autor: Adrián Herra Vargas
# Programa Validador de compra con descuento

#Entradas
nombre_cliente = input("Ingrese el nombre del cliente: ").upper().strip() 
try:
    monto = float(input("Ingrese el monto de la compra: "))
    if monto < 1:
        print(f"\tError el monto {monto} debe ser mayor a 1")
except ValueError:
    print(f"\tMonto ingresado invalido, favor ingrese un cantidad valida")
    monto = -1

cliente_frecuente = input("Es cliente frecuente (si/no)?: ").lower().strip() == 'si'

#Procesos
  
if not nombre_cliente or monto < 1:
    resultado = "Registro rechazado: revise los datos ingresados!"
elif cliente_frecuente and monto > 10000 or monto >= 1000000:
    resultado = f"Descuento aprobado para {nombre_cliente}: monto de compra ¢{monto}"
else:
    resultado = f"Estimado cliente {nombre_cliente}: monto de compra ¢{monto}, no aplica descuento,\nSolo aplica para compras mayores a ¢10000 y clientes frecuentes"
    

#Salida  
print("-" * 80, '\n')
print(resultado)