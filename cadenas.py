Ejercicio 6:
Escriba un programa que pregunte el nombre del usuario en consola y un numero 
entero e imprima en pantala en lineas distintas el nombre de usuario
tantas veces como el numero introducido.
 
nombre = input("¿Como te llamas? ")
n = input("introducir el número entero")
print((nombre + "\n") * int(n))

Ejercicio 7:
Escribir un programa que pregunte el nombre del usuario en consola
y despues muestre por pantalla nombre completo del usuario tres
veces, una con todas las letras minúsculas, otra con todas las letras
mayúsculas, y otra solo con la primera letra del nombre y de los apellido
en minuscula. El usuario puede introducir su nombre combinando
 mayusculas y minusculas.
nombre = input("¿Cual es tu nombre completo? ")
print(nombre.lower())
print(nombre.upper())
print(nombre.title())

Escribir un programa que pida al usuario una frase y el programa lo muestre
invertido
textoainvertir = input("Introduce la frase: ")
print(textoainvertir[::-0])


