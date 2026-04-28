# Reporte 11. Segmentación: promotores, pasivos, detractores
def segmentacion_clientes(datos):
    
    #Inicializa contadores para cada tipo de cliente.
    promotores = 0 
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

# Reporte 14. Relación entre gasto y satisfacción
def relacion_gasto_satisfaccion(datos):
    
    # Diccionario para agrupar por rangos de gasto
    segmentos = {
        "bajo": [0, 0, 0],      # suma_satisfaccion, cantidad, gasto_total
        "medio": [0, 0, 0],
        "alto": [0, 0, 0]
    }

    for p in datos:
        
        # Obtener datos
        gasto = p["consumo"]["gasto"]
        producto = p["experiencia"]["producto"]
        servicio = p["experiencia"]["servicio"]
        
        # Promedio de satisfacción
        satisfaccion = (producto + servicio) / 2
        
        # Clasificación por gasto
        if gasto < 50:
            segmento = "bajo"
        elif gasto <= 100:
            segmento = "medio"
        else:
            segmento = "alto"
        
        # Acumular datos
        segmentos[segmento][0] += satisfaccion
        segmentos[segmento][1] += 1
        segmentos[segmento][2] += gasto

    # Calcular promedios finales
    resultado = {}

    for key, valores in segmentos.items():
        suma_sat = valores[0]
        cantidad = valores[1]
        suma_gasto = valores[2]

        if cantidad > 0:
            resultado[key] = {
                "promedio_satisfaccion": round((suma_sat / cantidad),2),
                "promedio_gasto": round((suma_gasto / cantidad), 2)
            }
        else:
            resultado[key] = {
                "promedio_satisfaccion": 0,
                "promedio_gasto": 0
            }

    return resultado
