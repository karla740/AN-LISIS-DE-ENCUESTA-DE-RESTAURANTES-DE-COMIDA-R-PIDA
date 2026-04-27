# Reporte 11. Segmentación: promotores, pasivos, detractores
def segmentacion_clientes(datos): #Define la función que recibe la lista de encuestados.
    promotores = 0 #Inicializa contadores para cada tipo de cliente.
    pasivos = 0
    detractores = 0
    #Recorre cada encuestado (cada fila es un diccionario).
    for fila in datos:
        #Obtiene la calificación de recomendación (pregunta NPS).
        calificacion = fila["nps"]["recomendacion"]
        if calificacion >= 9:
            promotores += 1
        elif calificacion >= 7:
            pasivos += 1
        else:
            detractores += 1
    #Retorna los resultados en un diccionario para poder acceder fácilmente a cada valor.
    return {
    "promotores": promotores,
    "pasivos": pasivos,
    "detractores": detractores
    }

#Reporte 12. Comida con mayor satisfacción
def comida_mayor_satisfaccion(datos):
    #Diccionario para almacenar las comidas y la satisfaccion
    datos_comidas = {} 

    #Recorremos cada encuestado
    for p in datos:

        #Verifica que la clave "preferencias" exista
        if "preferencias" in p:
            
            #Primero obtenemos la comida y la satisfaccion
            comida = p["preferencias"]["comida_preferida"]
            satisfaccion = p["experiencia"]["producto"]

            # Si la comida no existe en el diccionario, se inicializa
            if comida not in datos_comidas:
                datos_comidas[comida] = [0, 0]

            # Se acumula la satisfacción total y se incrementa el contador de clientes
            datos_comidas[comida][0] += satisfaccion
            datos_comidas[comida][1] += 1
                
    # Recorre el diccionario para calcular el promedio y encontrar la comida con mayor satisfacción
    mejor_promedio = 0
    mejor_comida =""
    for comida, valores in datos_comidas.items():
        suma = valores[0]
        cantidad = valores[1]
        promedio = suma / cantidad
        if promedio > mejor_promedio:
            mejor_promedio = promedio
            mejor_comida = comida
    return mejor_comida

# Reporte 13. Comida con menor satisfacción
def comida_menor_satisfaccion(datos):
    datos_comidas = {} #Diccionario para almacenar las comidas y la satisfaccion
    #Recorremos cada encuestado
    for p in datos:
        #Verifica que la clave "preferencias" exista
        if "preferencias" in p:
            #Primero obtenemos la comida y la satisfaccion
            comida = p["preferencias"]["comida_preferida"]
            satisfaccion = p["experiencia"]["producto"]
            # Si la comida no existe en el diccionario, se inicializa
            if comida not in datos_comidas:
                datos_comidas[comida] = [0, 0]

            # Se acumula la satisfacción total y se incrementa el contador de clientes
            datos_comidas[comida][0] += satisfaccion
            datos_comidas[comida][1] += 1
                
    # Recorre el diccionario para calcular el promedio y encontrar la comida con menor satisfacción
    peor_promedio = float("inf")
    peor_comida =""
    for comida, valores in datos_comidas.items():
        suma = valores[0]
        cantidad = valores[1]
        promedio = suma / cantidad
        if promedio < peor_promedio:
            peor_promedio = promedio
            peor_comida = comida
    return peor_comida