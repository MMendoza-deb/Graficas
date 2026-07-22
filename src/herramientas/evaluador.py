import shutil

ancho = shutil.get_terminal_size().columns


def pedir_float(mensaje):
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print(" Por favor ingresa un número válido (ej. 2 o -1.5).")


def pedir_funcion():
    print(
        "A continuación ingresa los sigueintes parámetros: m (pendiente de la recta ) y b (intercepto en el eje y)"
    )
    print("EQ 1".center(ancho, "-"))
    print("Ingresa la pendiente (m1) y el intercepto(b1) de la ecuación 1")
    m1 = pedir_float("m1: ")
    b1 = pedir_float("b1: ")
    print("-".center(ancho, "-"))
    print("EQ 2".center(ancho, "-"))
    print("Ingresa la pendiente (m2) y el intercepto(b2) de la ecuación 2")
    m2 = pedir_float("m2: ")
    b2 = pedir_float("b2: ")
    print("-".center(ancho, "-"))
    return {"m1": m1, "b1": b1, "m2": m2, "b2": b2}


def comparar(datos):
    m1, b1 = datos["m1"], datos["b1"]
    m2, b2 = datos["m2"], datos["b2"]

    if m1 == m2 and b1 == b2:
        return "Las rectas son idénticas (tienen infinitas intersecciones)"
    if m1 == m2:
        return "Las rectas son paralelas (No hay intersección)"

    # y1=y2
    # m1X + b1 = m2X + b2
    # m1X - m2X = b2 - b1
    # X(m1 - m2) = b2 - b1
    # x = (b2 - b1) / (m1 - m2)
    xIntercepto = (b2 - b1) / (m1 - m2)
    yIntercepto = m1 * xIntercepto + b1
    return {"xIntercepto": xIntercepto, "yIntercepto": yIntercepto}


# datos = pedir_funcion()
# resultado = comparar(datos)
# print(resultado)
