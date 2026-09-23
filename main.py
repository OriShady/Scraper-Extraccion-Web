from ui.menu import mostrar_menu, obtener_seleccion, solicitar_url
from core.network import obtener_html
from core.parser import analizar_html
from core.extractors import (extraer_titulo, extraer_encabezados, extraer_parrafos,
                             extraer_enlaces, extraer_imagenes, extraer_listas,
                             extraer_metadatos, extraer_tablas)
from db.database import crear_tablas, guardar_extraccion
from utils.errors import ScraperError

EXTRACTORES = {
    1: ("Título", extraer_titulo),
    2: ("Encabezados", extraer_encabezados),
    3: ("Párrafos", extraer_parrafos),
    4: ("Enlaces", extraer_enlaces),
    5: ("Imágenes", extraer_imagenes),
    6: ("Listas", extraer_listas),
    7: ("Metadatos", extraer_metadatos),
    8: ("Tablas", extraer_tablas)
}

def procesar_extraccion(soup, selecciones):
    resultados = {}
    if 9 in selecciones:
        selecciones = list(range(1, 9))
        
    for sel in selecciones:
        if sel in EXTRACTORES:
            nombre, funcion = EXTRACTORES[sel]
            resultados[nombre] = funcion(soup)
    return resultados

def main():
    # Inicializa la BD si no existe
    try:
        crear_tablas()
    except ScraperError as e:
        print(f"[-] ERROR CRÍTICO: {e}")
        return

    while True:
        url = solicitar_url()
        if not url:
            print("La URL no puede estar vacía.")
            continue
            
        mostrar_menu()
        selecciones = obtener_seleccion()
        
        if 0 in selecciones:
            print("Saliendo del programa...")
            break

        print(f"\n[+] Conectando a {url}...")
            
        try:
            html = obtener_html(url)
            print(f"[+] Conexión exitosa. Analizando documento HTML...")
            
            soup = analizar_html(html)
            datos_extraidos = procesar_extraccion(soup, selecciones)
            
            print("\n" + "="*30 + "\nRESUMEN DE EXTRACCIÓN\n" + "="*30)
            for clave, valor in datos_extraidos.items():
                print(f"\n--- {clave} ---")
                if isinstance(valor, list):
                    print(f"Total extraído: {len(valor)} elementos.")
                    print(f"Muestra: {valor[:2]}")
                elif isinstance(valor, dict):
                    print(f"Total extraído: {len(valor)} categorías.")
                    print(f"Muestra: {list(valor.items())[:1]}")
                else:
                    print(valor)
            
            # Guardamos la información en SQLite
            guardar_extraccion(url, datos_extraidos)
            print("\n[+] Información guardada exitosamente en la base de datos.")
            
        except ScraperError as e:
            print(f"[-] ERROR: {e}")
        
        continuar = input("\n¿Deseas analizar otra URL? (s/n): ").strip().lower()
        if continuar != 's':
            print("Saliendo del programa...")
            break

if __name__ == "__main__":
    main()