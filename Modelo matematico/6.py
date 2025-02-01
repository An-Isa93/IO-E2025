import time

def cortar_viguetas(n_viguetas):
    # Definir tiempos de cada operación (en segundos)
    tiempos = {
        'colocar': 15,
        'medir': 5,
        'marcar': 5,
        'cortar': 20,
        'apilar': 20
    }
    
    # Definir los tiempos iniciales de los trabajadores
    t1_disponible = 0  # Tiempo en que el Trabajador 1 estará libre
    t2_disponible = 0  # Tiempo en que el Trabajador 2 estará libre
    cortador_disponible = 0  # Tiempo en que el cortador estará libre
    
    # Lista para almacenar los tiempos finales de cada vigueta
    tiempos_finales = []
    
    for i in range(n_viguetas):
        # Asignar tiempo de colocación y medición a los Trabajadores 1 y 2
        inicio_colocar = max(t1_disponible, t2_disponible)
        fin_colocar = inicio_colocar + tiempos['colocar']
        fin_medir = fin_colocar + tiempos['medir']
        
        # Asignar tiempo de marcado y corte al Cortador
        inicio_marcar = max(fin_medir, cortador_disponible)
        fin_marcar = inicio_marcar + tiempos['marcar']
        inicio_cortar = fin_marcar
        fin_cortar = inicio_cortar + tiempos['cortar']
        
        # Asignar tiempo de apilado a los Trabajadores 1 y 2
        fin_apilar = fin_cortar + tiempos['apilar']
        
        # Actualizar disponibilidad de los trabajadores
        t1_disponible = fin_apilar
        t2_disponible = fin_apilar
        cortador_disponible = fin_cortar
        
        # Guardar el tiempo final de la vigueta
        tiempos_finales.append(fin_apilar)
        
        print(f"Vigueta {i+1}: Termina en {fin_apilar} segundos")
    
    # Tiempo total mínimo para completar todas las viguetas
    tiempo_total = max(tiempos_finales)
    print(f"Tiempo total mínimo: {tiempo_total} segundos")

# Ejecutar la simulación con 6 viguetas
cortar_viguetas(6)
