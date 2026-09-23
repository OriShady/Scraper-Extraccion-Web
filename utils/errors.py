class ScraperError(Exception):
    """Clase base para excepciones del scraper."""
    pass

class InvalidURLError(ScraperError):
    """Se lanza cuando la URL tiene un formato incorrecto."""
    pass

class ConnectionError(ScraperError):
    """Se lanza cuando falla la conexión o se agota el tiempo de espera."""
    pass

class HTTPError(ScraperError):
    """Se lanza cuando el servidor devuelve un código de error (ej. 404, 500)."""
    def __init__(self, message, status_code=None):
        super().__init__(message)
        self.status_code = status_code