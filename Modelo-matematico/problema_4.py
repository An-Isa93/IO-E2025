from scipy.optimize import linprog
import numpy as np

# Definir tiempos individuales
times = {
    "Amy": 1,
    "Jim": 2,
    "John": 5,
    "Kelly": 10
}

# Índices para las personas
persons = list(times.keys())
n = len(persons)

# Crear las combinaciones de cruces
pairs = [(i, j) for i in range(n) for j in range(i + 1, n)]

# Cantidad de variables (cruces ida y posibles regresos)
num_vars = len(pairs) + n

# 1. Función objetivo: minimizar el tiempo total
c = []

# Tiempos para los cruces de ida (parejas)
for i, j in pairs:
    c.append(max(times[persons[i]], times[persons[j]]))

# Tiempos para los regresos (personas individuales)
for i in range(n):
    c.append(times[persons[i]])

# Convertir a array para scipy
c = np.array(c)

# 2. Restricciones
# 2.1 Cada persona debe cruzar exactamente una vez en los cruces de ida
A_eq = np.zeros((n, num_vars))
b_eq = np.ones(n)

# Agregar coeficientes para las combinaciones de ida
for k, (i, j) in enumerate(pairs):
    A_eq[i][k] = 1  # La persona i participa en el cruce k
    A_eq[j][k] = 1  # La persona j participa en el cruce k

# 2.2 Una sola persona puede regresar después de cada cruce
A_ub = np.zeros((len(pairs), num_vars))
b_ub = np.ones(len(pairs))

# Agregar coeficientes para los regresos
for k, (i, j) in enumerate(pairs):
    A_ub[k][k] = -1
    A_ub[k][len(pairs) + i] = 1
    A_ub[k][len(pairs) + j] = 1

# 3. Variables de decisión (binarias, pero se relajan para linprog)
bounds = [(0, 1)] * num_vars

# Resolver el problema con linprog
result = linprog(c, A_eq=A_eq, b_eq=b_eq, A_ub=A_ub, b_ub=b_ub, bounds=bounds, method="highs")

# Mostrar resultados
if result.success:
    print("Tiempo mínimo total:", result.fun)
    print("Variables de decisión:")
    for k, (i, j) in enumerate(pairs):
        print(f"Ida: {persons[i]} y {persons[j]} - {result.x[k]:.2f}")
    for i in range(n):
        print(f"Regreso: {persons[i]} - {result.x[len(pairs) + i]:.2f}")
else:
    print("No se pudo encontrar una solución.")
