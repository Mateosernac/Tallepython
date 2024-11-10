def eliminarCaracteres(str1, str2):
    out1 = ""
    for char in str1:
        if char not in str2:
            out1 += char
    
    out2 = ""
    for char in str2:
        if char not in str1:
            out2 += char
    
    print("out1:", out1)
    print("out2:", out2)
palabra1 = input("Ingrese la primera palabra.")
palabra2 = input("Ingrese la segunda palabra.")
eliminarCaracteres(palabra1, palabra2)
