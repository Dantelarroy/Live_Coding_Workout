from typing import List

# Objetivo: Contar la cantidad de eventos por tipo
# INFO, WARNING, ERROR

def contar_tipos_logs(logs: List[str]):
    ''' Recibe una lista de strings y devuelve 
'''
    contador = {}

    for log in logs:
        split_log = log.split("] ")[1].split(":")[0]

        if split_log not in contador:
            contador [split_log] = 1
        else:
            contador [split_log] +=1
    
    return contador


logs = [
    "[2025-07-28 10:00:00] INFO: Usuario autenticado",
    "[2025-07-28 10:01:13] WARNING: Uso elevado de CPU",
    "[2025-07-28 10:02:45] ERROR: Timeout de conexión",
    "[2025-07-28 10:02:46] ERROR: Timeout de conexión",
    "[2025-07-28 10:02:47] INFO: Petición completada"
]

print(contar_tipos_logs(logs))

