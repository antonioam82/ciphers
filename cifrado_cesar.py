#!/usr/bin/env python
# -*- coding: utf-8 -*#REVERSE CIPHER
from VALID import ns, enum, OKI

ops = ["encriptar","desencriptar"]
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!?.'

while True:
	mode = enum(ops)
	message = input("Tu texto: ")
	key = OKI(input("Introduce número clave: "))
	translated = ""
	for symbol in message:
		if symbol in SYMBOLS:
			S_INDEX = SYMBOLS.find(symbol)
			
			if mode == 'encriptar':
				T_INDEX = S_INDEX + key
			elif mode == 'desencriptar':
				T_INDEX = S_INDEX - key
				
			if T_INDEX >= len(SYMBOLS):
				T_INDEX = T_INDEX - len(SYMBOLS)
			elif T_INDEX < 0:
				T_INDEX = T_INDEX + len(SYMBOLS)
				
			translated = translated + SYMBOLS[T_INDEX%(len(SYMBOLS))]
		else:
			translated = translated + symbol
	print(translated)
	
	conti = ns(input("Continuar(n/s)?: "))
	
	if conti == "n":
		break
	
