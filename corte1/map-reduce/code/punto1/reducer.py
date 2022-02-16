import sys

arreglo = []

for line in sys.stdin:
	la = line.split()
	arreglo.append(la)

auxArr=[]

for i in arreglo:
	auxArr += i

for i in range(len(auxArr)):
	contador = 1
	for j in range(i+1, len(auxArr)):
		if (auxArr[i]==auxArr[j]):
			contador = contador +1
	print(auxArr[i], "/", contador)
