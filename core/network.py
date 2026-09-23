import requests
from utils.errors import InvalidURLError, ConnectionError, HTTPError
from utils.logger import logger

def obtener_html(url):
    logger.info(f"Iniciando solicitud a: {url}")
    try:
        if not url.startswith(('http://', 'https://')):
            logger.error(f"Formato de URL inválido: {url}")
            raise InvalidURLError("La URL debe comenzar con http:// o https://")

        # Solicitud HTTP con límite de tiempo de 10 segundos
        response = requests.get(url, timeout=10)
        response.raise_for_status() # Verifica si hay errores HTTP (como el 404)
        
        logger.info("Página HTML obtenida exitosamente.")
        return response.text

    except requests.exceptions.MissingSchema:
        logger.error(f"URL incompleta o inválida: {url}")
        raise InvalidURLError("El formato de la URL es incorrecto.")
    except requests.exceptions.ConnectionError:
        logger.error(f"Fallo de conexión al acceder a: {url}")
        raise ConnectionError("No se pudo establecer conexión con la página.")
    except requests.exceptions.Timeout:
        logger.error(f"Tiempo de espera agotado para: {url}")
        raise ConnectionError("El servidor tardó demasiado en responder.")
    except requests.exceptions.HTTPError as e:
        status = e.response.status_code
        logger.error(f"Error HTTP {status} al acceder a: {url}")
        raise HTTPError(f"El servidor devolvió un error HTTP.", status_code=status)