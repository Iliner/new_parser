from bs4 import BeautifulSoup
import requests
import os
import urllib.request
import urllib3
import re
import csv
import subprocess

class ParserCore:


  def __init__(self, file, field_code, field_article):
    self.file = file
    self.__test_file()
    self.field_code = field_code
    self.field_article = field_article

  def add_dict(self, my_dict):
    if type(my_dict) == dict:
      self.dict_with_data = my_dict


  def run_equal_data(self):
    pass

  def csv_reader(self):
    file = open(self.file, 'r')
    reader = csv.reader(file)
    for row in reader:
      for keys, values in self.dict_with_data.items():
        for value in values:
          brand, value = self.__cosmetic(row[2], value)
          if brand == value:
            print((keys, row[1], row[3]))
  






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













  # def csv_reader(self):
  #   file = open('OptOnline.csv', 'r')
  #   reader = csv.reader(file)
  #   for row in reader:
  #     for keys, values in self.dict_with_brands.items():
  #       for value in values:
  #         brand, value = self.__cosmetic(row[2], value)
  #         if brand == value:
  #           print((keys, row[1], row[3]))









dict_with_brands = {
'h-d.by': ['CYNEL', 'FLO','GAV','GEKO','GERLACH','H-D','JUCO','LUND','LUXI','NORMA','POWER UP','POWERUP','PROWIN',
       'STHOR','TOYA','VOREL','YATO','Zeta','ZMM MAXPOL','Сибиар',],
'tools.by': ['Строительный Инструмент', 'Fermer', 'Eco', 'Startul', 'Toptul', 'Wortex', 'Solaris', 'Oleo-Mac', 'Fiskars', 
       'Gepard', 'Юпитер', 'Starfix', 'ВОЛАТ', 'Sola', 'Wilo', 'Telwin', 'Slowik', 'Molot'],
'th-tool.by': ['Авто Инструмент', 'BaumAuto', 'Big Red', 'BRAUMAUTO', 'D&D', 'FORCEKRAFT', 'Forsage', 'Forsage electro', 
       'FORSAGE kids', 'HCB', 'JTC', 'KINGTUL', 'KingTul kraft', 'KINGTUL profi', 'KINGTUL(SK)', 'M7', 'MARSHAL', 'Partner', 'Prowin', 'Rotake']
}


first  = ParserCore('OptOnline.csv', field_code=1, field_article=3)
first.add_dict(dict_with_brands)
first.csv_reader()

