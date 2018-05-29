from bs4 import BeautifulSoup
import requests
import os
import urllib.request
import urllib3
import re
import csv
import subprocess

class ParserCore:


       def __init__(self, file):
           self.file = file
           self.__test_file()
           self.dict_with_brands = {
              'h-d.by': ['CYNEL', 'FLO','GAV','GEKO','GERLACH','H-D','JUCO','LUND','LUXI','NORMA','POWER UP','POWERUP','PROWIN',
                     'STHOR','TOYA','VOREL','YATO','Zeta','ZMM MAXPOL','Сибиар',],
              'tools.by': ['Строительный Инструмент', 'Fermer', 'Eco', 'Startul', 'Toptul', 'Wortex', 'Solaris', 'Oleo-Mac', 'Fiskars', 
                     'Gepard', 'Юпитер', 'Starfix', 'ВОЛАТ', 'Sola', 'Wilo', 'Telwin', 'Slowik', 'Molot'],
              'th-tool.by': ['Авто Инструмент', 'BaumAuto', 'Big Red', 'BRAUMAUTO', 'D&D', 'FORCEKRAFT', 'Forsage', 'Forsage electro', 
                     'FORSAGE kids', 'HCB', 'JTC', 'KINGTUL', 'KingTul kraft', 'KINGTUL profi', 'KINGTUL(SK)', 'M7', 'MARSHAL', 'Partner', 'Prowin', 'Rotake']
              }




       def csv_reader(self):
              file = open('OptOnline.csv', 'r')
              reader = csv.reader(file)
              for row in reader:
                  for keys, values in self.dict_with_brands.items():
                      for value in values:
                          brand, value = self.__cosmetic(row[2], value)
                          if brand == value:
                              self.searcher(keys, row[1], row[3])


       def searcher(self, site, code, article):
              if site == 'th-tool.by':
                     url = requests.get('http://th-tool.by/index.php?route=product/search&search=' + code)
                     soup = BeautifulSoup(url.text, 'html.parser')
                     searcher = soup.find_all('a')
                     for i in searcher:
                            if(i.get('href')):
                                   var = i.get('href').find(code)
                                   if(var >= 0):
                                          url = requests.get(i.get('href'))  # Страница с которого мы будем парсить в конце меняем на нужный нам код
                                          soup = BeautifulSoup(url.text, 'html.parser')
                                          try:
                                                 div = soup.find('div', {'class': 'image'}).next
                                                 href_photo = div.get('href')
                                                 print(href_photo)
                                                 #dowanload(href_photo, code, producer)
                                          except AttributeError as err:
                                                 #print('нет такого изображение пропускаем  ' + key + value)
                                                 continue
                     





       def add_brands(self, brands, site):
              self.dict_with_brands[site].append(brands)


       def __test_file(self):
              """Проверяем яляется ли аргумент файлом"""
              if os.path.isfile(self.file):
                     with open(self.file, "r") as f_obj:
                            pass
              else:
                     raise ValueError("Должен быть файл")


       def __cosmetic(self, brand, value):
              self.brand = brand.lower().replace(' ', '')    
              self.value = value.lower().replace(' ', '')
              return self.brand, self.value             


a  = ParserCore('OptOnline.csv')

a.csv_reader()