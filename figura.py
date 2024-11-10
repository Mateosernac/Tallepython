def dibujarFigura(tamano, figura):
    if figura == "cuadrado":
        for i in range(tamano):
            print("*" * tamano)
    elif figura == "triangulo":
        for i in range(1, tamano + 1):
            print("*" * i)
    else:
        print("Figura no reconocida. Usa 'cuadrado' o 'triangulo'.")

figura = input("¿Qué figura quieres dibujar? (cuadrado/triangulo): ").lower()
tamano = int(input("Ingresa el tamaño del lado: "))

dibujarFigura(tamano, figura)
