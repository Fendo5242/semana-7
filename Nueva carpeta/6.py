pares=0
impares=0
positivos=0
negativos=0
neutros=0
limite=5
for i in range (limite):
    number=int(input("Ingrese un número: "))
    if number % 2 == 0:
       pares += 1
    else:
       impares +=1
    if i<0:
       negativos +=1
    else:
       positivos +=1
    if number == 0:
        neutros +=1
print("La cantidad de números pares es ",pares)
print("La cantidad de números impares es ",impares)
print("La cantidad de números positivos es ",positivos)
print("La cantidad de números negativos es ",negativos)
print("La cantidad de números neutros es ",neutros)


