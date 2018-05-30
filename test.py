from try_2 import *

# def many_photo(dict, producer):
#        """
#        Ищем фотки ФОРСАЖ ПАРТНЕР КИНГТУЛ
#        """
#        for key, value in dict.items():
#               print(key,value, '---------------------------------')
#               url = requests.get('http://th-tool.by/index.php?route=product/search&search=' + value) # Страница с которого мы будем парсить в конце меняем на нужный нам код
#               soup = BeautifulSoup(url.text, 'html.parser')
#               searcher = soup.find_all('a')
#               #print(searcher)
#               code = key
#               #print(searcher)
#               for i in searcher:
#                      #print('i ' + str(i))
#                      if(i.get('href')):
#                             var = i.get('href').find(code)
#                             #print(var)
#                             if(var >= 0):
#                                    url = requests.get(i.get('href'))  # Страница с которого мы будем парсить в конце меняем на нужный нам код
#                                    soup = BeautifulSoup(url.text, 'html.parser')
#                                    try:
#                                           div = soup.find('div', {'class': 'image'}).next
#                                           href_photo = div.get('href')
#                                           #print('many_photo ' + str(div))
#                                           dowanload(href_photo, code, producer)
#                                    except AttributeError as err:
#                                           #print('нет такого изображение пропускаем  ' + key + value)
#                                           continue






url = requests.get('http://www.tools.by/?q=kat&part=1&keys=BD1015DLi1506') # Страница с которого мы будем парсить в конце меняем на нужный нам код
soup = BeautifulSoup(url.text, 'html.parser')
searcher = soup.find('tr', class_='subtitle odd').find_parent('tbody')
# for i in searcher:
# 	print(i.find('td'))
searcher_2 = soup.find('tr', class_='subtitle odd').next_sibling.next_sibling
searcher_2 = searcher_2.find_all('a', class_='zzoom')
print(searcher_2)


dict_with_brands = {
'h-d.by': ['CYNEL', 'FLO','GAV','GEKO','GERLACH','H-D','JUCO','LUND','LUXI','NORMA','POWER UP','POWERUP','PROWIN',
       'STHOR','TOYA','VOREL','YATO','Zeta','ZMM MAXPOL','Сибиар',],
'tools.by': ['Строительный Инструмент', 'Fermer', 'Eco', 'Startul', 'Toptul', 'Wortex', 'Solaris', 'Oleo-Mac', 'Fiskars', 
       'Gepard', 'Юпитер', 'Starfix', 'ВОЛАТ', 'Sola', 'Wilo', 'Telwin', 'Slowik', 'Molot'],
'th-tool.by': ['Авто Инструмент', 'BaumAuto', 'Big Red', 'BRAUMAUTO', 'D&D', 'FORCEKRAFT', 'Forsage', 'Forsage electro', 
       'FORSAGE kids', 'HCB', 'JTC', 'KINGTUL', 'KingTul kraft', 'KINGTUL profi', 'KINGTUL(SK)', 'M7', 'MARSHAL', 'Partner', 'Prowin', 'Rotake']
}