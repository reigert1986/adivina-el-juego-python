#!/usr/bin/env python3


"""
	INVENTA TU JUEGO CON PYTHON
	1- JUEGO ADIVINA EL NUMERO.

	la computadora pensará un número aleatorio entre 1 y 20
		y te pedira que intentes adivinarlo


	
"""
import random
print()
def main():
	#print("@@@@ Bienvendo al juego\n\tcomo te llamas?")
	name = input()
	#print(f"\tbueno, {name} estoy pensando en un numero entre 1 y 20")
	#print(f"\tintenta adivinar")
	guessN = int(input("introduce un numero"))
	numberA = random.randint(1,20)
	print(numberA)
	print(guessN)

	
main()