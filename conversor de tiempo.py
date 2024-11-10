print("Conversor de tiempo.")
dias = int(input("Ingrese los dias a convertir: "))
horas = int(input("Ingrese las horas a convertir: "))
minutos = int(input("Ingrese los minutos a convertir: "))
segundos = int(input("Ingrese los segundos a convertir: "))

def calcularMilisegundos(dias, horas, minutos, segundos):
    msDias = dias * 86400000
    msHoras = horas * 3600000
    msMinutos = minutos * 60000 
    msSegundos = segundos * 1000
    
    totalMilisegundos = msDias + msHoras + msMinutos + msSegundos
    return totalMilisegundos

resultado = calcularMilisegundos(dias, horas, minutos, segundos)
print("El total en milisegundos es:", resultado)
