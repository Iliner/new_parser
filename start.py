from bs4 import BeautifulSoup
import requests
import os
import urllib.request
import urllib3
import re
import csv
import subprocess

class ParserCore:
       dict_with_brands = {
              'h-d.by': ['CYNEL', 'FLO','GAV','GEKO','GERLACH','H-D','JUCO','LUND','LUXI','NORMA','POWER UP','POWERUP','PROWIN',
                     'STHOR','TOYA','VOREL','YATO','Zeta','ZMM MAXPOL','Сибиар',],
              'Tools.by': ['Строительный Инструмент', 'Fermer', 'Eco', 'Startul', 'Toptul', 'Wortex', 'Solaris', 'Oleo-Mac', 'Fiskars', 
                     'Gepard', 'Юпитер', 'Starfix', 'ВОЛАТ', 'Sola', 'Wilo', 'Telwin', 'Slowik', 'Molot'],
              'th-tool.by': ['Авто Инструмент', 'BaumAuto', 'Big Red', 'BRAUMAUTO', 'D&D', 'FORCEKRAFT', 'Forsage', 'Forsage electro', 
                     'FORSAGE kids', 'HCB', 'JTC', 'KINGTUL', 'KingTul kraft', 'KINGTUL profi', 'KINGTUL(SK)', 'M7', 'MARSHAL', 'Partner', 'Prowin', 'Rotake']
              }

       def __init__(self, file):
           self.file = file
           self.__test_file()


       def __test_file(self):
              """Проверяем яляется ли аргумент файлом"""
              if os.path.isfile(self.file):
                     with open(self.file, "r") as f_obj:
                            self.csv_reader(f_obj)
              else:
                     raise ValueError("Должен быть файл")


       def __cosmetic(self, brand, value):
              self.brand = brand.lower().replace(' ', '')    
              self.value = value.lower().replace(' ', '')
              return self.brand, self.value      


       def csv_reader(self, file_obj):
              file = open('OptOnline.csv', 'r')
              reader = csv.reader(file)
              a = 0
              for row in reader:
                  a+= 1
                  for keys, values in self.dict_with_brands.items():
                      for value in values:
                          brand, value = self.__cosmetic(row[2], value)
                          if brand == value:
                              self.searcher(keys, )

       def searcher(self, url, article='', code=''):
              pass

a  = ParserCore('OptOnline.csv')


# dict_with_brands = {
#        'h-d.by': ['CYNEL', 'FLO','GAV','GEKO','GERLACH','H-D','JUCO','LUND','LUXI','NORMA','POWER UP','POWERUP','PROWIN',
#               'STHOR','TOYA','VOREL','YATO','Zeta','ZMM MAXPOL','Сибиар',],
#        'Tools.by': ['Строительный Инструмент', 'Fermer', 'Eco', 'Startul', 'Toptul', 'Wortex', 'Solaris', 'Oleo-Mac', 'Fiskars', 
#               'Gepard', 'Юпитер', 'Starfix', 'ВОЛАТ', 'Sola', 'Wilo', 'Telwin', 'Slowik', 'Molot'],
#        'th-tool.by': ['Авто Инструмент', 'BaumAuto', 'Big Red', 'BRAUMAUTO', 'D&D', 'FORCEKRAFT', 'Forsage', 'Forsage electro', 
#               'FORSAGE kids', 'HCB', 'JTC', 'KINGTUL', 'KingTul kraft', 'KINGTUL profi', 'KINGTUL(SK)', 'M7', 'MARSHAL', 'Partner', 'Prowin', 'Rotake']
#        }

# file = open('OptOnline.csv', 'r')
# reader = csv.reader(file)
# a = 0
# for row in reader:
#     a+= 1
#     for keys, values in dict_with_brands.items():
#         for value in values:
#             if row[2].lower() == value.lower():
            
#       