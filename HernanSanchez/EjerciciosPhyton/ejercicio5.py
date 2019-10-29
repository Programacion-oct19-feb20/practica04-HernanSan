"""
	@autor: HernanSan
	Nombre: ejercicio5.py
	descripcion:...
"""
#System.outprintln("Ingrese su nombre")
#nombre = entrada.nextLine()

nombre = input("Ingrese su nombre: ")
edad = input("Ingrese su edad: \n")
nota1 = input("Ingrese el valor de su nota1: ")
nota2 = input("Ingrese el valor de su nota1: ")

suma = int(nota1) + int(nota2);

print("%s -- %s\nSu suma de notas es %s" % (nombre, edad, suma))