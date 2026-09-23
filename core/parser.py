from bs4 import BeautifulSoup
from utils.logger import logger
from utils.errors import ScraperError

def analizar_html(html):
    logger.info("Iniciando análisis del HTML con BeautifulSoup.")
    try:
        # Se utiliza html.parser que viene incluido por defecto en Python
        soup = BeautifulSoup(html, 'html.parser')
        return soup
    except Exception as e:
        logger.error(f"Error al analizar HTML: {e}")
        raise ScraperError("No se pudo procesar el documento HTML.")