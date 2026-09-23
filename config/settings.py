import os

# Rutas principales
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Configuración de Base de Datos
DB_NAME = 'scraper.db'
DB_PATH = os.path.join(BASE_DIR, DB_NAME)

# Configuración de Logs
LOG_FILE = os.path.join(BASE_DIR, 'scraper.log')