numeropares=0
numeroimpares=0
suma=0
for i in range(6):
    numero=int(input("Ingrese un número: "))
    if numero % 2 == 0 :
        numeropares+=1
    else:
        numeroimpares+=1
print("La cantidad de números pares es: ",numeropares)
print("La cantidad de números impares es: ",numeroimpares)
