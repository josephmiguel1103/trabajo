"""trabajo 3"""

#inicio

print("continuar con el la siguiente hora, minuto y segundo")
h = int(input("hora:"))
m = int(input("minuto: "))
s = int(input("segundo: "))

# proceso

s = s+1
if s==60:
	s = 0
	m = m+1
	if m==60:
		m = 0
		h = h+1
		if h==60:
			h = 0

# salida

print ("hora: ",h)
print ("minuto: ",m)
print ("segundo: ",s)
print (f"son las {h}:{m}:{s} ")

