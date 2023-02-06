from pydoc import doc
import ssl
import requests
from bs4 import BeautifulSoup as bs
import csv
import time
import random
import pymysql
import re
import unidecode
from config import site, type, location, find, headers, host, user, password, db_name, table_existing


'''Функция принимает на вход относительную дату из объявления 
и возвращает значение float суток с момента публикации'''

def dateintodays(date):
    result = re.findall(r'\d+', date)[0]
    #print(result)
    if re.search(r'часов|часа|час', date) is not None:
        result_hrs = int(result)
    elif re.search(r'дней|дня|день', date) is not None:
            result_hrs = int(result) * 24
    elif re.search(r'неделю|недели|недель', date) is not None:
        result_hrs = int(result) * 7 * 24
    else:
        result_hrs = 30*24
    result_days = (result_hrs/24.)

    return result_days





'''Настраиваем версию TLS на 1.1'''

from requests.adapters import HTTPAdapter
from requests.packages.urllib3.poolmanager import PoolManager
from requests.packages.urllib3.util import ssl_

CIPHERS = """ECDHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-SHA384:ECDHE-ECDSA-AES256-SHA384:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-RSA-AES128-SHA256:AES256-SHA"""

class TlsAdapter(HTTPAdapter):

    def __init__(self, ssl_options=0, **kwargs):
        self.ssl_options = ssl_options
        super(TlsAdapter, self).__init__(**kwargs)

    def init_poolmanager(self, *pool_args, **pool_kwargs):
        ctx = ssl_.create_urllib3_context(ciphers=CIPHERS, cert_reqs=ssl.CERT_REQUIRED, options=self.ssl_options)
        self.poolmanager = PoolManager(*pool_args, ssl_context=ctx, **pool_kwargs)

session = requests.session()
adapter = TlsAdapter(ssl.OP_NO_TLSv1 | ssl.OP_NO_TLSv1_1)
session.mount("https://", adapter)


'''В одной итерации цикла происходит открытие страницы через Get-запрос, сохранение страницы в локальный файл, 
парсинг объявлений из файла страницы, сохранение параметров объявления в перемнные и запись данных в csv файл для каждого найденного объявления
'''


#Подключаемся к MySQL СУБД

try:
    connection = pymysql.connect(
        host=host,
        port=3306,
        user=user,
        password=password,
        database=db_name,
        cursorclass=pymysql.cursors.DictCursor)
    print("Successfully connected...")
except Exception as ex:
    print("Connection refused...", ex)



'''Открываем нужную страницу, парсим данные и сразу же записываем их в файл'''

page = 0 
ad_counter = 0 
do = True

while do:

    page = page + 1
    URL = site + location + type + "?p=" + str(page) + find
    

    r = session.get(URL, headers=headers) #Делаем первый запрос, получаем статус ответа и куки

    #Проверка на статус код
    if (r.status_code >= 200 and r.status_code <= 300):
         print(f"\nGo ahead. Status code: {r.status_code}\n ")
    else: 
        print(f"Problem. Stastus code: {r.status_code} ")  
        exit('Exit code: 2')


    #Сохраняем код URL-страницы в переменную и в файл index.html
        
    src = r.text
    with open('index.html', mode='w', encoding='utf-8') as file: 
        file.write(r.text)
    
    '''Начинаем парсинг файла'''

    soup = bs(src, 'lxml')



    #Находим все объявления на странице и сохраняем их в переменную (внутри переменной все еще объект класса soup)

    all_items = soup.find( 'div', class_='items-items-kAJAg').find_all('div', class_='iva-item-root-_lk9K photo-slider-slider-S15A_ iva-item-list-rfgcH iva-item-redesign-rop6P iva-item-responsive-_lbhG items-item-My3ih items-listItem-Gd1jN js-catalog-item-enum')
    ad_counter = ad_counter + len(all_items)
    print(URL)
    print("Спрасено ", len(all_items), " объявлений")

    

    

    #Для каждого найденного объявления парсим набор параметров, сохраняем их в переменные и записываем в csv файл
    try: 
        for item in all_items: 
            item_name = item.find('h3', class_="title-root-zZCwT iva-item-title-py3i_ title-listRedesign-_rejR title-root_maxHeight-X6PsH text-text-LurtD text-size-s-BxGpL text-bold-SinUO").text
            item_descrip = item.find('div', class_='iva-item-text-Ge6dR iva-item-description-FDgK4 text-text-LurtD text-size-s-BxGpL').text
            item_price = item.find('span', class_='price-text-_YGDY text-text-LurtD text-size-s-BxGpL').text
            item_URL = site + item.find('a', class_='iva-item-sliderLink-uLz1v').get('href')
            item_date = (item.find('div', class_='date-text-KmWDf text-text-LurtD text-size-s-BxGpL text-color-noaccent-P1Rfs')).text
            item_id = item.get('data-item-id')
                
            
            #Форматируем некоторые перменные в удобный формат
            
            item_id = int(item_id)
            
            # def priceintodigit(price):
            #     price = (unidecode.unidecode(price))
            #     if price == 'Tsenaneukazana'
                    

            item_price = int(((unidecode.unidecode(item_price)).replace(" ", "")).strip("R"))
            item_date = dateintodays(item_date)

            #Функция принимает на вход относительную дату из объявления и возвращает значение float сутки с момента публикации



            #Сохранение результатов парсинга в csv
            
            with open('db.csv', 'a', encoding='utf-8', newline='') as file:
                writer = csv.writer(file)
                writer.writerow((item_id, item_name, item_price, item_URL, item_date, item_descrip))

            #Сохрание результатов парсинга в sql-файл на сервер

            with connection.cursor() as cursor:
                if table_existing == False:
                    create_table_query = "CREATE TABLE notebook(id int (24) NOT NULL PRIMARY KEY, \
                                                                name varchar(64), \
                                                                price varchar(12), \
                                                                url varchar(128));"
                    #cursor.execute(create_table_query)
                    table_existing = True
                    print("Table was created.")
                
                #create_row_query = f"INSERT INTO ad (id, name, price, url) VALUES ({item_id}, 'MacBook Pro', 50000, 'https://avito.ru');)
                
            
                
                

                    
                    
                    



      
    finally:
        connection.close() #Отключаемся от СУБД

        
        
        
        
   
    
    #Если на странице меньше 50 объявлений, то цикл завершается
    if len(all_items) < 50:

        print('\nЭта страница была последней. ')
        do = False
        break

    #Задержка между циклами
    rand = random.randint(3,10) 
    print('Сон:', rand, ' секунд.')
    time.sleep(rand)
    
print("Всего объявлений спарсено", str(ad_counter))
exit('Exit code: 0')





