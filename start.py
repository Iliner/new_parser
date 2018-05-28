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
              'h-d.by': ['CYNEL', 'FLO','GAV','GEKO','GERLACH','H-D','JUCO','LUND','LUXI','NORMA','POWER UP','POWERUP','PROWIN','STHOR','TOYA','VOREL','YATO','Zeta','ZMM MAXPOL','Сибиар',],
              'Tools.by': ['Строительный Инструмент', 'Fermer', 'Eco', 'Startul', 'Toptul', 'Wortex', 'Solaris', 'Oleo-Mac', 'Fiskars', 'Gepard', 'Юпитер', 'Starfix', 'ВОЛАТ', 'Sola', 'Wilo', 'Telwin', 'Slowik', 'Molot']
              'th-tool.by': ['Авто Инструмент','BaumAuto','Big Red','BRAUMAUTO','D&D','FORCEKRAFT','Forsage','Forsage electro','FORSAGE kids','HCB','JTC','KINGTUL','KingTul kraft','KINGTUL profi','KINGTUL(SK)','M7','MARSHAL','Partner','Prowin','Rotake']
              }

       def __init__(self, file):
           self.file = file
           self.__test_file()


       def __test_file(self):
              """Проверяем яляется ли аргумент файлом"""
           if os.path.isfile(self.file):
              with open(self.file, "r") as f_obj:
                     
           else:
              raise ValueError("Должен быть файл")

       def read_csv(self):
          

       def hd_by(self):


       def csv_reader(file_obj):
              """
              Создает словарь из CSV где ключ КОД(будет именем фото) а значения АРТИКУЛ(будет указателем для место выгрузки фото)
              """
              reader = csv.reader(file_obj)
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
              crop_min()
              crop_min_micro()
              print('start.py ЗАКОНЧИЛ СВОЮ РАБОТУ')


a  = ParserCore('OptOnline.csv')




# {
# 'h-d.by': ['CYNEL', 'FLO','GAV','GEKO','GERLACH','H-D','JUCO','LUND','LUXI','NORMA','POWER UP','POWERUP','PROWIN','STHOR','TOYA','VOREL','YATO','Zeta','ZMM MAXPOL','Сибиар',],
# 'Tools.by': ['Строительный Инструмент', 'Fermer', 'Eco', 'Startul', 'Toptul', 'Wortex', 'Solaris', 'Oleo-Mac', 'Fiskars', 'Gepard', 'Юпитер', 'Starfix', 'ВОЛАТ', 'Sola', 'Wilo', 'Telwin', 'Slowik', 'Molot']
# 'th-tool.by': ['Авто Инструмент','BaumAuto','Big Red','BRAUMAUTO','D&D','FORCEKRAFT','Forsage','Forsage electro','FORSAGE kids','HCB','JTC','KINGTUL','KingTul kraft','KINGTUL profi','KINGTUL(SK)','M7','MARSHAL','Partner','Prowin','Rotake']
# }
