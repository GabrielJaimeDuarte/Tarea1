# =========================================
# Inteligencia Artificial - Tarea práctica
# =========================================

import random

# ========================
# 1. VARIABLES DE ESTADO
# ========================
estado_robot = {
    "posicion": (0, 0),
    "bateria": 100,
    "objetivo_alcanzado": False
}

# ========================
# 2. ESPACIO DE ESTADOS
# ========================
posiciones = [(x, y) for x in range(3) for y in range(3)]
baterias = list(range(0, 101, 10))
espacio_estados = [(p, b) for p in posiciones for b in baterias]

# ========================
# 3. ESPACIO DE ACCIONES
# ========================
acciones = ["adelante", "atras", "izquierda", "derecha", "recargar"]

# ========================
# 4. FUNCIÓN DE RECOMPENSA
# ========================
def recompensa(accion, estado, pasos):
    if accion == "recargar":
        return 5
    if estado["bateria"] <= 0 and accion in ["adelante", "atras", "izquierda", "derecha"]:
        return -5
    if estado["objetivo_alcanzado"]:
        return 20 if pasos < 5 else 10
    if accion in ["adelante", "atras", "izquierda", "derecha"]:
        return -1
    return 0

# ========================
# 5. AMBIENTE
# ========================
def mover_robot(estado, accion):
    x, y = estado["posicion"]

    if estado["bateria"] <= 0 and accion != "recargar":
        return estado  # no se mueve

    if accion == "adelante":
        x = min(x + 1, 2); estado["bateria"] -= 10
    elif accion == "atras":
        x = max(x - 1, 0); estado["bateria"] -= 10
    elif accion == "derecha":
        y = min(y + 1, 2); estado["bateria"] -= 10
    elif accion == "izquierda":
        y = max(y - 1, 0); estado["bateria"] -= 10
    elif accion == "recargar":
        estado["bateria"] = 100

    if estado["bateria"] < 0:
        estado["bateria"] = 0

    estado["posicion"] = (x, y)
    if estado["posicion"] == (2, 2):
        estado["objetivo_alcanzado"] = True

    return estado

# ========================
# 6. ESTRATEGIAS
# ========================
def estrategia_aleatoria(estado):
    return random.choice(acciones)

def estrategia_conservadora(estado):
    if estado["bateria"] <= 30:
        return "recargar"
    return random.choice(["adelante", "atras", "izquierda", "derecha"])

def estrategia_dirigida(estado):
    x, y = estado["posicion"]
    if estado["bateria"] <= 20:
        return "recargar"
    if x < 2:
        return "adelante"
    if y < 2:
        return "derecha"
    return "recargar"

# ========================
# 7. SIMULACIÓN GENERAL
# ========================
def simular(estrategia, nombre):
    estado = {"posicion": (0, 0), "bateria": 100, "objetivo_alcanzado": False}
    recompensa_total = 0
    print(f"\n--- Estrategia: {nombre} ---")
    for paso in range(10):
        accion = estrategia(estado)
        estado = mover_robot(estado, accion)
        r = recompensa(accion, estado, paso + 1)
        recompensa_total += r
        print(f"Paso {paso+1}: Acción = {accion}, Estado = {estado}, Recompensa = {r}")
    print(f"Recompensa total con {nombre}: {recompensa_total}")

# ========================
# 8. PRUEBAS
# ========================
simular(estrategia_aleatoria, "Aleatoria")
simular(estrategia_conservadora, "Conservadora")
simular(estrategia_dirigida, "Dirigida")
