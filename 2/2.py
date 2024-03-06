# programa para saber si se le permite aceder a un prestamo bancario

# entrada
salario = int(input("cuanto es su salario : "))
Deuda = int(input("usted tiene otra deuda que no ha pagado (si o no): "))

# proceso y salida 
if salario >= 945200:
    if Deuda == "no":
        print ("su prestamo ha sido aprobado")
    else: 
        print("su prestamo ha sido denegado")
elif salario < 945200:
    print("su prestamo ha sido denegado")