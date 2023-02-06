
#Задаем URL-запрос

site = "https://www.avito.ru"
type = { 
    'Ноутбуки':'/noutbuki'
    }
location = {
    'Томск':'/tomsk',
    'Россия':'/all'
    }

type = type['Ноутбуки']
location = location['Россия']
find = "huawei matebook d16"

find = "&" + "q=" + (find.replace(' ','+'))


#Задаем параметры Get-запроса

headers = { "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36", 
            #"cookie": 'u=2tedhhyd.1d2cwl4.1rsz1hk8i2a00; sessid=3dc7e78493a51818680c3400cbb27569.1658733522; auth=1; buyer_laas_location=657600; abp=1; _gcl_au=1.1.1162982076.1660461749; _ym_uid=1660461750612073614; _ym_d=1660461750; tmr_lvid=d74a454f0780586fa3d240973bf39380; tmr_lvidTS=1660461750604; isCriteoSetNew=true; uxs_uid=667d8380-1d34-11ed-aa2c-61948ab34ad5; buyer_location_id=657600; SEARCH_HISTORY_IDS=3; _ym_isad=1; _gid=GA1.2.752077050.1662627609; f=5.32e32548b6f3e9782d6059f4e9572c014766c9e25d58fb374766c9e25d58fb374766c9e25d58fb374766c9e25d58fb37c631bbfde7e663b8c631bbfde7e663b8c631bbfde7e663b84766c9e25d58fb37357212485bdbc72734bd85fe5e85ba0346b8ae4e81acb9fa143114829cf33ca746b8ae4e81acb9fa46b8ae4e81acb9fae992ad2cc54b8aa8b175a5db148b56e92157fc552fc06411bc8794f0f6ce82fe915ac1de0d034112dc0d86d9e44006d8143114829cf33ca7143114829cf33ca724a135baa76198de46b8ae4e81acb9fad99271d186dc1cd0b5b87f59517a23f2c772035eab81f5e1c772035eab81f5e13de19da9ed218fe2c772035eab81f5e1143114829cf33ca7c8d9f279052cbd849568c32d8411f4f681997d94b754993e801105b5e0cdcab4d4d0ede10d5348f437863d73204ac56651a6daea57ca21e03ef1ddc4a804b4c8b363bef06738d0cb97292ca0d01dc1c1c772035eab81f5e146b8ae4e81acb9fa46b8ae4e81acb9faf5b8e78c6f0f62a3800d4f69bbc0d90a22aacb07d5f519512da10fb74cac1eab2da10fb74cac1eabc98d1c3ab1f148dc193cc3161054d47da6ef565a9fc26059; ft="h67cS/zWbJwoLTaTXu7LDEWfLDI4jc7m8YwRu3w4h+P/gMbT6XeD0qQUZneHapghPus7/L0nPRGJnm19MMKypWsjjIBZ8ne7TCyM9V8c/tB2pXYqRzjanVqXIwH+d2LoRY/fQ9bDY5lAPGprznNZTviDmCw5yra3I5L70ePrNAt3cwSwndJLLjKvQvUp4Hwt"; v=1662629861; dfp_group=33; isLegalPerson=0; _ym_visorc=b; luri=tomsk; sx=H4sIAAAAAAAC%2F1TMQZaCMAwA0LtkzaLQkFJuM5PWIAVTgUdRHnd35cIL%2FBOIiDg4unnyLSH56P6j9cG1htkFD%2F0JO%2FQwHq%2BFj5D%2BZHLPJuXpzcNWYpvmmO38gAoi9DVR42pC21wVdDXmbVrMkFVNZ8qKwkXUpC95F2d3GUweV%2B5EVAWLshQ2iIrlh7RI1%2FUJAAD%2F%2F1yGbCyuAAAA; _ga_9E363E7BES=GS1.1.1662629864.10.1.1662630037.36.0.0; _ga=GA1.1.1177195770.1660461750; _ga_M29JC28873=GS1.1.1662629864.10.1.1662630037.36.0.0; tmr_detect=0%7C1662630040563; tmr_reqNum=124',
            "sec-ch-ua": '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
            "sec-ch-ua-mobile":"?0",
            "sec-ch-ua-platform":"Windows",
            "sec-fetch-dest": "document",
            "sec-fetch-mode": "navigate",
            "sec-fetch-site": "none",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "en-US,en;q=0.9,ru;q=0.8",
            "scheme":"https",
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "if-none-match": 'W/"106853-rf/iEIeU6urDGFXJzojxYcJkdlk"',
            "upgrade-insecure-requests": "1"}

#Задаем параметры хоста
host = "127.0.0.1"
user = "root"
password = ''
db_name = "ads"
table_existing = False