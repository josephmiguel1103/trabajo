class Problema63 :

        # Variables
        i = 0
        n1 = 0
        n2 = 0
        s1 = 0
        s2 = 0
        r = ""
        # Entrada
        print("Numero 1: ", end ="")
        n1 = int(input())
        print("Numero 2: ", end ="")
        n2 = int(input())
        # Proceso
        i = 1
        while (i <= int(n1 / 2)) :
            if (n1 % i == 0) :
                s1 += i
            i += 1
        i = 1
        while (i <= int(n2 / 2)) :
            if (n2 % i == 0) :
                s2 += i
            i += 1
        if (n1 == s2 and n2 == s1) :
            r = "SON AMIGOS"
        else :
            r = "NO SON AMIGOS"
        # Salida
        print("")
        print("Resultado: " + r)
    
