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
        opcion = input("Elige una opción (0-9): ").strip()
        if opcion.isdigit() and 0 <= int(opcion) <= 9:
            return int(opcion)
        print("Error: Por favor ingresa un número válido entre 0 y 9.")

def solicitar_url():
    url = input("\nIntroduce la URL de la página web (ej. https://books.toscrape.com/): ").strip()
    return url