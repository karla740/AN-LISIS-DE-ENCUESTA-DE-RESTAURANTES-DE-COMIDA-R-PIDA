from lectura_datos import *
from reportes import *

# 1. Cargar datos al inicio
ruta = "encuesta_restaurante.csv"
datos = cargar_datos(ruta)

# ==============================================================================
# FUNCIÓN AUXILIAR PARA PAUSAR LA PANTALLA
# ==============================================================================
def pausar():
    """Detiene la ejecución hasta que el usuario presione ENTER."""
    input("\n[ Presiona ENTER para continuar... ]")

# ==============================================================================
# SUBMENÚS
# ==============================================================================

def submenu_1_5():
    while True:
        print("\n" + "-"*50)
        print(" SUBMENÚ: REPORTES 1 AL 5 (Integrante 1) ".center(50, "-"))
        print("-"*50)
        print("1. Cantidad de personas por comida preferida")
        print("2. Frecuencia de consumo")
        print("3. Promedio de gasto")
        print("4. Promedio de satisfacción del producto")
        print("5. Promedio de satisfacción del servicio")
        print("6. Volver al Menú Principal")
        
        opcion = input("\nElige un reporte (1-6): ")
        
        if opcion == '1':
            print("\n--- 1. Personas por comida preferida ---")
            for comida, cantidad in personas_por_comida(datos).items():
                print(f"   - {comida}: {cantidad} personas")
            pausar()
            
        elif opcion == '2':
            print("\n--- 2. Frecuencia de consumo ---")
            for frecuencia, cantidad in frecuencia_consumo(datos).items():
                print(f"   - {frecuencia}: {cantidad} personas")
            pausar()
            
        elif opcion == '3':
            print(f"\n--- 3. Promedio de gasto ---\n   $ {promedio_gasto(datos)}")
            pausar()
            
        elif opcion == '4':
            print(f"\n--- 4. Satisfacción del producto ---\n   {promedio_satisfaccion_producto(datos)} / 10 pts")
            pausar()
            
        elif opcion == '5':
            print(f"\n--- 5. Satisfacción del servicio ---\n   {promedio_satisfaccion_servicio(datos)} / 10 pts")
            pausar()
            
        elif opcion == '6':
            break
            
        else:
            print("\nOpción inválida. Intenta de nuevo.")
            pausar()

def submenu_6_10():
    while True:
        print("\n" + "-"*50)
        print(" SUBMENÚ: REPORTES 6 AL 10 (Integrante 2) ".center(50, "-"))
        print("-"*50)
        print("1. Distribución del tiempo de entrega")
        print("2. Distribución de percepción de precios")
        print("3. Promedio general de satisfacción")
        print("4. Porcentaje de clientes que volverían")
        print("5. Cálculo del NPS (Net Promoter Score)")
        print("6. Volver al Menú Principal")
        
        opcion = input("\nElige un reporte (1-6): ")
        
        if opcion == '1':
            print("\n--- 6. Distribución del tiempo de entrega ---")
            tiempos = distribucion_tiempo(datos)
            for tiempo, cantidad in tiempos.items():
                print(f"   - {tiempo}: {cantidad} respuestas")
            pausar()
            
        elif opcion == '2':
            print("\n--- 7. Distribución de percepción de precios ---")
            precios = distribucion_precios(datos)
            for precio, cantidad in precios.items():
                print(f"   - {precio}: {cantidad} respuestas")
            pausar()
            
        elif opcion == '3':
            print("\n--- 8. Promedio general de satisfacción ---")
            resultado = promedio_general_satisfaccion(datos)
            print(f"   Calificación promedio: {resultado} / 10 pts")
            pausar()
            
        elif opcion == '4':
            print("\n--- 9. Porcentaje de clientes que volverían ---")
            resultado = porcentaje_volverian(datos)
            print(f"   Índice de retorno: {resultado}")
            pausar()
            
        elif opcion == '5':
            print("\n--- 10. Cálculo del NPS (Net Promoter Score) ---")
            resultado = calculo_nps(datos)
            print(f"   Puntaje NPS: {resultado}")
            print("   (Fórmula: %Promotores - %Detractores)")
            pausar()
            
        elif opcion == '6':
            break
            
        else:
            print("\nOpción inválida. Intenta de nuevo.")
            pausar()

