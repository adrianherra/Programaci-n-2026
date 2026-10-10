"""Microreto: el portero del café."""


nombre = input ("Como te llamas?: ").upper().strip()
energia = int(input("Cuánta energía tienes de 0 a 100?: "))
trae_cafe = input("Traes café (si/no)?:").lower().strip() == 'si'

if energia < 50 and not(trae_cafe):
    mensaje = "Descansar"
elif energia >= 50 or trae_cafe:
    mensaje = "Puede ingresar a la clase"
else:
    mensaje = "Portero confundido: revisar respuestas"
    
print(f"{nombre}: {mensaje}")

