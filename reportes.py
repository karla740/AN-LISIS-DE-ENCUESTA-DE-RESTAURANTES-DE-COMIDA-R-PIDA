# ==============================================================================
# REPORTES 1 AL 5
# ==============================================================================

# Reporte 1. Cantidad de personas por comida preferida
def personas_por_comida(datos):
    # Inicializamos un diccionario vacío para ir guardando los resultados
    conteo_comidas = {}
    
    # Recorremos la lista completa de encuestados, persona por persona
    for p in datos:
        # Aseguramos que la sección "preferencias" exista antes de intentar acceder a ella
        if "preferencias" in p:
            # Extraemos el valor de la comida preferida de esa persona
            comida = p["preferencias"]["comida_preferida"]
            
            # Si la comida ya está registrada en nuestro diccionario, simplemente le sumamos 1 a su contador
            if comida in conteo_comidas:
                conteo_comidas[comida] += 1
            # Si la comida aún no está, la agregamos al diccionario con un valor inicial de 1
            else:
                conteo_comidas[comida] = 1
                
    # Retornamos el diccionario completo con el conteo final de todas las comidas
    return conteo_comidas


# Reporte 2. Frecuencia de consumo
def frecuencia_consumo(datos):
    # Creamos un diccionario vacío para contar las respuestas
    conteo_frecuencia = {}
    
    # Pasamos por cada uno de los registros de nuestra base de datos
    for p in datos:
        # Verificamos que los datos de "preferencias" vengan en el registro
        if "preferencias" in p:
            # Sacamos el dato de la frecuencia (ej. "Semanal", "Mensual")
            frecuencia = p["preferencias"]["frecuencia"]
            
            # Si ya vimos esta frecuencia antes, aumentamos su contador en 1
            if frecuencia in conteo_frecuencia:
                conteo_frecuencia[frecuencia] += 1
            # Si es la primera vez que vemos esta frecuencia, la registramos empezando en 1
            else:
                conteo_frecuencia[frecuencia] = 1
                
    # Devolvemos nuestro diccionario ya con los totales calculados
    return conteo_frecuencia


# Reporte 3. Promedio de gasto
def promedio_gasto(datos):
    # Creamos una variable en 0 donde iremos sumando todo el dinero gastado
    suma_gasto = 0
    # Obtenemos la cantidad exacta de personas midiendo el tamaño de la lista
    total_personas = len(datos)
    
    # Si la lista está vacía (0 personas), regresamos 0 de inmediato 
    # para evitar que el programa falle al intentar dividir entre cero
    if total_personas == 0:
        return 0
        
    # Recorremos a cada persona en la encuesta
    for p in datos:
        # Nos aseguramos de que el bloque "consumo" exista en sus datos
        if "consumo" in p:
            # Sumamos el gasto de esta persona a nuestro total acumulado
            suma_gasto += p["consumo"]["gasto"]
            
    # Calculamos el promedio matemático: todo lo sumado dividido entre el total de gente
    promedio = suma_gasto / total_personas
    
    # Retornamos el resultado, pero redondeado a solo 2 decimales para que se vea como dinero
    return round(promedio, 2)


# Reporte 4. Promedio de satisfacción del producto
def promedio_satisfaccion_producto(datos):
    # Iniciamos nuestro acumulador en 0 para ir sumando las notas
    suma_satisfaccion = 0
    # Contamos cuántas personas respondieron la encuesta en total
    total_personas = len(datos)
    
    # Prevenimos un error del sistema asegurándonos de no dividir entre cero
    if total_personas == 0:
        return 0
        
    # Revisamos los datos persona por persona
    for p in datos:
        # Comprobamos que el diccionario tenga la información de su "experiencia"
        if "experiencia" in p:
            # Tomamos la nota que le dio al producto y la sumamos al gran total
            suma_satisfaccion += p["experiencia"]["producto"]
            
    # Sacamos el promedio dividiendo el puntaje total entre todos los encuestados
    promedio = suma_satisfaccion / total_personas
    
    # Devolvemos el número redondeado a dos decimales para mayor claridad
    return round(promedio, 2)


# Reporte 5. Promedio de satisfacción del servicio
def promedio_satisfaccion_servicio(datos):
    # Variable donde iremos sumando todas las calificaciones del servicio
    suma_satisfaccion = 0
    # Usamos len() para saber el total de personas en la lista
    total_personas = len(datos)
    
    # Si no hay nadie registrado, devolvemos 0 como seguridad
    if total_personas == 0:
        return 0
        
    # Iteramos sobre todos los clientes encuestados
    for p in datos:
        # Validamos que la pregunta sobre su "experiencia" sí fue contestada
        if "experiencia" in p:
            # Añadimos la calificación del servicio al acumulador
            suma_satisfaccion += p["experiencia"]["servicio"]
            
    # Calculamos la media (suma total de calificaciones / cantidad de personas)
    promedio = suma_satisfaccion / total_personas
    
    # Entregamos el promedio final redondeado a dos cifras
    return round(promedio, 2)

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