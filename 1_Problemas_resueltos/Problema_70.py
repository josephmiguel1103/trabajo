
# entrada
num = int(input("ingrese un valor numerico "))
div = int(input("ingrese un divisor "))

# proceso y salida
for i in range(num-1, 0, -1):
    if i % div == 0:
        print(f"\n el multiplo anterior es {i}")
        break
