# 🧪 Día 2 — Contador de Tipos de Logs

## 🎯 Objetivo

Simular una tarea común en sistemas de monitoreo o procesamiento de logs: **contar la cantidad de eventos por tipo** (`INFO`, `WARNING`, `ERROR`).

Este ejercicio evalúa tu capacidad para:
1. Parsear strings con estructura semi-formal (como un log)
2. Aplicar condicionales y estructuras de conteo
3. Usar diccionarios de forma eficiente

---

## 🧩 Enunciado

Implementar la función:

```python
def contar_tipos_logs(logs: List[str]) -> Dict[str, int]:
    ...
Que reciba una lista de strings, cada uno representando una línea de log con formato:

ruby
Copiar
Editar
[YYYY-MM-DD HH:MM:SS] LEVEL: mensaje
Ejemplo:

python
Copiar
Editar
logs = [
    "[2025-07-28 10:00:00] INFO: Usuario autenticado",
    "[2025-07-28 10:01:13] WARNING: Uso elevado de CPU",
    "[2025-07-28 10:02:45] ERROR: Timeout de conexión",
    "[2025-07-28 10:03:00] ERROR: Timeout de conexión",
    "[2025-07-28 10:03:10] INFO: Petición completada"
]
Output esperado:

python
Copiar
Editar
{
  "INFO": 2,
  "WARNING": 1,
  "ERROR": 2
}
Requisitos técnicos:

Usar re para extraer el LEVEL de cada línea

Contar cuántas veces aparece cada tipo (INFO, WARNING, ERROR)

Devolver un dict con los totales por tipo

No importa el contenido del mensaje

Test adicional:

python
Copiar
Editar
assert contar_tipos_logs([
    "[2025-07-28 08:00:00] INFO: Inicio",
    "[2025-07-28 08:01:00] ERROR: Falla",
    "[2025-07-28 08:02:00] INFO: OK"
]) == {"INFO": 2, "ERROR": 1}
🧠 Dificultad estimada: 5/10

⏱ Duración recomendada: 20–30 minutos

Tip: pensá cómo usar re.findall() o re.search() para extraer la parte del LEVEL fácilmente