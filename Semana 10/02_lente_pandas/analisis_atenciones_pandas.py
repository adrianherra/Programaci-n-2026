"""El mismo expediente, con Pandas y las mismas tres funciones."""

import pandas as pd
from pathlib import Path


ARCHIVO_CSV = Path(__file__).with_name("atenciones.csv")


def explorar_atenciones(atenciones):
    print('Atenciones: ', len(atenciones))
    print('Atenciones tipo: ', type(atenciones))
    print('Campos: ', list(atenciones.columns))


def contar_categorias(atenciones):
    print("Medicamentos", atenciones['medicamento'].value_counts().to_dict())
    print("Hostitales", atenciones['hospital'].value_counts())
    print("Diagnosticos", atenciones['diagnostico'].value_counts())  

def concluir(atenciones):
    print("Pacientes:", atenciones["cedula"].nunique())
    print("Minutos espera:", atenciones["minutos_espera"].sum())
    print("Minutos espera Promedio:", atenciones["minutos_espera"].mean())
    print("Minutos espera Moda:", atenciones["minutos_espera"].mode())
    print("Minutos espera Media:", atenciones["minutos_espera"].median())

try:
    #antenciones = pd.read_csv(ARCHIVO_CSV, encoding='utf-8', sep=',')
    atenciones = pd.read_csv(ARCHIVO_CSV)
    
except FileNotFoundError:
    print(f"No encontramos el archivo: {ARCHIVO_CSV}")
    raise SystemExit(1)

if not atenciones.empty:
    explorar_atenciones(atenciones)
    contar_categorias(atenciones)
    concluir(atenciones)
else:
    print("El archivo no contiene atenciones.")
