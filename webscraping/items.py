# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class WebscrapingItem(scrapy.Item):
     precio = scrapy.Field()
     nombre = scrapy.Field()
     referencia = scrapy.Field()
     lugar = scrapy.Field()
     puertas = scrapy.Field()
     direccion = scrapy.Field()
     tipocaja = scrapy.Field()
     combustible = scrapy.Field()
     
     
     
