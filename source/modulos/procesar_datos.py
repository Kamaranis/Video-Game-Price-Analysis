#procesar_datos.py

import pandas as pd
import os
from time import strftime
import csv
import glob

def generar_csv(enlaces, nombre_archivo):
    """
    Genera un archivo CSV y un df de pandas 
    a partir de una lista de enlaces.

    Args:
        enlaces: Una lista de enlaces.
        nombre_archivo: El nombre del archivo CSV a generar.
    ejemplo:
        >>> generar_csv([enlaces_web_site_x, 'enlaces_web_site_x.csv')
    """
    # Obtenemos la fecha actual en formato YYYYMMDD
    fecha_actual = strftime("%Y%m%d")
    # Construimos el nombre del archivo con la fecha
    nombre_archivo_con_fecha = f"{nombre_archivo[:-4]}_{fecha_actual}.csv"  

    # Construimos la ruta completa al archivo en la carpeta 'pricecharting'
    ruta_archivo = os.path.join('pricecharting', nombre_archivo_con_fecha)  
    df = pd.DataFrame(enlaces)
    # Guardamos el archivo CSV
    df.to_csv(ruta_archivo, index=False)
    print(f"Se han guardado {len(enlaces)} enlaces en el archivo '{nombre_archivo_con_fecha}'.\n")


def generar_csv_precios_v3(nombre_archivo, datos, nombres_columnas, plataforma):
    """
    Genera un archivo CSV con los datos proporcionados.

  Args:
      nombre_archivo: El nombre del archivo CSV a generar.
      datos: Una lista de tuplas o listas que contienen los datos.
      nombres_columnas: Una lista con los nombres de las columnas para la cabecera.

    """
    fecha_actual = strftime("%Y%m%d")
    nombre_archivo_con_fecha = f"{nombre_archivo[:-4]}_{plataforma}_{fecha_actual}.csv"

    # Obtenemos la ruta del directorio actual
    directorio_actual = os.path.dirname(os.path.abspath(__file__))

    # Construimos la ruta al directorio 'dataset' un nivel por encima
    ruta_dataset = os.path.join(directorio_actual, '..', '..', 'dataset')

    # Creamos el directorio 'dataset' si no existe
    os.makedirs(ruta_dataset, exist_ok=True)

    # Construimos la ruta completa al archivo en la carpeta 'dataset'
    ruta_archivo = os.path.join(ruta_dataset, nombre_archivo_con_fecha)

    print(f"Directorio actual: {directorio_actual}\n")
    print(f"Ruta final del archivo CSV: {ruta_archivo}\n")

    with open(ruta_archivo, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(nombres_columnas)  # Escribimos la cabecera
        writer.writerows(datos)  # Escribimos los datos
        print(f"Se han guardado los datos en el archivo '{nombre_archivo_con_fecha}'.\n")


def agregar_categoria(df, nombre_columna, valor):
    """
    Agrega una nueva columna de tipo categórico con un valor fijo a un DataFrame de pandas.

    Parámetros:
    - df (pd.DataFrame): DataFrame al cual se le añadirá la columna.
    - nombre_columna (str): Nombre de la nueva columna.
    - valor (str): Valor que se aplicará a todos los registros de la nueva columna.

    Retorna:
    - pd.DataFrame: DataFrame con la nueva columna añadida.
    """
    df[nombre_columna] = valor
    print(df.head(10))  # cargamos las primeras 10 filas como ejemplo
    return df


def obtener_fecha_dinamica():
  """
  Esta función devuelve la fecha actual en el formato YYYYMMDD.
  """
  from datetime import datetime
  return datetime.now().strftime("%Y%m%d")

def cargar_archivo_mas_reciente(ruta_dataset, plataforma):
  """
  Carga el archivo CSV más reciente con el formato 'videojuegos_X_Y.csv' 
  donde X es la plataforma y Y es la fecha.

  Args:
      ruta_dataset: La ruta a la carpeta donde se almacenan los datasets.
      plataforma: La plataforma de videojuegos.

  Returns:
      Un DataFrame de pandas con los datos del archivo CSV.
  """
  fecha_dinamica = obtener_fecha_dinamica()
  patron_archivo = f"{ruta_dataset}/videojuegos_{plataforma}_{fecha_dinamica}*.csv"
  lista_archivos = glob.glob(patron_archivo)
  
  if lista_archivos:
    archivo_mas_reciente = max(lista_archivos, key=os.path.getctime)
    df = pd.read_csv(archivo_mas_reciente)
    return df
  else:
    print(f"No se encontraron archivos CSV para la plataforma {plataforma} con la fecha {fecha_dinamica}")
    return None
