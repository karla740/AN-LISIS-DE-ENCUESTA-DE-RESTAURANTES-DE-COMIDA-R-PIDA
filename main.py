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


#-----------------Reportes 16 - 20 -------------------------------

print("\n" + "="*70)
print("REPORTES 16-20".center(70,"-"))
print("="*70)

# Reporte 16. Relación entre precio y recomendación
print("\n16. Relación entre precio y recomendación (Suma de puntos):")
r = reporte16(datos)
for categoria, suma in r['suma'].items():
    print(f"Percepción: {categoria:15} | Suma Recomendación: {suma}")

# Reporte 17. Tiempo de entrega vs Satisfacción
print("\n17. Tiempo de entrega vs Satisfacción (Promedios):")
tiempos = reporte17(datos)
for tiempo, promedio in tiempos.items():
    print(f"Tiempo: {tiempo:15} | Satisfacción Promedio: {promedio}")

# Reporte 18. Ranking de comidas más consumidas
print("\n18. Ranking de comidas más consumidas:")
ranking = reporte18(datos)
for comida, cantidad in ranking.items():
    print(f"Comida: {comida:15} | Cantidad: {cantidad} veces")

# Reporte 19. Promedio general por tipo de comida
print("\n19. Promedio general por tipo de comida:")
promedios = reporte19(datos)
for comida, promedio in promedios.items():
    print(f"Comida: {comida:15} | Calificación Promedio: {promedio}")

# Reporte 20. Perfil del cliente promedio
print("\n20. Perfil del cliente promedio:")
perfil = reporte20(datos)
print(f"Gasto promedio:        ${perfil['gasto_medio']}")
print(f"Satisfacción promedio: {perfil['satisfaccion_media']}/10")