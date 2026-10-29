class Cola:
    def __init__(self):
        self.elementos = []

    def encolar(self, dato):
        self.elementos.append(dato)

    def desencolar(self):
        if not self.esta_vacia():
            return self.elementos.pop(0)
        return None

    def esta_vacia(self):
        return len(self.elementos) == 0


# Colas de los diferentes servicios
servicios = {}

# Contador de números de atención por servicio
contadores = {}


def obtener_cola(servicio):
    if servicio not in servicios:
        servicios[servicio] = Cola()
        contadores[servicio] = 0

    return servicios[servicio]


print("SISTEMA DE ATENCION - COMPANIA DE SEGUROS")
print("------------------------------------------")
print("C1: Registrar cliente en el servicio 1")
print("A1: Atender cliente del servicio 1")
print("Puedes usar cualquier numero de servicio.")
print("S: Salir del programa")

while True:
    comando = input("\nIngresa un comando: ").strip().upper()

    if comando == "S":
        print("Saliendo del sistema...")
        break

    if len(comando) < 2 or comando[0] not in ["C", "A"]:
        print("Comando no valido. Ejemplo: C1 o A1.")
        continue

    try:
        servicio = int(comando[1:].strip())

        if servicio <= 0:
            print("El numero de servicio debe ser mayor que cero.")
            continue

    except ValueError:
        print("Comando no valido. Ejemplo: C1 o A1.")
        continue

    cola = obtener_cola(servicio)

    if comando[0] == "C":
        # Registrar un nuevo cliente
        contadores[servicio] += 1
        numero_atencion = contadores[servicio]

        cola.encolar(numero_atencion)

        print("Cliente registrado correctamente.")
        print("Servicio:", servicio)
        print("Numero de atencion:", numero_atencion)

    elif comando[0] == "A":
        # Atender al siguiente cliente
        if cola.esta_vacia():
            print("No hay clientes esperando en el servicio", servicio)
        else:
            numero_atencion = cola.desencolar()

            print("Atendiendo al cliente numero:", numero_atencion)
            print("Servicio:", servicio)