import time as t
import csv
import datetime as dt
from datetime import datetime, date, time, timedelta
import requests

token = '713688ca2ea75604dccb04dab5f2b8bed0aba5196ff563b35b124c976f5f90dd6a997397405e021794aea'
q = 'Путин' #без знака # только одно слово.
v = 5.92

with open(q + '.csv', 'w', newline='', encoding='UTF-8') as csvfile:
    datawriter = csv.writer(csvfile, delimiter=';',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)

    datawriter.writerow(['date'] + ['owner_id'] + ['post_id'] + ['likes'] +
                        ['reposts'] + ['comments'] +

                        ['coordinates'] +
                        # не трогать, не работает.
                        # ['place_country']+['city']+['address']+['coordinates']+
                        # ['place_id']+['latitude']+['longitude']+
                        # ['created']+['updated']+['checkins']+

                        ['post_type'] +
                        ['platform'] + ['platform_type'])

i = 0
while True:

    if i == 0:
        b = datetime.now()  # текущее время

        end_time = int(t.mktime(b.timetuple())) #подставить unix-время если требуется сбор с определённого момента

        print('Цербер начал собирать посты с:', end_time, dt.datetime.fromtimestamp(  # функция преобразования
            int(end_time)
        ).strftime('%Y-%m-%d %H:%M:%S'))

        i = 1

    else:
        end_time = r[0]  # возвращает ВК крайнее время от которого нужно опускаться дальше

    r = requests.get('https://api.vk.com/method/execute.Shmakov_search_post?q=' + str(q)
                      + '&end_time=' + str(end_time)
                      + '&access_token=' + token + '&v=' + str(v)).json()['response']
    # print('крайнее время, должно совпадать', r[0])

    # print(len(r[1])) - сколько постов собрано за раз

    # print(time_start)

    for i in r[1]:

        date = i['date']  # дата поста

        owner_id = i['owner_id']  # создатель поста
        post_id = i['id']  # id поста

        likes = i['likes']['count']  # количество лайков
        reposts = i['reposts']['count']  # количество репостов
        comments = i['comments']['count']  # количество комментариев
        geo = i.setdefault('geo', None)

        if geo == None:
            coordinates = None
        else:
            '''
            place_id = i['geo']['place'].setdefault('id',None)
            latitude = geo['place'].setdefault('latitude',None) #широта места
            longitude = geo['place'].setdefault('longitude',None) #долгота места
            created= geo['place'].setdefault('created',None) # дата создания места
            updated= geo['place'].setdefault('updated',None) # дата обновления информации о месте
            checkins= geo['place'].setdefault('checkins',None) #количество чекинов в этом месте
            place_name = i['geo'].setdefault('title',None)
            country = i['geo'].setdefault('country',None)
            city = i['geo'].setdefault('city',None)
            address = i['geo'].setdefault('address',None)

            '''
            coordinates = geo.setdefault('coordinates', None)  # координаты пользователя

        post_type = i['post_type']

        platform = i['post_source'].setdefault('platform', 'direct')
        platform_type = i['post_source'].setdefault('type', None)
        platform_url = i['post_source'].setdefault('url', None)

        with open(str(q) + '.csv', 'a', newline='', encoding='UTF-8') as csvfile:
            datawriter = csv.writer(csvfile, delimiter=';',
                                    quotechar='|', quoting=csv.QUOTE_MINIMAL)

            datawriter.writerow([date] + [owner_id] + [post_id] + [likes] +
                                [reposts] + [comments] +

                                # [geo]+
                                [coordinates] +

                                # не трогать - не работает
                                # [country]+[city]+[address]+
                                # [place_id]+[latitude]+[longitude]+
                                # [created]+[updated]+[checkins]+

                                [post_type] +
                                [platform] + [platform_type])
    print('Цербер собрал посты до:', r[0], dt.datetime.fromtimestamp(  # функция преобразования
        int(r[0])
    ).strftime('%Y-%m-%d %H:%M:%S'))
    t.sleep(30)
