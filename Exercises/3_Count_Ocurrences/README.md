# 🧪 Día 3 — Contar Ocurrencias de una Palabra

## 🎯 Objetivo

Simular una situación común donde queremos saber **cuántas veces aparece una palabra específica** dentro de un texto.

Este ejercicio refuerza:
1. Lógica básica de iteración
2. Comparación de strings
3. Conteo sin estructuras complejas

---

## 🧩 Enunciado

Implementar la función:

```python
def contar_palabra(texto: str, palabra: str) -> int:
    ...

Que reciba un texto largo (string) y una palabra objetivo (también string).

Debe devolver cuántas veces aparece esa palabra exacta, sin distinguir mayúsculas/minúsculas y sin signos de puntuación.

📥 Input de ejemplo:
texto = "Hola hola chau hola Hola, qué tal? Chau chau."
palabra = "hola"

📤 Output esperado:
4

✅ Requisitos técnicos:
- Convertir todo el texto a minúsculas (.lower())

- Eliminar signos de puntuación usando re.sub()

- Separar en palabras con .split()

- Contar solo las coincidencias exactas

🧪 Test adicional:
assert contar_palabra("Python es simple. python es poderoso. PYTHON!", "python") == 3


🧠 Dificultad estimada: 3/10

⏱ Duración recomendada: 15–25 minutos