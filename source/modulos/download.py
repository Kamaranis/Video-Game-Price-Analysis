# download.py
# Version 3
# Función para descargar sitios de internet
# con manejo de errores

import urllib.request
import time
def download(url, user_agent='Mozilla/5.0', retries=2):
    """Descarga el contenido de una URL con manejo de errores y reintentos.

    Esta función intenta descargar el contenido de una URL específica. 
    Utiliza un `User-Agent` personalizado para evitar bloqueos de ciertos 
    sitios web y maneja errores HTTP y de conexión. Si se produce un error 
    5xx (por ejemplo, problemas temporales del servidor), la función intentará 
    reintentar la descarga hasta el número máximo de `retries`.

    Args:
        url (str): La URL que se desea descargar.
        user_agent (str): El `User-Agent` a enviar en la petición HTTP 
            (por defecto, 'Mozilla/5.0').
        retries (int): Número máximo de intentos de reintento en caso de error (por defecto, 2).

    Returns:
        bytes or None: El contenido descargado en formato de bytes, o `None` en caso de fallo.

    Raises:
        urllib.error.HTTPError: Si se produce un error HTTP, como el código 404.
        urllib.request.URLError: Si se produce otro tipo de error de descarga o conexión.
    
    Ejemplo:
        >>> html = download('https://www.example.com')
        >>> if html:
        >>>     print(html.decode('utf-8'))

    Notas:
        - Implementa un `timeout` de 10 segundos para evitar bloqueos prolongados.
        - Incluye un retraso de 1 segundo entre solicitudes para reducir la probabilidad 
          de ser bloqueado por el servidor.
    """
    print('Downloading:', url)
    headers = {'User-agent': user_agent}
    req = urllib.request.Request(url, headers=headers)

    try:
        # 'Tiempo fuera' para evitar bloqueos prolongados
        html = urllib.request.urlopen(req, timeout=10).read()
    except urllib.error.HTTPError as e:
        print('HTTP Error:', e.code, e.reason)
        html = None
    except urllib.request.URLError as e:
        print('Download error:', e.reason)
        html = None
        if retries > 0 and hasattr(e, 'code') and 500 <= e.code < 600:
            # Reintento para errores 5xx
            return download(url, user_agent, retries - 1)
    
    # Retraso para evitar bloqueos
    time.sleep(1)
    return html