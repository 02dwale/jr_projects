import time
import re

item_date = ["1 день назад",
"8 часов назад",
"10 часов назад",
"14 часов назад",
"2 дня назад",
"5 часов назад",
"10 часов назад",
"7 часов назад",
"3 дня назад",
"5 часов назад",
"9 часов назад",
"2 дня назад",
"4 дня назад",
"4 дня назад",
'14 октября']

#print(item_date[0])
#Функция принимает на вход относительную дату из объявления и возвращает значение float сутки с момента публикации

def dateintodays(date):
    result = re.findall(r'\d+', item)[0]
    #print(result)
    if re.search(r'часов|часа', date) is not None:
        result_hrs = int(result)
    elif re.search(r'дней|дня|день', date) is not None:
            result_hrs = int(result) * 24
    elif re.search(r'неделю|недели', date) is not None:
        result_hrs = int(result) * 7 * 24
    else:
        result_hrs = 30*24
    result_days = (result_hrs/24.)

    return result_days



now = time.localtime()


#Создать функцию, которая на вход берет текущее время, время объявления (в текстовом виде) и возвращает сколько объявление висит в сутках. Эта инфа идет в таблицу

#Применить машинное обучение для определения актуальности объявления. 