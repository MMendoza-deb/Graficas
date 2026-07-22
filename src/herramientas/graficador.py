import matplotlib.pyplot as plt
import numpy as np


def graficar_rectas(datos, resultado):
    m1, b1 = datos["m1"], datos["b1"]
    m2, b2 = datos["m2"], datos["b2"]

    # Definimos el rango de X centrado en la intersección si existe
    if isinstance(resultado, dict):
        x_center = resultado["xIntercepto"]
        x = np.linspace(x_center - 10, x_center + 10, 400)
    else:
        x = np.linspace(-10, 10, 400)

    # Calculamos Y para cada recta
    y1 = m1 * x + b1
    y2 = m2 * x + b2

    # Trazamos las rectas
    plt.plot(x, y1, label=f"y1 = {m1}x + {b1}", color="blue")
    plt.plot(x, y2, label=f"y2 = {m2}x + {b2}", color="orange")

    # Si hay un punto de intersección, lo graficamos con un punto rojo
    if isinstance(resultado, dict):
        px = resultado["xIntercepto"]
        py = resultado["yIntercepto"]
        plt.plot(px, py, "ro", markersize=8, label=f"Intersección ({px:.2f}, {py:.2f})")

    # Estilos de la gráfica
    plt.axhline(0, color="black", linewidth=0.8, linestyle="--")
    plt.axvline(0, color="black", linewidth=0.8, linestyle="--")
    plt.grid(True, linestyle=":", alpha=0.6)
    plt.legend()
    plt.title("Intersección de Rectas")
    plt.xlabel("Eje X")
    plt.ylabel("Eje Y")

    # Mostrar ventana con la gráfica
    plt.show()
    # plt.savefig("interseccion.png", dpi=300, bbox_inches="tight")
    # print("Gráfica guardada exitosamente como 'interseccion.png'")
