#!/usr/bin/python
# -*- coding: latin-1 -*-
from VALID import ns, OKI

def encript(k,M):
	texto_cifrado = [""]*k
	for column in range(k):
		currentIndex = column
		while currentIndex < len(M):
			texto_cifrado[column] += M[currentIndex]
			
			currentIndex += k
	result = ("".join(texto_cifrado))
	return(result)

while True:
	myMessage = input("Texto: ")
	myKey = OKI(input("Clave: "))
	texto_cifrado = (encript(myKey,myMessage))
	print("Texto cifrado: ",texto_cifrado)
	
	conti = ns(input("¿Continuar(n/s)?: "))
	
	if conti == "n":
		break
