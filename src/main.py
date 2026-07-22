from herramientas.evaluador import ancho, comparar, pedir_funcion
from herramientas.graficador import graficar_rectas


def main():
    # 1. Pedir datos
    datos = pedir_funcion()

    # 2. Calcular intersección
    resultado = comparar(datos)

    # 3. Imprimir el resultado en consola
    print("RESULTADO".center(ancho, "-"))
    if isinstance(resultado, dict):
        print(
            f"Punto de intersección: ({resultado['xIntercepto']:.2f}, {resultado['yIntercepto']:.2f})"
        )
    else:
        print(resultado)

    print("-".center(ancho, "-"))

    # 4. Graficar
    graficar_rectas(datos, resultado)


if __name__ == "__main__":
    main()
