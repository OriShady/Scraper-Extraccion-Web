def extraer_titulo(soup):
    titulo = soup.find('title')
    return titulo.text.strip() if titulo else "Sin título"

def extraer_encabezados(soup):
    encabezados = {}
    for i in range(1, 7):
        etiqueta = f'h{i}'
        tags = soup.find_all(etiqueta)
        if tags:
            encabezados[etiqueta] = [t.text.strip() for t in tags]
    return encabezados

def extraer_parrafos(soup):
    return [p.text.strip() for p in soup.find_all('p') if p.text.strip()]

def extraer_enlaces(soup):
    return [{'texto': a.text.strip(), 'url': a.get('href')} for a in soup.find_all('a', href=True)]

def extraer_imagenes(soup):
    return [{'alt': img.get('alt', ''), 'src': img.get('src')} for img in soup.find_all('img', src=True)]

def extraer_listas(soup):
    listas = []
    for lista in soup.find_all(['ul', 'ol']):
        items = [li.text.strip() for li in lista.find_all('li')]
        if items:
            listas.append(items)
    return listas

def extraer_metadatos(soup):
    return [{'propiedad': meta.get('name') or meta.get('property'), 'contenido': meta.get('content')} 
            for meta in soup.find_all('meta') if meta.get('content')]

def extraer_tablas(soup):
    tablas_extraidas = []
    for tabla in soup.find_all('table'):
        filas = []
        for fila in tabla.find_all('tr'):
            celdas = [celda.text.strip() for celda in fila.find_all(['td', 'th'])]
            if celdas:
                filas.append(celdas)
        if filas:
            tablas_extraidas.append(filas)
    return tablas_extraidas