def obtener_valores_url(url):
    inicio_parametros = -1
    for i in range(len(url)):
        if url[i] == '?':
            inicio_parametros = i
            break

    if inicio_parametros == -1:
        return []

    valores = []
    valor_actual = ""
    es_valor = False

    for i in range(inicio_parametros + 1, len(url)):
        if url[i] == '=':
            es_valor = True
        elif url[i] == '&':
            valores.append(valor_actual)
            valor_actual = ""
            es_valor = False
        elif es_valor:
            valor_actual += url[i]

    if valor_actual:
        valores.append(valor_actual)

    return valores


url = input("Ingrese url: ")
valores = obtener_valores_url(url)
print("Los valores de los parámetros son:", valores)
