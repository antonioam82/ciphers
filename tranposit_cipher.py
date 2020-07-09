#!/usr/bin/python
# -*- coding: latin-1 -*-
from VALID import ns, OKI

def encript(k,M):
	cif = [""]*k
	for column in range(k):
		currentIndex = column
		while currentIndex < len(M):
			cif[column] += M[currentIndex]
			currentIndex += k
	result = ("".join(cif))
	return(result)

while True:
	myMessage = input("Texto: ")
	myKey = OKI(input("Clave: "))
	texto_cifrado = (encript(myKey,myMessage))
	print(texto_cifrado)
	
	conti = ns(input("¿Continuar(n/s)?: "))
	
	if conti == "n":
		break
