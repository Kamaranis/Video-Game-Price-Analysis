"""
Módulo para descargar datos de productos de Pricecharting.
"""

from requests_html import HTMLSession

def download_pc(url, session=HTMLSession()):
    """Descarga datos de productos de Pricecharting.

    Args:
        url: La URL de la página de Pricecharting.
        session: Una sesión de Requests-HTML (opcional).

    Returns:
        Una lista de tuplas, donde cada tupla contiene los datos de un producto:
            (product_id, title, loose_price, cib_price, new_price)
    """
    # Parámetros base peticiones
    params = {
        "sort": "",
        "when": "none",
        "release-date": "2024-10-31",
        "format": "json"
    }

    # Valor inicial del cursor
    cursor = 0

    # Lista para almacenar los datos de los productos
    products_data = []

    # Bucle para cargar páginas de productos (videojuegos)
    while True:
        # Actualizamos el valor del cursor
        cursor += 50
        params["cursor"] = cursor

        # Realizamos la petición desde la URL base
        # con los parámetros de la petición
        response = session.get(url, params=params)

        # Si la petición es exitosa
        if response.status_code == 200:
            try:
                # Convertimos la respuesta a JSON
                data = response.json()

                # Si no hay más productos, salimos del bucle
                if not data["products"]:
                    break

                # Iteramos sobre los productos y extraemos los datos
                for product in data["products"]:
                    product_data = extract_product_data(product)
                    products_data.append(product_data)

            except ValueError:
                print(f"Error al procesar la respuesta JSON: {response.content}")
                break

        else:
            print(f"Error en la petición: {response.status_code}")
            break

    return products_data

def extract_product_data(product):
    """
    Extrae los datos relevantes de un producto.
    """
    product_id = product["id"]
    title = product["productName"]
    loose_price = product["price1"]
    cib_price = product["price2"]
    new_price = product["price3"]
    return product_id, title, loose_price, cib_price, new_price