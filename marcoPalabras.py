def marcoPalabras(texto):
    palabras = texto.split()
    max_len = max(len(palabra) for palabra in palabras)
    borde = "*" * (max_len + 4)
    
    print(borde)
    for palabra in palabras:
        print(f"* {palabra.ljust(max_len)} *")
    print(borde)

texto = input("Ingresa el texto: ")
marcoPalabras(texto)
