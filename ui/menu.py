def mostrar_menu():
    print("\n" + "="*45)
    print("   SISTEMA DE EXTRACCIÓN Y PROCESAMIENTO WEB")
    print("="*45)
    print("¿Qué información deseas extraer?")
    print("1. Título de la página ()")
    print("2. Encabezados (h1, h2, h3, etc.)")
    print("3. Párrafos (<p>)")
    print("4. Enlaces (<a>)")
    print("5. Imágenes (<img>)")
    print("6. Listas (<ul>, <ol>)")
    print("7. Metadatos (meta)")
    print("8. Tablas HTML")
    print("9. TODO lo anterior")
    print("0. Salir")
    print("-" * 45)

def obtener_seleccion():
    while True:
        opcion = input("Elige una o varias opciones separadas por coma (ej. 1,3,5) o 9 para TODO: ").strip()
        if not opcion:
            continue
            
        try:
            # Convierte la entrada "1, 3" en una lista de enteros: [1, 3]
            selecciones = [int(x.strip()) for x in opcion.split(',')]
            if all(0 <= x <= 9 for x in selecciones):
                return selecciones
        except ValueError:
            pass
            
        print("Error: Ingresa números válidos entre 0 y 9, separados por comas.")

def solicitar_url():
    url = input("\nIntroduce la URL de la página web (ej. https://books.toscrape.com/): ").strip()
    return url