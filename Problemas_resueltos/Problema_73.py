
#define valores 
acum: int = 0
n = ["", "", "", "", "", ""]

divisor = int(input("ingrese un divisor: "))
for i in range(5):
    #ingresa datos a la lista
    a = int(input(f" {i+1}° numero: "))
    n[i] = a
    #proceso
    if n[i] % divisor == 0:
        acum += 1

#salida de datos 
print(f" {acum} numeros son multiplos de {divisor}")

