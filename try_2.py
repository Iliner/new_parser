from bs4 import BeautifulSoup
import requests
import os
import urllib.request
import urllib3
import re
import csv
import subprocess

class ParserCore:


  def __init__(self, file, field_code, field_article, field_producer):
    self.file = file
    self.__test_file()
    self.field_code = field_code
    self.field_article = field_article
    self.field_producer = field_producer
    self.dict_for_download = {}
  def add_dict(self, my_dict):
    if type(my_dict) == dict:
      self.dict_with_data = my_dict


  def run_equal_data(self):
    pass

  def csv_reader(self):
    file = open(self.file, 'r')
    reader = csv.reader(file)
    dicts_data = {}
    for row in reader:
      for keys, values in self.dict_with_data.items():
        if keys not in  dicts_data:
          dicts_data[keys] = {}
        for value_in_dict in values:
          brand, value_in_dict = self.__cosmetic(row[self.field_producer], value_in_dict)
          if brand == value_in_dict:
            dicts_data[keys].update({row[self.field_code]: (row[self.field_article], row[self.field_producer])})
    return dicts_data
           


  def parser_ph_tools(self, dict):
    l = 0
    dict_with_url = {}
    for code, value in dict.items():
      l += 1
      if l <=10:
        #print(key,value, '---------------------------------')
        url = requests.get('http://th-tool.by/index.php?route=product/search&search=' + code) # Страница с которого мы будем парсить в конце меняем на нужный нам код
        soup = BeautifulSoup(url.text, 'html.parser')
        searcher = soup.find_all('a')
        #print(searcher)
        #print(searcher)
        for i in searcher:
          #print('i ' + str(i))
          if(i.get('href')):
            var = i.get('href').find(code)
            #print(var)
            if(var >= 0):
              url = requests.get(i.get('href'))  # Страница с которого мы будем парсить в конце меняем на нужный нам код
              soup = BeautifulSoup(url.text, 'html.parser')
              try:
                div = soup.find('div', {'class': 'image'}).next
                href_photo = div.get('href')
                #print('many_photo ' + str(div))
                # print(dict_with_url)
                # print(href_photo, code, value[1])
                dict_with_url[href_photo] = (code, value[1])
              except AttributeError as err:
                #print('нет такого изображение пропускаем  ' + key + value)
                continue
    self.dict_for_download = dict_with_url
    return dict_with_url



  def parser_ph_tools(self, dict):
    l = 0
    dict_with_url = {}
    for code, value in dict.items():
      l += 1
      if l <=10:
        #print(key,value, '---------------------------------')
        url = requests.get('http://th-tool.by/index.php?route=product/search&search=' + code) # Страница с которого мы будем парсить в конце меняем на нужный нам код
        soup = BeautifulSoup(url.text, 'html.parser')
        searcher = soup.find_all('a')
        #print(searcher)
        #print(searcher)
        for i in searcher:
          #print('i ' + str(i))
          if(i.get('href')):
            var = i.get('href').find(code)
            #print(var)
            if(var >= 0):
              url = requests.get(i.get('href'))  # Страница с которого мы будем парсить в конце меняем на нужный нам код
              soup = BeautifulSoup(url.text, 'html.parser')
              try:
                div = soup.find('div', {'class': 'image'}).next
                href_photo = div.get('href')
                #print('many_photo ' + str(div))
                # print(dict_with_url)
                # print(href_photo, code, value[1])
                dict_with_url[href_photo] = (code, value[1])
              except AttributeError as err:
                #print('нет такого изображение пропускаем  ' + key + value)
                continue
    self.dict_for_download = dict_with_url
    return dict_with_url


  def download(self):
    if self.dict_for_download:
      for link, data in self.dict_for_download.items():
        url = link
        get_photo = requests.get(link)
        #format_photo = url.rsplit('.', maxsplit=1)
        #name_photo = format_photo[0].rsplit('/')[-1]
        #full_name = name_photo + "." + format_photo[-1]
        format_photo = url.rsplit('.', maxsplit=1)[-1]
        full_name = data[0] + "." + format_photo
        try:
         file = open('./photos/' + full_name, 'wb')
         #file = open('./test/' + full_name, 'wb')
         #file = open('./Yato_img/' + full_name, 'wb')
         file.write(get_photo.content)
         #print(data, key,)
         file.close()
        except FileNotFoundError as err:
         print(err)




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


# first  = ParserCore('OptOnline.csv', field_code=1, field_producer=2, field_article=3)
# first.add_dict(dict_with_brands)
# my_dict =  first.csv_reader()
# # for key in my_dict:
# #     if key == 'th-tool.by':
# #       first.parser_ph_tools(my_dict[key])

# # first.download()

# for key in my_dict:
#   if key == 'tools.by':
#     print(my_dict[key])
