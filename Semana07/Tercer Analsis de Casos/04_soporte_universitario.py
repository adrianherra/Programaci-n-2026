#Nombre del estudiante: Adrián Herra Vargas
#Fecha: 06/11/2026

"""Caso 4: analice los registros de soporte sin crear funciones propias."""

from incidencias import incidencias

# Cada incidencia es un diccionario: id, provincia, categoria,
# minutos_atencion y resuelto (True o False).
 
# TODO: Prepare un acumulador de minutos, un diccionario para contar
#       "Acceso", "Equipo" y "Red", un contador de casos pendientes,
#       un set de provincias con pendientes, una lista de tuplas de casos
#       urgentes y una tupla para el caso con más minutos de atención.
acumulador_minutos = 0
contador_categorias = {"Acceso": 0, "Equipo": 0, "Red": 0}
contador_pendientes = 0 
provincias_pendientes = set()
casos_urgentes = []
caso_largo = ("", 0)

# TODO: Recorra incidencias una sola vez. Actualice los acumuladores y el
#       conteo de la categoría de cada registro.
# TODO: Si un caso NO está resuelto, cuéntelo y agregue su provincia al set.
#       Si, además, tiene 60 minutos o más, agregue (id, minutos) a la lista
#       de casos urgentes. Actualice la tupla del caso más largo si corresponde.

for incidencia in incidencias:
    acumulador_minutos += incidencia["minutos_atencion"]
    contador_categorias[incidencia["categoria"]] += 1

    if not incidencia["resuelto"]:
        contador_pendientes += 1
        provincias_pendientes.add(incidencia["provincia"])

        if incidencia["minutos_atencion"] >= 60:
            casos_urgentes.append((incidencia["id"], incidencia["minutos_atencion"]))

    if incidencia["minutos_atencion"] > caso_largo[1]:
        caso_largo = (incidencia["id"], incidencia["minutos_atencion"])
        
        
# TODO: Muestre total y promedio de minutos, conteo por categoría, cantidad
#       de pendientes, provincias con pendientes, casos urgentes y caso más
#       largo. Compruebe también si "San Jose" pertenece al set.
# Control: 10 casos; 500 minutos; promedio 50; Acceso 4, Equipo 3, Red 3;
# 4 pendientes en 4 provincias; urgentes INC-02, INC-05 e INC-07;
# más largo INC-07 con 95 minutos; hay pendientes en San Jose.
# Prueba: cambie temporalmente INC-07 a resuelto=True. Debe salir de la
# lista de urgentes, del conteo de pendientes y del set de provincias
# pendientes, pero seguir como caso más largo. Restaure incidencias.py.

promedio = acumulador_minutos / len(incidencias)

print("Reporte de análisis de casos")
print("-"*80,"\n")

print(f"Total de casos: {len(incidencias)}")
print(f"Total de minutos: {acumulador_minutos}")
print(f"Promedio de minutos: {promedio:.0f}")
print(f"Conteo por categoría: {contador_categorias}")
print(f"Casos pendientes: {contador_pendientes}")
print(f"Provincias con pendientes: {provincias_pendientes}")
print(f"Casos urgentes: {casos_urgentes}")
print(f"Caso más largo: {caso_largo[0]} con {caso_largo[1]} minutos")
print(f"¿Hay pendientes en San Jose? {'San Jose' in provincias_pendientes}")