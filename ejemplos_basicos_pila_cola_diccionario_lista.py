# Lista
numero = [1,2,3,4,5,6,7,8,9]
nombre = ["Juan", "Pedro", "Andrea", "Maria"]
mixLista = ["Juan", 2, 3.4]

#Diccionario
personas = {
    "Juan": 20,
    "Maria": 30,
    "Profesion": "Ingeniero",
    "Salario": "$5000"
}

edades = {"Juan":30,"Maria":20, "Pedro":18}

#Ejemplo de pila

pila = []

pila.append(1)
print("Pila con elementos:", pila)
sacarElemento = pila.pop()
print("Pila sin elementos:", pila)

#Ejemplo de una cola
from collections import deque
cola = deque([1,2,3,4,5])

for valor in cola:
    print("Los elementos en la cola listos para ser extraidos segun COLA \n " , valor)

elementoaSacar = cola.popleft()

for valor in cola:
    print("Elemento sacado de la cola: \n " , valor)

elementoaSacar = cola.popleft()
print(cola)