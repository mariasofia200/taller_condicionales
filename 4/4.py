# Programa para calcular el índice de masa corporal de una persona

# input
PESO= int(input(" por favor ingrese su peso: "))
ALTURA= float(input(" por favor ingrese su altura: "))

# processing 
IMC = PESO/ALTURA**2

if IMC < 16:
    RESULTADO= "criterio de ingreso en hospital"
elif IMC <=17:
    RESULTADO= "infrapeso"
elif IMC <=18:
    RESULTADO= "bajo peso"
elif IMC <=25:
    RESULTADO= "peso normal (saludable)"
elif IMC <=30:
    RESULTADO= "sobre peso (obecidad de grado I)"
elif IMC <=30:
    RESULTADO= "sobrepeso cronico (obcidad de grado II)"
elif IMC <=35:
    RESULTADO= "obecidad premórbida (obecidad de grado III)"
elif IMC > 40:
    RESULTADO= "obecidad morbida (obecidad de grado IV)"
# output 
print("si IMC es" ,IMC," y sus resultados son",RESULTADO,)