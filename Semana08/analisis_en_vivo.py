"""Semana 8: informe de atenciones hospitalarias ficticias.

Complete las fases con el docente. La lectura de datos ya está preparada.
"""

# FASE 0: CONSUMIR LA CONEXIÓN PREPARADA
# conexion_api.py se encuentra junto a este archivo.
from conexion_api import cargar_datos

registros = cargar_datos()
print("Fuente: JSON público de GitHub")
print("Atenciones recibidas:", len(registros))

# La muestra solicitada usa range(3): deben existir las posiciones 0, 1 y 2.
if len(registros) < 3:
    raise SystemExit("Se necesitan al menos 3 registros. Publique la etapa 3.")

 
# FASE 1: MOSTRAR Y CONTAR LOS MEDICAMENTOS DE TRES ATENCIONES
print("\n ANALISIS FASE #1 MUESTRA 3")
for indice in range(3):
    registro = registros[indice]
    print(f"\n\t\tDianostico del paciente")
    print(f"Cédula: {registro['paciente_cedula']}")
    print(f"Nombre: {registro['paciente_nombre']}")
    print(f"Cédula: {registro['paciente_cedula']}")
    print(f"Diagnostico: {registro['diagnostico']}")
    print(f"Medicamentos: {registro['medicamentos']} \n")
    print(type(registro['medicamentos']))
    
# FASE 2: CONTAR LOS MEDICAMENTOS DE TODAS LAS ATENCIONES
print("\n ANALISIS FASE #2 MEDICAMENTOS Y ATENCIONES")
for registro in registros:
    print(registro['paciente_nombre'])
# FASE 3: CONTAR ATENCIONES POR HOSPITAL

# FASE 4: CONTAR ATENCIONES POR ENFERMEDAD DIAGNOSTICADA

