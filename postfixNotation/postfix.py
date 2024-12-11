"""
Ejercicio 4. postfixNotation
Author: Patricio Salvador González Castillo
No. Cuenta: 32114239-1
Version 1.0.0

"""

def postfixNotation(tokens):
    '''
    Función postfixNotation. En pila_evaluación guardamos los elementos que son resultado de una operación o los proximos operandos a realizar.

    Args:

    tokens (list): La lista con la operacion en notación postfix

    Returns:

    pila_evaluacion[0] (int): El resultado final de realizar las operaciones indicadas

    '''
    pila_evaluacion = []
    
    for i in range(0, len(tokens)):
        # lstrp elimina el inicio de una cadena con '-' para verificar que los numeros negativos tambien sean agregados a la pila
        if tokens[i].lstrip('-').isdigit():
            pila_evaluacion.append(int(tokens[i]))
        else:
            operando2 = pila_evaluacion.pop()
            operando1 = pila_evaluacion.pop()

            if tokens[i] == "+":
                pila_evaluacion.append(operando1 + operando2)
            elif tokens[i] == "-":
                pila_evaluacion.append(operando1 - operando2)
            elif tokens[i] == "*":
                pila_evaluacion.append(operando1 * operando2)
            elif tokens[i]  == "/":
                pila_evaluacion.append(int(operando1 / operando2))
            else:
                result = "Invalid operator"

    return pila_evaluacion[0]


# 5 Pruebas Adicionales. La primera y segunda son las 2 iterpretaciones de 6÷2(2+1), 
# la tercera sobre operaciones anidadas, la cuarta y quinta prueban las leyes de los
# signos.

primera = ["2","1","+","2","*","6","/"]
segunda =["6","2","/","2","1","+","*"]
tercera = ["1","1","1","1","1","/","/","/","/"]
cuarta = ["5","-20","+"]
quinta = ["-300","-301","-","-1","*"]
 
if postfixNotation(primera) == 1:
    print(f"Postfix: {primera} = 1")

if postfixNotation(segunda) == 9:
    print(f"Postfix: {segunda} = 9")

if postfixNotation(tercera) == 1:
    print(f"Postfix: {tercera} = 1")

if postfixNotation(cuarta) == -15:
    print(f"Postfix: {cuarta} = -15")

if postfixNotation(quinta) == -1:
    print(f"Postfix: {quinta} = -1")




    

