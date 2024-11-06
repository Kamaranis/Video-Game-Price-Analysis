#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Autor: Anton Barrera Mora (abarreramora@uoc.edu)
Organización: Universitat Oberta de Catalunya (UOC)
Asignatura: PR1 - Tipología y ciclo de vida de los datos
Fecha de creación: 2024-10-29
Descripción: Este script realiza web scraping de Pricecharting.com para extraer
             información sobre precios de videojuegos y generar un archivo CSV.
Licencia: CC BY-NC-SA 4.0

Descripción:

Este módulo ejecuta el flujo principal del programa para descargar y procesar
los datos de precios de videojuegos de Pricecharting.com. El proceso se divide
en las siguientes etapas:

1. Extracción de los enlaces de los videojuegos de interés.
2. Extracción de los datos de precios de los videojuegos plataforma X.
3. Extracción de los datos de precios de los videojuegos plataforma Y.
4. Creación de un dataset final con los datos de ambas plataformas.

"""
# main.py

from modulos.link_crawler import link_crawler
from modulos.procesar_datos import generar_csv
import pandas as pd
import os
from modulos.procesar_datos import cargar_archivo_mas_reciente
from modulos.download_pc import download_pc
from modulos.procesar_datos import agregar_categoria
from modulos.procesar_datos import generar_csv_precios_v3


print("Practica 1 - Tipología y ciclo de vida de los datos")
print("Autor: Anton Barrera Mora")
print("Correo: abarreramora@uoc.edu")
print("Organización: Universitat Oberta de Catalunya (UOC)")
print("PR1: Web Scraping de videojuegos de consola con potencial de revalorización\n")
print("Nos basaremos en la web Pricecharting.com para obtener información sobre precios de videojuegos.")
print("En este trabajo analizaremos los precios de los videojuegos de XBOX en varios modelos.\n")
input("Presiona Enter para continuar con el proceso de Web Scraping...")
print("Iniciando proceso de web scraping...\n")

# 1. Extracción de enlaces de videojuegos XBOX
print(f"En un primer paso, extraeremos los enlaces de los videojuegos...")
print("Esto nos permitirá obtener los enlaces a las diferentes plataformas de las que extraeremos los precios")
input("Presiona Enter para continuar con la extracción de enlaces de videojuegos...\n")

# Definimos la URL semilla y la expresión regular
seed_url = 'https://www.pricecharting.com/es/category/video-games'
print(f"URL de la que vamos a partir para el Web Scrapings: \n{seed_url}\n")

# Capturamos solo enlaces de consolas que no terminan en 'price'
link_regex = r'^/es/console/(?!.*price$).+'
input("\nPresiona Enter para iniciar la extracción de enlaces de videojuegos...")

# Llamamos al crawler
enlaces_price_charting = link_crawler(seed_url, link_regex)

# Guardamos los enlaces en un archivo CSV
# y en un dataframe de pandas
input("\nPresiona Enter para guardar los enlaces en un archivo CSV...")
generar_csv(enlaces_price_charting, 'enlaces_price_charting.csv')

enlaces_price_charting = pd.DataFrame(enlaces_price_charting, columns=["enlaces"])
input("\nPresiona Enter para mostrar los primeros registros del dataframe de videojuegos de Xbox One..")
print(f"\n,{enlaces_price_charting.head()}\n")



###### Inicio de procesamiento de precios xbox-one ###################
###########################################################################

# 2. Extracción de datos de precios de videojuegos XBOX ONE

# URL base de la página
# Filtramos los enlaces que contengan la palabra "xbox-one"
base_url = enlaces_price_charting[enlaces_price_charting['enlaces'].str.contains("xbox-one", case=False)]
base_url = base_url['enlaces'].iloc[0] if not base_url.empty else None

# base_url = "https://www.pricecharting.com/console/xbox-one"
print(f"URL base de la página de Pricecharting: \n{base_url}\n")

# Llamamos a la función para descargar los datos
# y guardarlos en un archivo CSV
input("\nPresiona Enter para iniciar la extracción de datos de precios de videojuegos...")


precios_xbox_one = download_pc(base_url)

input("\nPresiona Enter para tener una muestra de los resultados...")

# Imprimimos los datos de cada videojuego
for juego in precios_xbox_one:
    product_id, title, loose_price, cib_price, new_price = juego
    print(f"ID: {product_id}, Título: {title}, Loose: {loose_price}, CIB: {cib_price}, New: {new_price}")

# Accedemos a los datos de un videojuego específico
primer_juego = precios_xbox_one[0]
# Accedemos al título del primer juego
print(f"El primer juego es: {primer_juego[1]}")

# Guardamos los datos en un archivo CSV
input("\nPresiona Enter para guardar los datos en un archivo CSV...")

from modulos.procesar_datos import generar_csv_precios_v3


# Llamamos a la función para generar el CSV
generar_csv_precios_v3(
    nombre_archivo='videojuegos.csv', 
    datos=precios_xbox_one, 
    nombres_columnas=["ID", "Título", "Loose", "CIB", "New"],
    plataforma="Xbox One"
)

# creamos un dataframe de pandas para los juegos de Xbox One
input("\nPresiona Enter para cargar el archivo CSV en un dataframe de pandas...")


# Obtenemos la ruta del directorio actual
directorio_actual = os.path.dirname(os.path.abspath(__file__))

# Construimos la ruta al directorio 'dataset' un nivel por encima
ruta_dataset = os.path.join(directorio_actual, '..', 'dataset')
plataforma = "Xbox One"  # Plataforma objetivo en esta fase
df_precios_xbox_one = cargar_archivo_mas_reciente(ruta_dataset, plataforma)
input("\nPresiona Enter para mostrar los primeros registros del dataframe...")

#Cargamos el archivo CSV en un dataframe de pandas
# y Agregamos la categoría 'Xbox One' a los datos
df_precios_xbox_one = agregar_categoria(df_precios_xbox_one, 'Plataforma', 'Xbox One')



###### Inicio de procesamiento de precios xbox-series-x ###################
###########################################################################


# 3. Extracción de datos de precios de videojuegos XBOX SERIES X

# URL base de la página
# Filtramos los enlaces que contengan la palabra "xbox-series-x"
base_url = enlaces_price_charting[enlaces_price_charting['enlaces'].str.contains("xbox-series-x", case=False)]
base_url = base_url['enlaces'].iloc[0] if not base_url.empty else None
print(f"\nURL base de la página de Pricecharting: \n{base_url}")

# Llamamos a la función para descargar los datos
# y guardarlos en un archivo CSV
input("Presiona Enter para iniciar la extracción de datos de precios de videojuegos de XBOX series X...")
precios_xbox_series_x = download_pc(base_url)
input("\nPresiona Enter para tener una muestra de los resultados...")

# Imprimimos los datos de cada videojuego
for juego in precios_xbox_series_x:
    product_id, title, loose_price, cib_price, new_price = juego
    print(f"ID: {product_id}, Título: {title}, Loose: {loose_price}, CIB: {cib_price}, New: {new_price}")

# Accedemos a los datos de un videojuego específico
primer_juego = precios_xbox_series_x[0]
# Accedemos al título del primer juego
print(f"El primer juego es: {primer_juego[1]}")

# Guardamos los datos en un archivo CSV
input("\nPresiona Enter para guardar los datos en un archivo CSV...")


# Llamamos a la función para generar el CSV
generar_csv_precios_v3(
    nombre_archivo='videojuegos.csv', 
    datos=precios_xbox_series_x, 
    nombres_columnas=["ID", "Título", "Loose", "CIB", "New"],
    plataforma="Xbox Series X"
)

# creamos un dataframe de pandas para los juegos de Xbox series X
input("\nPresiona Enter para cargar el archivo CSV en un dataframe de pandas...")


# Obtenemos la ruta del directorio actual
directorio_actual = os.path.dirname(os.path.abspath(__file__))

# Construimos la ruta al directorio 'dataset' un nivel por encima
ruta_dataset = os.path.join(directorio_actual, '..', 'dataset')
plataforma = "Xbox Series X"  # Plataforma objetivo en esta fase
df_precios_xbox_series_x = cargar_archivo_mas_reciente(ruta_dataset, plataforma)
input("\nPresiona Enter para mostrar los primeros registros del dataframe...")
#Cargamos el archivo CSV en un dataframe de pandas
# y Agregamos la categoría 'Xbox Series X' a los datos
df_precios_xbox_series_x = agregar_categoria(df_precios_xbox_series_x, 'Plataforma', 'Xbox Series X')


### Creamos el dataset final con los datos de Xbox One y Xbox Series X ###################
##########################################################################################

# 4. Creación del dataset final con los datos de Xbox One y Xbox Series X
input("\nPresiona Enter para crear el dataset final con los datos de Xbox One y Xbox Series X...")
# Concatenamos los dataframes de Xbox One y Xbox Series X
# para crear un único dataset con todos los datos
# de precios de videojuegos de ambas plataformas
df = pd.concat([df_precios_xbox_one, df_precios_xbox_series_x], ignore_index=True)
# Mostramos los primeros registros del dataset final
print(df.head())

# Guardamos el dataset final en un archivo CSV
df.to_csv(os.path.join(ruta_dataset, 'videojuegos_xbox.csv'), index=False)

# Mostramos los primeros registros del dataset final
input("\nPresiona Enter para mostrar los primeros registros del dataset final...")
print(df.head())

# Mostramos los últimos registros del dataset final
input("\nPresiona Enter para mostrar los últimos registros del dataset final...")
print(df.tail())

# Mostramos un resumen del dataset final
input("\nPresiona Enter para mostrar un resumen del dataset final...")
print(df.info())

# Mostramos un resumen estadístico del dataset final
input("\nPresiona Enter para mostrar un resumen estadístico del dataset final...")
print(df.describe())

# Mostramos la cantidad de registros por plataforma
input("\nPresiona Enter para mostrar la cantidad de registros por plataforma...")
print(df['Plataforma'].value_counts())

# Finalizamos el proceso
print("\nProceso de Web Scraping finalizado con éxito.")
print("Los datos han sido guardados en el archivo 'videojuegos_xbox.csv'.")
print("Gracias por utilizar nuestro programa.")
print("¡Hasta la próxima!\n")
input("Presione Enter para salir...")

# Fin del script