def submenu_11_15():
    while True:
        print("\n" + "-"*50)
        print(" SUBMENÚ: REPORTES 11 AL 15 (Integrante 3) ".center(50, "-"))
        print("-"*50)
        print("1. Segmentación: promotores, pasivos, detractores")
        print("2. Comida con mayor satisfacción")
        print("3. Comida con menor satisfacción")
        print("4. Relación entre gasto y satisfacción")
        print("5. Frecuencia vs satisfacción")
        print("6. Volver al Menú Principal")
        
        opcion = input("\nElige un reporte (1-6): ")
        
        if opcion == '1':
            print("\n--- 11. Segmentación: promotores, pasivos, detractores ---")
            resultado = segmentacion_clientes(datos) 
            print(f"   Promotores: {resultado['promotores']}") 
            print(f"   Pasivos:    {resultado['pasivos']}")
            print(f"   Detractores: {resultado['detractores']}")
            pausar()
            
        elif opcion == '2':
            print("\n--- 12. Comida con mayor satisfacción ---")
            print(f"   {comida_mayor_satisfaccion(datos)}")
            pausar()
            
        elif opcion == '3':
            print("\n--- 13. Comida con menor satisfacción ---")
            print(f"   {comida_menor_satisfaccion(datos)}")
            pausar()
            
        elif opcion == '4':
            print("\n--- 14. Relación Gasto vs Satisfacción ---")
            resultado_14 = relacion_gasto_satisfaccion(datos)

            for segmento, valores in resultado_14.items():
                print(f"\nSegmento: {segmento}")
                print(f"Promedio de satisfacción: {valores['promedio_satisfaccion']}")
                print(f"Promedio de gasto: {valores['promedio_gasto']}")
            pausar()
            
        elif opcion == '5':
            print("\n--- 15. Frecuencia vs Satisfacción ---")
            print("   (Llamada a tu función)")
            pausar()
            
        elif opcion == '6':
            break
        else:
            print("\nOpción inválida. Intenta de nuevo.")
            pausar()

def submenu_16_20():
    while True:
        print("\n" + "-"*50)
        print(" SUBMENÚ: REPORTES 16 AL 20 (Integrante 4) ".center(50, "-"))
        print("-"*50)
        print("1. Precio vs recomendación")
        print("2. Tiempo de entrega vs satisfacción")
        print("3. Ranking de comidas más consumidas")
        print("4. Promedio general por tipo de comida")
        print("5. Perfil del cliente promedio")
        print("6. Volver al Menú Principal")
        
        opcion = input("\nElige un reporte (1-6): ")
        
        if opcion == '1':
            print("\n--- 16. Relación entre precio y recomendación (Suma de puntos) ---")
            r = reporte16(datos)
            for categoria, suma in r['suma'].items():
                print(f"   Percepción: {categoria:15} | Suma Recomendación: {suma}")
            pausar()
            
        elif opcion == '2':
            print("\n--- 17. Tiempo de entrega vs Satisfacción (Promedios) ---")
            tiempos = reporte17(datos)
            for tiempo, promedio in tiempos.items():
                print(f"   Tiempo: {tiempo:15} | Satisfacción Promedio: {promedio}")
            pausar()
            
        elif opcion == '3':
            print("\n--- 18. Ranking de comidas más consumidas ---")
            ranking = reporte18(datos)
            for comida, cantidad in ranking.items():
                print(f"   Comida: {comida:15} | Cantidad: {cantidad} veces")
            pausar()
            
        elif opcion == '4':
            print("\n--- 19. Promedio general por tipo de comida ---")
            promedios = reporte19(datos)
            for comida, promedio in promedios.items():
                print(f"   Comida: {comida:15} | Calificación Promedio: {promedio}")
            pausar()
            
        elif opcion == '5':
            print("\n--- 20. Perfil del cliente promedio ---")
            perfil = reporte20(datos)
            print(f"   Gasto promedio:        ${perfil['gasto_medio']}")
            print(f"   Satisfacción promedio: {perfil['satisfaccion_media']}/10")
            pausar()
            
        elif opcion == '6':
            break
        else:
            print("\nOpción inválida. Intenta de nuevo.")
            pausar()

# ==============================================================================
# MENÚ PRINCIPAL
# ==============================================================================

def menu_principal():
    while True:
        print("\n" + "="*50)
        print(" SISTEMA DE ANÁLISIS DE RESTAURANTES ".center(50, "="))
        print("="*50)
        print(f"Registros cargados: {len(datos)}\n")
        print("1. Reportes 1 al 5   (Integrante 1)")
        print("2. Reportes 6 al 10  (Integrante 2)")
        print("3. Reportes 11 al 15 (Integrante 3)")
        print("4. Reportes 16 al 20 (Integrante 4)")
        print("5. Salir del sistema")
        
        opcion = input("\nSeleccione el bloque de reportes (1-5): ")
        
        if opcion == '1':
            submenu_1_5()
        elif opcion == '2':
            submenu_6_10()
        elif opcion == '3':
            submenu_11_15()
        elif opcion == '4':
            submenu_16_20()
        elif opcion == '5':
            print("\nSaliendo del sistema... ¡Buen trabajo equipo!\n")
            break
        else:
            print("\nOpción inválida. Por favor, ingrese un número del 1 al 5.")
            pausar()

# ==============================================================================
# ARRANQUE DEL PROGRAMA
# ==============================================================================
if __name__ == "__main__":
    if datos:
        menu_principal()
