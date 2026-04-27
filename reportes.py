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



def reporte16(datos):
    #Calcula la suma de recomendaciones según la percepción del precio.
    analisis = {}
    for fila in datos:
        p = fila["experiencia"]["precio"]
        r = fila["nps"]["recomendacion"]
        # Acumula la recomendación por cada categoría de precio
        analisis[p] = analisis.get(p, 0) + r
    return {"suma": analisis}

def reporte17(datos):
    #"""Promedio de satisfacción general según el tiempo de entrega."""
    tiempos = {}
    conteos = {}
    for fila in datos:
        t = fila["experiencia"]["tiempo de entrega"]
        s = fila["nps"]["general"]
        tiempos[t] = tiempos.get(t, 0) + s
        conteos[t] = conteos.get(t, 0) + 1
    
    # Genera el promedio por cada tiempo (Rápido, Normal, Lento)
    return {t: round(tiempos[t]/conteos[t], 2) for t in tiempos}

def reporte18(datos):
    #"""Crea un ranking de las comidas más mencionadas."""
    ranking = {}
    for fila in datos:
        comida = fila["preferencias"]["comida_preferida"]
        ranking[comida] = ranking.get(comida, 0) + 1
    # Ordena el diccionario de mayor a menor frecuencia
    return dict(sorted(ranking.items(), key=lambda item: item[1], reverse=True))

def reporte19(datos):
    #"""Promedio de calificación general por cada tipo de comida rápida."""
    comidas = {}
    conteos = {}
    for fila in datos:
        c = fila["preferencias"]["comida_preferida"]
        g = fila["nps"]["general"]
        comidas[c] = comidas.get(c, 0) + g
        conteos[c] = conteos.get(c, 0) + 1
    return {c: round(comidas[c]/conteos[c], 2) for c in comidas}

def reporte20(datos):
    #"""Define el perfil promedio: gasto y satisfacción de todos los encuestados."""
    total_gasto = 0
    total_sat = 0
    cantidad = len(datos)
    
    if cantidad == 0: return "Sin datos"
    
    for fila in datos:
        total_gasto += fila["consumo"]["gasto"]
        total_sat += fila["nps"]["general"]
        
    return {
        "gasto_medio": round(total_gasto / cantidad, 2),
        "satisfaccion_media": round(total_sat / cantidad, 2)
    }