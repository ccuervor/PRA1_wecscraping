# PRA1_webscraping
# Descripción:
Es el resultado de la primera practica de la asignatura Tipología y ciclo de vida de los datos, en la cual se hace uso de diferentes técnicas de scraping, todo bajo el lenguaje de programación Python, y su librería Scrapy. Así entonces, se obtiene un dataset con información de la página http://www.carroya.com, la cual brinda información de los vehículos en el mercado Colombiano.

# Desarrollado por:
Esta actividad fue desarrollada por Carlos Alfonso Cuervo Rodriguez.

# Ficheros:
El código fue desarrollado bajo la librería Scrapy de Python.
La carpeta webscraping contiene los ficheros: items: que contienen los items que se van a obtener de la página web. settings:indica las condiciones bajo las cuales se va a realizar el crawler. Dentro de esta carpeta se encuentra otra llamada spiders, dentro de la cual está el crawler denominado "carroya".
Así mismo fuera de la carpeta webscraping se encuentra el fichero scrapy.CFG , el cual es necesario al momento de lanzar el spider.
Todos estos archivos deben ser guardados dentro de un mismo repositoria para su correcta ejecución.

# Archivos relacionados:
Dentro de este mismo repositorio se encuentra un archivo en PDF donde se indica: Objetivos del dataset, campos que incluye y contexto. Así mismo, se encuentra el archivo de datos carro.csv dentro de la carpeta webscraping.

# Consideraciones Adicionales:
Como se comentó anteriormente, todos los archivos de la carpeta webscraping y el archivo .CFG deben ser guardados en un mismo repositorio. Así mismo para correr el programa se debe hacer desde consola desde el directorio donde se encuentra el repositorio con todos los archivos descargados: 

$scrapy crawl carroya -o carro.csv -t csv

Con esta instrucción se está indicando que se corra el crawl lladado carroya, que se guarde el resultado en un archivo llamado carro.csv y que el formato del archivo sea csv.
