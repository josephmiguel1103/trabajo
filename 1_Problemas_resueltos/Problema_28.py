#Ejercicio 28

#Variables
n1=0
n2=0
operador=()
r=0
#Entrada
operador=input("Ingrese el operador: ")
n1=int(input("Ingrese el primer valor: "))
n2=int(input("Ingrese el segundo valor: "))
#Proceso
if operador == "+":
    r = n1 + n2 
elif operador == "-":
        r = n1 - n2
elif operador == "*":
            r = n1 * n2
elif operador == "/":
    if n2 == 0:
        r = 0
    else:
        r = n1 / n2
#Salida
print (f"Resultado: {r}")
