# programa para calcular el porcentaje de ganancia de un articulo vendido

# input
precio_costo = float(input ("ingrese el valor del producto: "))
Ganancia = 0
precio_venta = precio_costo+Ganancia

# processing

if precio_costo <3000:
    Ganancia = precio_costo  *0.15
elif precio_costo > 6000:
        Ganancia = precio_costo *0.25
else:
       Ganancia = 500

precio_venta = (precio_costo + Ganancia)

# output 
print("el producto tiene precio final de",precio_venta,)