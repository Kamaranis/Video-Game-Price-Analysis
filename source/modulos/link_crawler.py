#link_crawler.py
"""
Modulo que contiene la función link_Crawler , la cual se encarga de extraer 
los links de una pagina web y almacenarlos en una variable.

"""
from bs4 import BeautifulSoup
import re
from urllib.parse import urljoin
from modulos.download import download

def link_crawler(seed_url, link_regex):
    """
    Rastrea una página web y extrae enlaces que coincidan con una expresión regular.

    Args:
        seed_url: La URL inicial para comenzar el rastreo.
        link_regex: Una expresión regular para filtrar los enlaces.

    Returns:
        Una lista de enlaces que coinciden con la expresión regular desde 
        el archivo extraído de la URL tratada con beautifulsoup.

    Ejemplo:
        >>> enlaces = link_crawler('https://www.example.com', 'example')
        >>> print(enlaces)
        ['https://www.example.com/example1', 'https://www.example.com/example2']
    
    """
    crawl_queue = [seed_url]
    visited = set()
    enlaces = []

    while crawl_queue:
        url = crawl_queue.pop()
        if url in visited:
            continue
        visited.add(url)

        html = download(url)
        if html is None:
            continue
        
        soup = BeautifulSoup(html, 'html.parser')
        for link in soup.find_all('a', href=True):
            href = link['href']
            full_url = urljoin(url, href)
            if re.match(link_regex, href):
                enlaces.append(full_url)
                print("Añadiendo enlace:", full_url)

    return enlaces