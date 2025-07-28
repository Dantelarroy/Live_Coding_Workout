# 🧪 Día 1 — Top K Palabras Frecuentes

## 🎯 Objetivo

Simular una tarea común en sistemas de análisis de logs o chats de usuario: encontrar las **K palabras más frecuentes** en un texto, ordenadas por:

1. **Frecuencia descendente**
2. **Orden alfabético** si hay empate

---

## 🧩 Enunciado

Implementar la función:

```python
def top_k_frequent_words(text: str, k: int) -> List[str]:
    ...

- Que reciba un texto largo y devuelva las k palabras más frecuentes, en minúsculas y sin signos de puntuación.

- Input ejemplo: 
text = """
Los modelos de lenguaje son el corazón de muchas aplicaciones de inteligencia artificial. 
Modelos como GPT o LLaMA son entrenados con grandes volúmenes de texto. 
Texto texto texto... modelos modelos modelos. GPT GPT.
"""
k = 3

- Output ejemplo: ['modelos', 'texto', 'gpt']
    * Ignorar mayúsculas/minúsculas (.lower())
    * Eliminar signos de puntuación (re.sub)
    * Las palabras deben estar ordenadas por frecuencia y luego alfabéticamente

 - Requisitos tecnicos:
    * Usar collections.Counter o tu propia implementación de conteo
    * Limpiar el texto con re para eliminar puntuación
    * No incluir el conteo en la respuesta final (solo las palabras)
    * Bonus: agregar parámetro opcional stopwords: Optional[List[str]] = None

- Test adicional: 
assert top_k_frequent_words("hola hola chau hola chau chau chau", 2) == ['chau', 'hola']

- 🧠 Dificultad estimada 4/10

- Duración recomendada: 25–40 minutos