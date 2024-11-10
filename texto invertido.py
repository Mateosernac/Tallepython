def invertir_cadena(texto):
    invertida = ""
    for i in range(len(texto) - 1, -1, -1):
        invertida += texto[i]      
    return invertida
cadena = input("Ingrese un texto: ")
cadena_invertida = invertir_cadena(cadena)
print("El texto invertido es:", cadena_invertida)
