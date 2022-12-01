#Problema 31
factorial = int (1)
numero = int(input(">Ingrese un numero: "))

while(numero != 0 ):
    factorial = factorial * numero 
    numero = numero - 1

print("El factorial del numero es: "+str (factorial))