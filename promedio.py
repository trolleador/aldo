a="si"
arreglo = []

while(a=="si"):
    
    arreglo.append(float(input("dame un número\n")))
    a=input("quieres promediar otras cantidades? \n")

cantidad=(len(arreglo))
suma=0

for i in arreglo:
    suma = suma + i
print(suma/cantidad)