import os
import time
import sys

CARPETA_REPORTES = "./reportes_diarios_susana"

def limpiar_reportes_antiguos():
    print("--- INICIANDO MANTENIMIENTO AUTOMATIZADO ---")
    
    # CONTROL DE SEGURIDAD: Si el alumno olvidó crear la carpeta, el script falla.
    if not os.path.exists(CARPETA_REPORTES):
        print("[ERROR CRÍTICO]: No existe la carpeta 'reportes_diarios'.")
        print("Por favor, créala y coloca un archivo dentro antes de correr este script.")
        sys.exit(1) 
        
    tiempo_actual = time.time()
    archivos_eliminados = 0

    # Escaneamos la carpeta real
    for archivo in os.listdir(CARPETA_REPORTES):
        ruta_completa = os.path.join(CARPETA_REPORTES, archivo)
        
        if os.path.isfile(ruta_completa) and archivo.endswith(".csv"):
            fecha_modificacion = os.path.getmtime(ruta_completa)
            
            # REGLA: Compara el tiempo actual con la fecha del archivo.
            # Como el archivo ya existe en tu disco, la diferencia será mayor a 5 segundos.
            if (tiempo_actual - fecha_modificacion) > 5:
                os.remove(ruta_completa)
                print(f"[CONSOLA] Archivo obsoleto eliminado: {archivo}")
                archivos_eliminados += 1

    print(f"--- MANTENIMIENTO FINALIZADO. Se eliminaron {archivos_eliminados} archivos. ---")
    sys.exit(0) 

if __name__ == "__main__":
    limpiar_reportes_antiguos()
