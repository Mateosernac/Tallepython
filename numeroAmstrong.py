def numeroArmstrong(numero):
    digitos = str(numero)
    num_digitos = len(digitos)
    suma = sum(int(digito) ** num_digitos for digito in digitos)
    return suma == numero

numero = int(input("Ingresa un número: "))
if numeroArmstrong(numero):
    print(f"{numero} es un número de Armstrong")
else:
    print(f"{numero} no es un número de Armstrong")
