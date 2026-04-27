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
resultado = segmentacion_clientes(datos)
print(f"Promotores: {resultado['promotores']}") 
print(f"Pasivos: {resultado['pasivos']}")
print(f"Detractores: {resultado['detractores']}")