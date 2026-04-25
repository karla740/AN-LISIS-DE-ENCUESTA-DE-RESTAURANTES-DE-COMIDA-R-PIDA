import csv

def cargar_datos(nombre_archivo):
    lista_encuestados = []
    try:
        with open(nombre_archivo, mode='r', encoding='utf-8') as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                registro = {
                    "id": int(fila["id"]),
                    "prefierencias": {
                        "comida_preferida": fila["comida_preferida"],
                        "frecuencia": fila["frecuencia_consumo"],
                    },
                    "consumo":{
                        "gasto": float(fila["gasto_promedio"])
                    },
                    "experiencia": {
                        "producto": int(fila["satisfaccion_producto"]),
                        "servicio": int(fila["satisfaccion_servicio"]),
                        "tiempo de entrega": fila["tiempo_entrega"],
                        "precio": fila["precio_percepcion"],
                    },
                    "nps": {
                        "recomendacion": int(fila["recomendaria"]),
                        "volveria": fila["volveria_comprar"].strip().lower() == "true",
                        "general": int(fila["calificacion_general"])
                    }
                }
                lista_encuestados.append(registro)
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo {nombre_archivo}")
    return lista_encuestados