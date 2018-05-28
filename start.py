from bs4 import BeautifulSoup
import requests
import os
import urllib.request
import urllib3
import re
import csv
import subprocess




def csv_reader(file_obj):
       """
       Создает словарь из CSV где ключ КОД(будет именем фото) а значения АРТИКУЛ(будет указателем для место выгрузки фото)
       """
       reader = csv.reader(file_obj)
       #dict_code_articul = dict()
       for row in reader:
              if(row[2] == 'Yato'): # Отдельный блок потому что мы ято ищем на другом сайте 
                     dict_code_articul = dict()
                     dict_code_articul.update({row[1] : row[3]})
                     producer = row[2]
                     yato(dict_code_articul, producer)
              else:
                     dict_code_articul = dict()
                     dict_code_articul.update({row[1]: row[3]})
                     producer = row[2]
                     many_photo(dict_code_articul, producer)
       #print(dict_code_articul)
       #yato(dict_code_articul)
       #for key, value in dict_code_articul.items():
       #main(dict_code_articul)
       crop_min()
       crop_min_micro()
       print('start.py ЗАКОНЧИЛ СВОЮ РАБОТУ')


def many_photo(dict, producer):
       """
       Ищем фотки ФОРСАЖ ПАРТНЕР КИНГТУЛ
       """
       for key, value in dict.items():
              print(key,value, '---------------------------------')
              url = requests.get('http://th-tool.by/index.php?route=product/search&search=' + value) # Страница с которого мы будем парсить в конце меняем на нужный нам код
              soup = BeautifulSoup(url.text, 'html.parser')
              searcher = soup.find_all('a')
              #print(searcher)
              code = key
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
                                          dowanload(href_photo, code, producer)
                                   except AttributeError as err:
                                          #print('нет такого изображение пропускаем  ' + key + value)
                                          continue
def yato(dict, producer):
       """
       Ищем фотки из сайто YATO
       """
       for key, value in dict.items():

              s = requests.get('http://yato.com/products/12/' + value)
              soup = BeautifulSoup(s.text, 'html.parser')
              #div = soup.find('div', {"class": 'w3-row w3-card-4'})
              div = soup.find('a', {'class': 'chocolat-image'})
              div = div.get('href')
              dowanload(div, key, producer)



def dowanload(data, key, producer):
       """
       Функция непосредственно скачивает фото
       """
       url = data
       get_photo = requests.get(url)
       #format_photo = url.rsplit('.', maxsplit=1)
       #name_photo = format_photo[0].rsplit('/')[-1]
       #full_name = name_photo + "." + format_photo[-1]
       format_photo = url.rsplit('.', maxsplit=1)[-1]
       full_name = key + "." + format_photo
       producer_1 = producer.capitalize()
       """
       Меняем имена так как они указаны с учетом из название в репозитории 
       """
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
              #file = open('./test/' + full_name, 'wb')
              #file = open('./Yato_img/' + full_name, 'wb')
              file.write(get_photo.content)
              #print(data, key,)
              file.close()
              
       except FileNotFoundError as err:
              print(err)
              

def crop_min():
       print('crop_min я начал работу')
       list_photo = ['baumauto', 'belstub', 'bigred', 'braumauto', 
                     'dandd', 'forcekraft', 'forsage', 'forsageelectro', 
                     'geko', 'groz', 'gtv', 'h-d', 'hammer', 'hcb', 'hogert', 
                     'jupiter', 'kingtul', 'kingtulkraft', 'kingtulprofi', 'krino', 
                     'luxi', 'm7', 'marshal', 'partner', 'profcley', 'prowin', 'rotake', 
                     'selta', 'telwin', 'wortex', 'yato']

       for producer in list_photo:
              subprocess.call(["bash", "/var/www/opt-online/sh/crop_for_min.sh", producer])


def crop_min_micro():
       print('crop_min_micro я начал работу')
       list_photo = ['baumauto', 'belstub', 'bigred', 'braumauto', 
                     'dandd', 'forcekraft', 'forsage', 'forsageelectro', 
                     'geko', 'groz', 'gtv', 'h-d', 'hammer', 'hcb', 'hogert', 
                     'jupiter', 'kingtul', 'kingtulkraft', 'kingtulprofi', 'krino', 
                     'luxi', 'm7', 'marshal', 'partner', 'profcley', 'prowin', 'rotake', 
                     'selta', 'telwin', 'wortex', 'yato']

       for producer in list_photo:
              subprocess.call(["bash", "/var/www/opt-online/sh/crop_for_min_micro.sh", producer])

"""
def main():
       html = open('yato.html').read()
       soup = BeautifulSoup(html, 'lxml')
       div = soup.find('input', {'id': 'search_index'})
       #div = soup.find_all('img', src=re.compile('stopka'))
       div = soup.find('div', class_='item')
       print(div)
       for i in div:
              path = i#.get('src')
              print(path)
"""

if __name__ == '__main__':
       csv_path = "opt_clear.csv"
       with open(csv_path, "r") as f_obj:
              csv_reader(f_obj)
