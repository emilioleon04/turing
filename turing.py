# Simulación de una máquina de Turing para sumar 1 a un número binario

# Cinta inicial con el número binario
cinta = [0, 1, 0, 1, 0, 1, 0, 1, 1]
print("Número binario actual:", cinta)

# Definición de los estados de la máquina de Turing
estadoActual = [1, 1, 1, 1, 2, 2, 2]
lectura = [1, 0, '_', '0', 1, 0, '_']
escribeCaracter = [0, 1, 1, '0', 0, 1, 1]
estadoSiguiente = [1, 1, 3, 2, 2, 2, 3]
moverCabezal = [-1, -1, 'L', -1, -1, -1, 'L']

# Función para buscar la acción a realizar según el estado y el valor leído
def buscar(estadoA, lecturaA):
    for i in range(len(estadoActual)):
        if estadoA == estadoActual[i] and lecturaA == lectura[i]:
            print(f"Debe escribir: {escribeCaracter[i]}, Va al estado nuevo: {estadoSiguiente[i]}, Mueve el cabezal a: {moverCabezal[i]}")
            acciones = {"escribir": escribeCaracter[i], "estado": estadoSiguiente[i], "cabezal": moverCabezal[i]}
            return acciones
    return None

# Inicialización del cabezal y estado
cabezal = len(cinta) - 1
estado = 1

# Ejecución de la máquina de Turing
while True:
    if cabezal > -1:
        print(f"Estado actual: {estado}, Valor en cinta: {cinta[cabezal]}, Ubicación cabezal: {cabezal}")
        accionesLocal = buscar(estado, cinta[cabezal])
        if accionesLocal:
            cinta[cabezal] = accionesLocal["escribir"]
            estado = accionesLocal["estado"]
            if accionesLocal["cabezal"] == 'L':
                cabezal -= 1
            else:
                cabezal += accionesLocal["cabezal"]
        else:
            print("No se encontraron acciones para el estado y lectura actuales.")
            break
    else:
        break

print("Número binario después de sumar 1:", cinta)
