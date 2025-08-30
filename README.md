Punto 1: Modificar la función mover_robot

Se modificó la función mover_robot para que cada vez que el robot realice un movimiento su batería disminuya. Esto permite reflejar el consumo de energía en cada acción realizada dentro del ambiente simulado.

Punto 2: Restringir movimiento cuando la batería es cero

Se implementó la condición de que si la batería llega a 0, el robot no puede moverse. En este caso, únicamente puede ejecutar la acción de recargar para restablecer su nivel de energía. De esta forma, se evita que el robot se desplace sin bateria disponible.

Punto 3: Añadir más recompensas y castigos

Castigo por intentar moverse sin batería: -5 puntos.
Recompensa por recargar la batería: +5 puntos.
Recompensa por llegar al objetivo: +10 puntos.
Bonus adicional si alcanza el objetivo en menos de 5 pasos: +20 puntos.
Costo por cada movimiento normal: -1 punto.

Punto 4: Probar diferentes estrategias de movimiento

Se probaron distintas estrategias de movimiento para observar cuál permite maximizar la recompensa total:

Estrategia aleatoria: el robot elige acciones sin criterio definido.
Estrategia conservadora: el robot recarga si la batería es menor a cierto nivel, de lo contrario se mueve al azar.
Estrategia dirigida: el robot recarga si la batería es baja y, en los demás casos, toma decisiones que lo acerquen al objetivo de forma planificada.
