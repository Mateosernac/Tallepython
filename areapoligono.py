tipo_poligono = input("Ingresa el tipo de polígono (triangulo, cuadrado, rectangulo): ").strip().lower()

def calcular_area(poligono):
    if poligono == "triangulo":
        base = float(input("Ingresa la base del triángulo: "))
        altura = float(input("Ingresa la altura del triángulo: "))
        area = (base * altura) / 2
        print(f"Área del triángulo: {area}")
        return area
    elif poligono == "cuadrado":
        lado = float(input("Ingresa el lado del cuadrado: "))
        area = lado * lado
        print(f"Área del cuadrado: {area}")
        return area
    elif poligono == "rectangulo":
        ancho = float(input("Ingresa el ancho del rectángulo: "))
        alto = float(input("Ingresa el alto del rectángulo: "))
        area = ancho * alto
        print(f"Área del rectángulo: {area}")
        return area
    else:
        print("Polígono no soportado.")
        return None

calcular_area(tipo_poligono)

