limite = int(input("Ingrese el límite:"))
suma=0
for i in range(limite):
    number=int(input("Ingrese un número :"))
    suma+=i
promedio=suma/limite
print("La suma es ",suma)
print("El promedio es ",promedio)
