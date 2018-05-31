from bs4 import BeautifulSoup
import requests
import os
import urllib.request
import urllib3
import re
import csv
import subprocess

class ParserCore:
  """
  При инициализации мы даем наш CSV файл 
  Дальше с помощью функции add_dict_with_brand мы добовляем словарб где ключ юрл сайта,
  а значение список с брендами
  При помощи функции csv_reader мы создаем из полей файла словарь где ключ ссылка сайта на котором искать фотки
  а значение словарь где ключ код товара: значение кортеж(артиклб товара, имя производителя/бренда)

  """

  def __init__(self, file, field_code, field_article, field_producer):
    self.file = file
    self.__test_file()
    self.field_code = field_code
    self.field_article = field_article
    self.field_producer = field_producer
    self.dict_for_download = {}
    self.dicts_data = {}

  def add_dict_with_brand(self, my_dict):
    if type(my_dict) == dict:
      self.dict_with_data = my_dict
      self.csv_reader()





  def csv_reader(self):
    file = open(self.file, 'r')
    reader = csv.reader(file)
    for row in reader:
      for keys, values in self.dict_with_data.items():
        if keys not in  self.dicts_data:
          self.dicts_data[keys] = {}
        for value_in_dict in values:
          brand, value_in_dict = self.__cosmetic(row[self.field_producer], value_in_dict)
          if brand == value_in_dict:
            self.dicts_data[keys].update({row[self.field_code]: (row[self.field_article], row[self.field_producer])})
    return self.dicts_data
           


  def parser_th_tools(self, dict=''):
    if self.dicts_data:
      my_dict =  self.dicts_data['th-tool.by']
      l = 0
      dict_with_url = {}
      for code, value in my_dict.items():
        l += 1
        if l <=10:
          url = requests.get('http://th-tool.by/index.php?route=product/search&search=' + code) # Страница с которого мы будем парсить в конце меняем на нужный нам код
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
                  dict_with_url[href_photo] = (code, value[1])
                except AttributeError as err:
                  continue
      self.dict_for_download = dict_with_url
      return dict_with_url



  def parser_tools(self, dict=''):
    if self.dicts_data:
      my_dict =  self.dicts_data['tools.by']
      l = 0
      dict_with_url = {}
      for code, value in my_dict.items():
        l += 1
        if l < 10:
          url = requests.get('http://www.tools.by/?q=kat&part=1&keys=' + value[0]) # Страница с которого мы будем парсить в конце меняем на нужный нам код
          soup = BeautifulSoup(url.text, 'html.parser')
          try:
            searcher = soup.find('tr', class_='subtitle odd').next_sibling.next_sibling
            searcher = searcher.find('td')
            find_need_data = searcher.find('a', class_='zzoom')
            find_need_data = find_need_data.get('big')
            link = 'http://www.tools.by' + find_need_data
            url = requests.get(link)
            soup = BeautifulSoup(url.text, 'html.parser')
            else_searcher = soup.find('img')
            else_searcher = else_searcher.get('src')
            href_photo = 'http://www.tools.by' + else_searcher
          except AttributeError as err:
            print('Произошла ошибка или нет такого товара вообще: ' + value[0])
            continue
          else:
            dict_with_url[href_photo] = (code, value[1])
      self.dict_for_download = dict_with_url #ссылка на фото: (код товара, артикул)
      return dict_with_url



  def parser_h_d(self, dict=''):   
    if self.dicts_data:
      my_dict =  self.dicts_data['h-d.by']
      l = 0
      dict_with_url = {}
      for code, value in my_dict.items():
        l += 1
        if l < 10:
          url = requests.get('http://h-d.by/buscar?orderby=position&orderway=desc&search_query={}&submit_search='.format(value[0])) # Страница с которого мы будем парсить в конце меняем на нужный нам код
          soup = BeautifulSoup(url.text, 'html.parser')
          try:
            searcher = soup.find('div', class_='center_block')
            searcher = searcher.find('a', class_='product_img_link')
            href_for_big_photo = searcher.get('href')
            url = requests.get(href_for_big_photo)
            soup = BeautifulSoup(url.text, 'html.parser')
            searcher = soup.find('div', class_='image-block').find('img')
            href_photo = searcher.get('src')
          except AttributeError as err:
            print('Произошла ошибка или нет такого товара вообще: ' + value[0])
            continue
          else:
            dict_with_url[href_photo] = (code, value[1])
      self.dict_for_download = dict_with_url
      return dict_with_url




  def download(self, path):
    if self.dict_for_download:
      for link, data in self.dict_for_download.items():
        url = link
        print('download', link, data)
        get_photo = requests.get(link)
        format_photo = url.rsplit('.', maxsplit=1)[-1]
        full_name = data[0] + "." + format_photo
        try:
         file = open(path + full_name, 'wb')
         file.write(get_photo.content)
         file.close()
        except FileNotFoundError as err:
         print(err)
      self.clear_dict_for_download()


  def dowanload_on_server(self):
    """
    Функция непосредственно скачивает фото на сервере
    """
    if self.dict_for_download:
      for link, data in self.dict_for_download.items():
        url = link
        get_photo = requests.get(url)
        format_photo = url.rsplit('.', maxsplit=1)[-1]
        full_name = data[0] + "." + format_photo
        #producer_1 = producer.capitalize()
        """
        Меняем имена так как они указаны с учетом из название в репозитории 
        """
        producer = data[1]
        if producer == 'D&D' or producer == 'd&d':
            producer = 'dandd'
        elif producer == 'Юпитер':
            producer = 'jupiter'
        elif producer == 'Белстаб':
            producer = 'belstub'
        elif producer == 'KingTul kraft':
            producer = 'kingtulkraft'
        elif producer == 'big red':
          producer = 'bigred'
        elif producer == 'KINGTUL profi':
            producer = 'kingtulprofi'
        elif producer == 'ПрофКлей':
            producer = 'profcley'
        elif producer == 'HÖGERT technik':
            producer = 'hogert'
        elif producer == 'ПрофКлей':
          producer = 'profcley' 


        producer_2 = producer.lower()
        producer_2 = producer_2.replace(' ', '')
        print(producer_2 + '_bot' '/' + full_name)
        try:
          file = open('/var/www/opt-online/photos/bot_producer/' + producer_2 + '_bot' '/' + full_name, 'wb')
          file.write(get_photo.content)
          file.close()
        except FileNotFoundError as err:
          print(err)
      self.clear_dict_for_download()



  def work_request(self):
    pass


  def clear_dict_for_download(self):
    self.dict_for_download = {}


  def __test_file(self):
    """Проверяем яляется ли аргумент файлом"""
    if os.path.isfile(self.file):
      with open(self.file, "r") as f_obj:
        pass
    else:
      raise ValueError("Должен быть файл")


  def __cosmetic(self, brand, value):
    brand = brand.lower().replace(' ', '')    
    value = value.lower().replace(' ', '')
    return brand, value             






