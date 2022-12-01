#problema 26

print ("***********************************")
print ("*********VENTA DE MANZANAS*********")
print ("***********************************")
print ("**Opcion    kilos      %Descuento**")
print ("**  1         0-2           0%   **")
print ("**  2       2.01-5         10%   **")
print ("**  3       5.01-10        20%   **")
print ("**  4      mayor a 10      30%   **")
print ("***********************************")


#Variables

PN=0
PD=0


#Entrada

Kilos:str=str(input("Ingrese la opcion: "))
kilo=float(input("ingrese el kilo: "))


#Proceso

match Kilos:
    case "1":
        PN = 1.7 * kilo
        PD = ((10*PN)/100)

        #Salida

        print ("El precio normal es: ", PN)
        print ("No tiene descuento")
    case "2":
        PN = 1.7 * kilo
        PD = ((10*PN)/100)
        
        #Salida

        print ("El precio normal es: ", PN)
        print ("El descuento es: ", PD) 
    case "3":
        PN = 1.7 * kilo
        PD = ((20*PN)/100)

        #Salida

        print ("El precio normal es: ", PN)
        print ("El descuento es: ", PD) 
    case "4":
        PN = 1.7 * kilo
        PD = ((30*PN)/100)

        #Salida
        
        print ("El precio normal es: ", PN)
        print ("El descuento es: ", PD)