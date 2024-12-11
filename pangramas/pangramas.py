''' 
Un pangrama es una frase que contiene todas las letras del alfabeto al menos una vez.

Crea una función llamada pangramas que reciba un string y devuelva "Es Pangrama" si 
es un pangrama o "No es pangrama" si no lo es.

Puntos a considerar:

- En español, el alfabeto tiene 27 letras, incluyendo la ñ.

- La función debe ignorar espacios, acentos y no debe importar si los caracteres ingresados
  son mayúsculas o minúsculas.
  
- Para que los tests pasen, la función debe devolver el string exactamente como se indica.
  Ya sea 'Es Pangrama' o 'No es pangrama'.

Ejemplos:
Entrada: 'El jefe vikingo Wamba hizo conquistar Guadix y España'
Salida: Es Pangrama

Entrada: 'hola'
Salida: No es pangrama

'''


"""
Nombre: Patricio Salvador González Castillo No.Cuenta: 321142391
Funcion pangramas. Recibe una cadena (s) y devuelve "Es Pangrama" si lo es, y "No es pangrama" en caso contrario.
Version 2.0
Utiliza un diccionario de las vocales acentuadas para poder distinguirlas. Utilizamos un ciclo for para rellenar un set pangrama, si la longitud es mayor a 27 entonces es un pangrama.
"""
def pangramas(s):    
    acentos = {'á':'a',
               'é':'e',
               'í':'i',
               'ó':'o',
               'ú':'u'}
    # Declaramos un set vacío para ingresar los valores válidos de la cadena s
    pangrama = set()

    # Iteramos sobre cada caractér y lo agregamos solo si es una letra minúscula, 
    # en caso de ser una letrra acentuada entonces regresamos su valor en el diccionario
    for letra in s:
        if letra.isalpha() and (not letra in acentos):
            pangrama.add(letra)

    if len(pangrama) < 27:
        return "No es pangrama"
    else:
        return "Es Pangrama"
