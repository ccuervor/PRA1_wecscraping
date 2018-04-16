# -*- coding: utf-8 -*-
import scrapy
import lxml.html
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from webscraping.items import WebscrapingItem

class CarroyaSpider(CrawlSpider):
      name = 'carroya'
      start_urls = ['http://carroya.com/buscar/vehiculos/t4e2d5c1.do?']
      allowed_domains = ['carroya.com']
      
      rules = (
              Rule(LinkExtractor(allow= 'paginaActua=\d',),follow=True),
              Rule(LinkExtractor(allow='/vehiculo/nuevoficha/'), callback='parse_item')
              )
    
      def parse_item(self, response):
         item = WebscrapingItem()
         precio_css = 'span.text-primary::text'
         item['precio']= response.css(precio_css).extract()
          
         nombre_css = 'h1::text'
         item['nombre']= response.css(nombre_css).extract()
            
         refer_css = 'div.col-xs-12.col-sm-5.car-name > h2::text'
         item['referencia']= response.css(refer_css).extract()
         
         lugar_css = response.xpath('//*[@id="specs"]/ul/li[2]/div/text()').extract()
         lugar_css = lugar_css[-1]
         item['lugar'] = lugar_css
            
         puer_css = response.xpath('//*[@id="specs"]/ul/li[4]/div/text()').extract()
         puer_css = puer_css[0].replace('\n','').replace('\t','')
         item['puertas']= puer_css
            
         dir_css= response.xpath('//*[@id="specs"]/ul/li[5]/div/text()').extract()
         dir_css = dir_css[0].replace('\n','').replace('\t','')
         item['direccion']= dir_css 
            
         tcaja_css= response.xpath('//*[@id="specs"]/ul/li[6]/div/text()').extract()
         tcaja_css= tcaja_css[0].replace('\n','').replace('\t','')
         item['tipocaja']= tcaja_css 
            
         comb_css= response.xpath('//*[@id="specs"]/ul/li[7]/div/text()').extract()
         comb_css= comb_css[0].replace('\n','').replace('\t','')
         item['combustible']= comb_css 
            
         return item


