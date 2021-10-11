a=0
b=1
n = int(input("Ingrese el límite: "))
suma=0
for number in range (1,n ,1) :
    c=a+b
    a=b
    b=c
    print(b)
    suma += b
print("La suma es :", suma)
