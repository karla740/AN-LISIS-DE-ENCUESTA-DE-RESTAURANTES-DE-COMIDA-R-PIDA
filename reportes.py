# Reporte 11. Segmentación: promotores, pasivos, detractores
def segmentacion_clientes(datos):
    promotores = 0
    pasivos = 0
    detractores = 0
    
    for fila in datos:
        calificacion = fila["nps"]["recomendacion"]
        if calificacion >= 9:
            promotores += 1
        elif calificacion >= 7:
            pasivos += 1
        else:
            detractores += 1
    #Retornando como un diccionario los resultados, para acceder a ellos uno por uno
    #Asi si quiero acceder a los promotores, solo tengo que llamar resultado["promotores"] etc
    return {
    "promotores": promotores,
    "pasivos": pasivos,
    "detractores": detractores
    }