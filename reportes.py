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

# ==============================================================================
# REPORTES 6 AL 10
# ==============================================================================

# Reporte 6. Distribución del tiempo de entrega
def distribucion_tiempo(datos):
    # Inicializamos un diccionario vacío para contar las respuestas de tiempo
    conteo_tiempo = {}
    
    # Recorremos a cada persona encuestada en nuestra lista
    for p in datos:
        # Verificamos que la información de "experiencia" exista para evitar errores
        if "experiencia" in p:
            # Extraemos lo que opinó sobre el tiempo de entrega (ej. "Rápido", "Lento")
            tiempo = p["experiencia"]["tiempo de entrega"]
            
            # Si ya tenemos esa respuesta en el diccionario, le sumamos 1
            if tiempo in conteo_tiempo:
                conteo_tiempo[tiempo] += 1
            # Si es una respuesta nueva, la registramos con el valor de 1
            else:
                conteo_tiempo[tiempo] = 1
                
    # Retornamos el diccionario con el conteo total
    return conteo_tiempo


# Reporte 7. Distribución de percepción de precios
def distribucion_precios(datos):
    # Creamos un diccionario vacío para ir guardando cómo perciben los precios
    conteo_precios = {}
    
    # Pasamos por cada registro de la base de datos
    for p in datos:
        # Aseguramos que el bloque "experiencia" esté presente
        if "experiencia" in p:
            # Sacamos el dato del precio (ej. "Medio", "Caro")
            precio = p["experiencia"]["precio"]
            
            # Si esta percepción ya existe, aumentamos su contador
            if precio in conteo_precios:
                conteo_precios[precio] += 1
            # Si no existe aún, la agregamos empezando en 1
            else:
                conteo_precios[precio] = 1
                
    # Devolvemos el diccionario ya lleno con los resultados
    return conteo_precios


# Reporte 8. Promedio general de satisfacción
def promedio_general_satisfaccion(datos):
    # Variable para ir sumando todas las calificaciones generales
    suma_general = 0
    # Calculamos cuántas personas respondieron en total
    total_personas = len(datos)
    
    # Si la lista está vacía, regresamos 0 para no dividir entre cero
    if total_personas == 0:
        return 0
        
    # Iteramos sobre todos los clientes
    for p in datos:
        # Verificamos que la sección "nps" exista en este registro
        if "nps" in p:
            # Sumamos la calificación general al total acumulado
            suma_general += p["nps"]["general"]
            
    # Calculamos el promedio matemático
    promedio = suma_general / total_personas
    
    # Retornamos el promedio redondeado a dos decimales
    return round(promedio, 2)


# Reporte 9. Porcentaje de clientes que volverían
def porcentaje_volverian(datos):
    # Contador para las personas que dijeron que SÍ volverían
    si_volverian = 0
    # Obtenemos el total de personas encuestadas
    total_personas = len(datos)
    
    # Protección para evitar división por cero si no hay datos
    if total_personas == 0:
        return "0%"
        
    # Recorremos cada persona en los datos
    for p in datos:
        # Validamos que exista "nps" y que la respuesta de "volveria" sea True (Verdadera)
        if "nps" in p and p["nps"]["volveria"]:
            # Si es True, sumamos 1 a nuestro contador
            si_volverian += 1
            
    # Calculamos el porcentaje: (los que dijeron sí / el total) multiplicado por 100
    porcentaje = (si_volverian / total_personas) * 100
    
    # Retornamos un texto formateado con el símbolo de porcentaje y 2 decimales
    return f"{round(porcentaje, 2)}%"


# Reporte 10. Cálculo del NPS (Net Promoter Score)
def calculo_nps(datos):
    # Variables para contar cuántos son promotores y cuántos detractores
    promotores = 0
    detractores = 0
    total_personas = len(datos)
    
    # Si no hay registros, el NPS es 0
    if total_personas == 0:
        return 0
        
    # Recorremos la lista de personas
    for p in datos:
        # Validamos que el bloque "nps" exista
        if "nps" in p:
            # Extraemos la calificación de recomendación que dio el cliente
            recomendacion = p["nps"]["recomendacion"]
            
            # Si la calificación es 9 o 10, es un promotor
            if recomendacion >= 9:
                promotores += 1
            # Si la calificación es 6 o menos, es un detractor (los de 7 y 8 son pasivos y se ignoran en esta parte)
            elif recomendacion <= 6:
                detractores += 1
                
    # Calculamos qué porcentaje del total representan los promotores
    porcentaje_promotores = (promotores / total_personas) * 100
    # Calculamos qué porcentaje del total representan los detractores
    porcentaje_detractores = (detractores / total_personas) * 100
    
    # La fórmula oficial del NPS es: % Promotores - % Detractores
    nps = porcentaje_promotores - porcentaje_detractores
    
    # Retornamos el resultado redondeado a dos decimales
    return round(nps, 2)

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
