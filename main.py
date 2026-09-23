from ui.menu import mostrar_menu, obtener_seleccion, solicitar_url
from core.network import obtener_html
from utils.errors import ScraperError

def main():
    while True:
        url = solicitar_url()
        if not url:
            print("La URL no puede estar vacía.")
            continue
            
        mostrar_menu()
        seleccion = obtener_seleccion()
        
        if seleccion == 0:
            print("Saliendo del programa...")
            break
            
        print(f"\n[+] Conectando a {url}...")
        
        try:
            # Intentamos obtener el HTML
            html = obtener_html(url)
            print(f"[+] ¡Conexión exitosa! Se descargaron {len(html)} caracteres de HTML.")
            
        except ScraperError as e:
            # Atrapa nuestros errores personalizados y los muestra en rojo/consola
            print(f"[-] ERROR: {e}")
        
        print("\n[!] Siguiente paso: Analizar este HTML con BeautifulSoup...")
        
        continuar = input("\n¿Deseas analizar otra URL? (s/n): ").strip().lower()
        if continuar != 's':
            print("Saliendo del programa...")
            break

if __name__ == "__main__":
    main()