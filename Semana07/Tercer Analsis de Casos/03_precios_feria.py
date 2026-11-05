#Nombre del estudiante: Adrián Herra Vargas
#Fecha: 06/11/2026

"""Caso 3: comparación de precios de un producto en cinco ferias."""

producto = "Tomate"
precios = [900, 850, 1000, 950, 1200]

# TODO: Calcule promedio, mínimo, máximo y rango (máximo - mínimo).
total = 0
for precio in precios:
    total += precio
    
promedio = total / len(precios)
minimo = min(precios)
maximo = max(precios)
rango = maximo - minimo
    
# TODO: Recorra precios con while y un índice para contar los que SUPERAN
#       el promedio. Aumente el índice en cada vuelta para terminar el ciclo.
contador = 0
indice = 0
while indice < len(precios):
    if precios[indice] > promedio:
        contador += 1
    indice += 1 

# TODO: Clasifique el rango: >=300 variación alta; >=150 moderada; si no, baja.
if rango >= 300:
    variacion = "variación alta"
elif rango >= 150:
    variacion = "variación moderada"
else:
    variacion = "variación baja"

# TODO: Muestre producto y todos los resultados.
# Con los datos base: promedio ₡980, mínimo ₡850, máximo ₡1200,
# rango ₡350, 2 precios sobre el promedio, variación alta.
# Prueba de código: use temporalmente cinco precios iguales y compruebe que
# el rango sea cero y ninguno supere el promedio. Restaure la lista.

print("Reporte de Comparativo de precios de productos")
print("-"*80,"\n")

print(f"Producto: {producto}")
print(f"Precio promedio: ₡{promedio:.0f}")
print(f"Precio mínimo: ₡{minimo}")
print(f"Precio máximo: ₡{maximo}")
print(f"Rango: ₡{rango}")
print(f"Precios que superan el promedio: {contador}")
print(f"Clasificación: {variacion}")