if __name__ == '__main__':

  dict_with_brands = {
  'h-d.by': ['CYNEL', 'FLO','GAV','GEKO','GERLACH','H-D','JUCO','LUND','LUXI','NORMA','POWER UP','POWERUP','PROWIN',
         'STHOR','TOYA','VOREL','YATO','Zeta','ZMM MAXPOL','Сибиар',],
  'tools.by': ['Строительный Инструмент', 'Fermer', 'Eco', 'Startul', 'Toptul', 'Wortex', 'Solaris', 'Oleo-Mac', 'Fiskars', 
         'Gepard', 'Юпитер', 'Starfix', 'ВОЛАТ', 'Sola', 'Wilo', 'Telwin', 'Slowik', 'Molot'],
  'th-tool.by': ['Авто Инструмент', 'BaumAuto', 'Big Red', 'BRAUMAUTO', 'D&D', 'FORCEKRAFT', 'Forsage', 'Forsage electro', 
         'FORSAGE kids', 'HCB', 'JTC', 'KINGTUL', 'KingTul kraft', 'KINGTUL profi', 'KINGTUL(SK)', 'M7', 'MARSHAL', 'Partner', 'Prowin', 'Rotake']
  }


  # first  = ParserCore('OptOnline.csv', field_code=1, field_producer=2, field_article=3)
  # first.add_dict_with_brand(dict_with_brands)
  # #my_dict =  first.csv_reader()
  # first.parser_th_tools()
  # # for key in my_dict:
  # #     if key == 'th-tool.by':
  # #       first.parser_th_tools(my_dict[key])
  # first.download('./phot/')

  first  = ParserCore('OptOnline.csv', field_code=1, field_producer=2, field_article=3)
  first.add_dict_with_brand(dict_with_brands)
  first.parser_h_d()
  #first.download('./phot/')
  first.dowanload_on_server()
  print(first.dict_for_download)
