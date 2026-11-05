#Nombre del estudiante: Adrián Herra Vargas
#Fecha: 06/11/2026

"""Caso 1: cambio del consumo diario de agua. Complete el programa."""

consumos_litros = [120, 115, 108, 102, 96]

# TODO: Calcule el consumo total y el promedio diario.
total = 0
for consumo in consumos_litros:
    total += consumo
    
promedio = total / len(consumos_litros)    

# TODO: Compare el primer día con el último: litros ahorrados y porcentaje
#       de reducción respecto al primer día.

primer_dia = consumos_litros[0]
ultimo_dia = consumos_litros[-1]

litros_ahorrados = primer_dia - ultimo_dia
porcentaje_reduccion = (litros_ahorrados / primer_dia) * 100

# TODO: Clasifique: >=15 % reducción alta; >0 % reducción moderada;
#       de lo contrario, sin reducción.

if porcentaje_reduccion >= 15:
    estado = "reducción alta"
elif porcentaje_reduccion > 0:
    estado = "reducción moderada"
else:
    estado = "sin reducción"

# TODO: Muestre los cinco resultados.
# Control: total 541 L; promedio 108,2 L; ahorro 24 L; reducción 20 %;
#          reducción alta.
# Prueba: use temporalmente cinco consumos iguales. Debe indicar 0 % y
# "Sin reducción". Restaure la lista antes de entregar.


print("Reporte de Cálculo de consumo combustible")
print("-"*80,"\n")

print(f"Consumo total: {total} L")
print(f"Promedio diario: {promedio} L")
print(f"Ahorro respecto al primer día: {litros_ahorrados} L")
print(f"Reducción: {porcentaje_reduccion:.0f}%")
print(f"Clasificación: {estado}")
