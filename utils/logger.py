import logging
from config.settings import LOG_FILE

def setup_logger():
    logger = logging.getLogger("WebScraper")
    logger.setLevel(logging.INFO)
    
    # Evitar duplicar registros si el logger se invoca varias veces
    if not logger.handlers:
        file_handler = logging.FileHandler(LOG_FILE, encoding='utf-8')
        formato = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formato)
        logger.addHandler(file_handler)
        
    return logger

logger = setup_logger()