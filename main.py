from lectura_datos import *
from reportes import *

ruta="encuesta_restaurante.csv" #Aqui almacenamos la ruta del archivo

datos=cargar_datos(ruta) #Mandamos a llamar la funsion que lee el archivo y donde la esta estructura

#================================= Reportes 11-15 =================================
print("\n" + "="*70)
print("REPORTES 11-15".center(70,"-"))
print("="*70)
#Reporte 11. Segmentación: promotores, pasivos, detractores
print("\n11. Segmentación: promotores, pasivos, detractores")

#Esta funcion retorna un diccionario y lo almacenamos en una variable
resultado = segmentacion_clientes(datos) 

#Imprimimos los resultados por separado
print(f"Promotores: {resultado['promotores']}") 
print(f"Pasivos: {resultado['pasivos']}")
print(f"Detractores: {resultado['detractores']}")

#Reporte 12. Comida con mayor satisfacción
print("\n12. Comida con mayor satisfacción")
print(comida_mayor_satisfaccion(datos))

#Reporte 13. Comida con menor satisfacción
print("\n13. Comida con menor satisfacción") 
print(comida_menor_satisfaccion(datos))

# Reporte 14. Relación entre gasto y satisfacción
print("\n14. Relación entre gasto y satisfacción")

resultado_14 = relacion_gasto_satisfaccion(datos)

for segmento, valores in resultado_14.items():
    print(f"\nSegmento: {segmento}")
    print(f"Promedio de satisfacción: {valores['promedio_satisfaccion']}")
    print(f"Promedio de gasto: {valores['promedio_gasto']}")
