##Ejercicio 3:
def parentesis_balancedos(cadena):
    pila = []
    for caracter in cadena:
        if caracter == '(':
            pila.append(caracter)
        elif caracter == ')':
            if not pila or pila.pop() != '(':
                return False
    return not pila
cadena = "(3,4,55,4,3,3)"
parentesis_balancedos("(3,4,55,4,3,3)")