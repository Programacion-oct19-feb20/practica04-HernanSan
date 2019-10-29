"""
	@autor: HernanSan
	Nombre: ejercicio6.py
	descripcion:...

	Hernan Sanchez -- 18
	Su suma de notas es: 30
	Su promedio es: 15


"""
#System.outprintln("Ingrese su nombre")
#nombre = entrada.nextLine()

nombre = input("Ingrese su nombre: ")
edad = input("Ingrese su edad: \n")
nota1 = input("Ingrese el valor de su nota1: ")
nota2 = input("Ingrese el valor de su nota1: ")

suma = int(nota1) + int(nota2);
promedio = int(suma)/2 

print("%s -- %s\nSu suma de notas es %s\n Su promedio es %s" % (nombre, edad, suma, promedio))
