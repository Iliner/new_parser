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






# url = requests.get('http://www.tools.by/?q=kat&part=1&keys=BD1015DLi1506') # Страница с которого мы будем парсить в конце меняем на нужный нам код
# soup = BeautifulSoup(url.text, 'html.parser')
# # searcher = soup.find('tr', class_='subtitle odd').find_parent('tbody')
# # for i in searcher:
# # 	print(i.find('td'))
# searcher_2 = soup.find('tr', class_='subtitle odd').next_sibling.next_sibling
# searcher_2 = searcher_2.find('td')
# find_need_data = searcher_2.find('a', class_='zzoom')
# find_need_data = find_need_data.get('big')

# #reg_2 = re.search(r"big=([\"'])(.*?)\1", find_need_data)
# link = 'http://www.tools.by' + find_need_data

# url = requests.get(link)
# soup = BeautifulSoup(url.text, 'html.parser')
# searcher_3 = soup.find('img')
# searcher_3 = searcher_3.get('src')
# url = 'http://www.tools.by' + searcher_3






# get_photo = requests.get(url)
# #format_photo = url.rsplit('.', maxsplit=1)
# #name_photo = format_photo[0].rsplit('/')[-1]
# #full_name = name_photo + "." + format_photo[-1]
# format_photo = url.rsplit('.', maxsplit=1)[-1]
# full_name = 'aaaaa' + "." + format_photo
# try:
#  file = open('./photos/' + full_name, 'wb')
#  #file = open('./test/' + full_name, 'wb')
#  #file = open('./Yato_img/' + full_name, 'wb')
#  file.write(get_photo.content)
#  #print(data, key,)
#  file.close()
# except FileNotFoundError as err:
#  print(err)



# dict_with_brands = {
# 'h-d.by': ['CYNEL', 'FLO','GAV','GEKO','GERLACH','H-D','JUCO','LUND','LUXI','NORMA','POWER UP','POWERUP','PROWIN',
#        'STHOR','TOYA','VOREL','YATO','Zeta','ZMM MAXPOL','Сибиар',],
# 'tools.by': ['Строительный Инструмент', 'Fermer', 'Eco', 'Startul', 'Toptul', 'Wortex', 'Solaris', 'Oleo-Mac', 'Fiskars', 
#        'Gepard', 'Юпитер', 'Starfix', 'ВОЛАТ', 'Sola', 'Wilo', 'Telwin', 'Slowik', 'Molot'],
# 'th-tool.by': ['Авто Инструмент', 'BaumAuto', 'Big Red', 'BRAUMAUTO', 'D&D', 'FORCEKRAFT', 'Forsage', 'Forsage electro', 
#        'FORSAGE kids', 'HCB', 'JTC', 'KINGTUL', 'KingTul kraft', 'KINGTUL profi', 'KINGTUL(SK)', 'M7', 'MARSHAL', 'Partner', 'Prowin', 'Rotake']
# }

# a = """[<a big="/product/zoompic_preview&amp;id=915069.jpg" class="/zzoom" href="javascript:void(0)" title="Аккум. дрель-шуруповерт WORTEX BD 1015 DLi в чем.'qweqw' (10.8 В, 2 акк., 1.5 А/ч Li-Ion, 2 скор., 25 Нм, шурупы до 6 мм)"><img class="lazyload" data-src="/newkatfiles/small/915069.jpg" height="60px" onclick="zoom_picture_new(915069,0)" src="/misc/o.gif" title="Аккум. дрель-шуруповерт WORTEX BD 1015 DLi в чем. (10.8 В, 2 акк., 1.5 А/ч Li-Ion, 2 скор., 25 Нм, шурупы до 6 мм)" width="80px"/></a>]
# <_sre.SRE_Match object; span=(4, 8), match='big='>qweq@mail.ru
# """
# reg = re.search(r"<a\s+(?:[^>]*?\s+)?big=([\"'])(.*?)\1", a)
# reg_2 = re.search(r"big=([\"'])(.*?)\1", a)
# print(reg_2.group(2))


url = requests.get('http://h-d.by/buscar?orderby=position&orderway=desc&search_query=YT-0185&submit_search=')
soup = BeautifulSoup(url.text, 'html.parser')
searcher = soup.find('div', class_='center_block')
searcher = searcher.find('a', class_='product_img_link')
href_for_big_photo = searcher.get('href')

url = requests.get(href_for_big_photo)
soup = BeautifulSoup(url.text, 'html.parser')
searcher = soup.find('div', class_='image-block').find('img')
url = searcher.get('src')


get_photo = requests.get(url)
#format_photo = url.rsplit('.', maxsplit=1)
#name_photo = format_photo[0].rsplit('/')[-1]
#full_name = name_photo + "." + format_photo[-1]
format_photo = url.rsplit('.', maxsplit=1)[-1]
full_name = 'aaaaa' + "." + format_photo
try:
 file = open('./phot/' + full_name, 'wb')
 #file = open('./test/' + full_name, 'wb')
 #file = open('./Yato_img/' + full_name, 'wb')
 file.write(get_photo.content)
 #print(data, key,)
 file.close()
except FileNotFoundError as err:
 print(err)
