#!/usr/bin/env python3


"""
	INVENTA TU JUEGO CON PYTHON
	1- JUEGO ADIVINA EL NUMERO.

	la computadora pensará un número aleatorio entre 1 y 20
		y te pedira que intentes adivinarlo


	
"""
import random

intentosRealizados = 0

print("como te llamas?")
miNombre = input()

numero = random.randint(1,20)
print(f"bueno {miNombre} estoy pensando en un numero entre 1 y 20.")

while intentosRealizados < 6:
    print("intenta adivinar")
    estimacion = int(input())
    intentosRealizados += 1
    if estimacion < numero:
        print("tu estimacion es muy baja.")
    elif estimacion > numero:
        print("tu estimacion es muy alta")
    else:
        print("adivinaste!!!")
        break

if estimacion == numero:
    intentosRealizados = str(intentosRealizados)
    print(f"buen trabajo {miNombre}! lo hiciste en {intentosRealizados} intentos")

if estimacion != numero:
    print(f"pues no. el numero que estaba pensando era {numero}")                 

