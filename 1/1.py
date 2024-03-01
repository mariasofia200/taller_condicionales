#programa para calcular en que cuadrante esta un punto, de un plano cartesiano 

#entrada
X = int(input("ingrese la coordenada x: "))
Y = int(input("ingrese la coordenada y: "))

# proceso y salida
if X == 0:
    if Y == 0:
        print("la coordenada" ,(X , Y),"este en el origen")
    else:
        print("la coordenada" , (X , Y),"esta en el eje Y")
elif Y == 0:
    print("la coordenada" ,(X , Y),"esta en el eje x")
elif X > 0:
    if Y > 0:
        print("la coordenada" ,(X , Y)," esta en el cuadrante 1")
    else:
        print("la coordenada" ,(X , Y),"esta en el cuadrante 4")
elif Y < 0:
    print(" la coordenada" ,(X , Y),"esta en el cuadrante 3")
else:
    print("la coordenada" ,(X , Y),"esta ej el cuadrante 2")