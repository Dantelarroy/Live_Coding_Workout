'''Palabras mas frecuentes

0. Crear lista vacia
1. normalizar a minuscula todo
2. normalizar limpiando todo
3. hacer el conteo de palabras
4. ordenar alfabeticamente
5. tomar las k mas frecuentes
6. si hay empate que sea por orden alfabetico'''
import re

def top_k_frequent_words(text: str, k: int):

    frecuencia = {}

    # Normalizar minusculas
    text = text.lower()

    # Normalizar puntuacion
    text = re.sub(r"[^\w\s]","",text)

    # Normalizar espacios
    text = text.split()

    # Frecuencia de palabras 
    for palabra in text:
        if palabra in frecuencia:
          frecuencia[palabra] += 1
        else: 
           frecuencia[palabra] = 1
    
    # Convertir en tupla
    frecuencia_tupla = frecuencia.items()

    # Ordenar
    ordenadas = sorted(frecuencia_tupla, key=lambda x: (-x[1], x[0]))

    top_k = ordenadas [:k]
             
    return [palabra for palabra, _ in top_k]


palabra_top = top_k_frequent_words("""
Los modelos de lenguaje son el corazón de muchas aplicaciones de inteligencia artificial. 
Modelos como GPT o LLaMA son entrenados con grandes volúmenes de texto. 
Texto texto texto... modelos modelos modelos. GPT GPT.
""",3)
print(palabra_top)

# Dificultad percibida = 9.5
# Tiempo de trabajo 2 horas y media

# Test adicional: 
assert top_k_frequent_words("hola hola chau hola chau chau chau", 2) == ['chau', 'hola']