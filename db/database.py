import sqlite3
import json
from datetime import datetime
from config.settings import DB_PATH
from utils.logger import logger
from utils.errors import ScraperError

def crear_tablas():
    try:
        conexion = sqlite3.connect(DB_PATH)
        cursor = conexion.cursor()
        
        # Tabla para registrar cada ejecución exitosa
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS busquedas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                url TEXT NOT NULL,
                fecha TEXT NOT NULL
            )
        ''')
        
        # Tabla para guardar el detalle de lo extraído
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS resultados (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                busqueda_id INTEGER,
                tipo_dato TEXT NOT NULL,
                contenido TEXT NOT NULL,
                FOREIGN KEY (busqueda_id) REFERENCES busquedas (id)
            )
        ''')
        
        conexion.commit()
        conexion.close()
    except sqlite3.Error as e:
        logger.error(f"Error al crear tablas en SQLite: {e}")
        raise ScraperError("No se pudo inicializar la base de datos.")

def guardar_extraccion(url, datos_extraidos):
    try:
        conexion = sqlite3.connect(DB_PATH)
        cursor = conexion.cursor()
        
        fecha_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cursor.execute('INSERT INTO busquedas (url, fecha) VALUES (?, ?)', (url, fecha_actual))
        busqueda_id = cursor.lastrowid
        
        for tipo, contenido in datos_extraidos.items():
            # Convertirs las listas y diccionarios a un string formato JSON para guardarlo en la celda de la tabla
            contenido_str = json.dumps(contenido, ensure_ascii=False)
            cursor.execute('INSERT INTO resultados (busqueda_id, tipo_dato, contenido) VALUES (?, ?, ?)', 
                           (busqueda_id, tipo, contenido_str))
            
        conexion.commit()
        conexion.close()
        logger.info(f"Datos guardados exitosamente en BD para la URL: {url}")
    except sqlite3.Error as e:
        logger.error(f"Error al insertar en SQLite: {e}")
        raise ScraperError("Error al guardar la información en la base de datos.")