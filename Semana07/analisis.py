from sedes import sedes

#Acceso  a lista de sedes de emprendimientos
print("Sedes registradas", len(sedes))
print("Primera sede:", sedes[0]["nombre"])
print("Ventas de Primera sede:", sedes[0]["ventas"])

#Analisis
print("\nANÁLISIS SEMANA DE EMPRENDIMIENTOS")

provincias = set()

for sede in sedes:
    total = sum(sede["ventas"])
    porcentaje = total / sede["meta"] * 100
    
    #clasificacion
    if porcentaje >= 100:
        estado = "Meta Alcanzada"
    elif porcentaje >= 80:
        estado = "Cerca de la meta"
    else:
        estado = "Requiere atencion"
                
    print(
        f"{sede['nombre']} | Total:¢{total:,.2f} | "
        f"Cumplimiento: {porcentaje:.2f}% | {estado}"   
    )
    provincias.add(sede["provincia"])
print("Set de provincias:", provincias)
