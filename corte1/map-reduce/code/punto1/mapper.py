import sys

for line in sys.stdin:
	linea = line.split()
	for i in range (len(linea)):
		print(linea[i],1)
