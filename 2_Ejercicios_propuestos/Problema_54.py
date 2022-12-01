
#ingreso de datos 
lista=[]
for i in range (5):    
    a=input(f"ingrese {i+1} digito ")
    lista.append(a)

lista=[int(x) for x in lista]
print (f"lista normal\n{lista}")

#proceso 
opcion=str(input("ingrese el orden a(ascendente) d(descendente): "))

match (opcion):
    case "a":
        for i in range (1,len(lista)):
            insert_lista= int(lista[i])
            j=i-1
            while j>= 0 and int(lista[j]) > insert_lista:
                lista[j+1] = int(lista[j])
                j-=1
            lista[j+1]=insert_lista
        print(lista)        
    case "d":
        for i in range (1,len(lista)):
            insert_lista= int(lista[i])
            j=i-1
            while j>= 0 and int(lista[j]) < insert_lista:
                lista[j+1] = int(lista[j])
                j-=1
            lista[j+1]=insert_lista
        print (lista)
