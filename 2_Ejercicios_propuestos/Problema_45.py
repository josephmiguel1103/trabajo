
#Entrada
acum = 0 
a = int(input("igrese el intervalo inferior: "))
b = int(input("ingrese el intervalo superior: "))

print("Los capicuas encontrados son los siguientes:")
#proceso
for i in range(a, b+1):
    num_s = str(i)
    num_list = list(num_s)
    
    if num_list == num_list[::-1]:
        invers = ''.join(num_list)
        acum += 1
        print(invers)
#salida
print("Total de Capicuas:", acum)
   
