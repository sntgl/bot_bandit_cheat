from settings import *
import requests
import random
import time
random.seed()
rnd = str(random.randrange(1000000, 9999999))
requests.get(zap + 'messages.send?peer_id=-166948584&message=выход&random_id=' + rnd + vkt).json()['response']
rnd = str(random.randrange(1000000, 9999999))
requests.get(zap + 'messages.send?peer_id=-166948584&message=работа&random_id=' + rnd + vkt).json()['response']
rnd = str(random.randrange(1000000, 9999999))
requests.get(zap + 'messages.send?peer_id=-166948584&message=федерал&random_id=' + rnd + vkt).json()['response']
while True:
    try:
        time.sleep(2)
        r = requests.get(zap+'messages.getHistory?peer_id=-166948584&count=1'+vkt).json()
        text = r['response']['items'][0]['text']
        if id == r['response']['items'][0]['id']:
            if r['response']['items'][0]['from_id'] != -166948584:
                print('Бот перестал отвечать, жду его ответа.')
                r = requests.get(zap + 'messages.getHistory?peer_id=-166948584&count=1' + vkt).json()
                while r['response']['items'][0]['from_id'] != -166948584:
                    r = requests.get(zap + 'messages.getHistory?peer_id=-166948584&count=1' + vkt).json()
                    time.sleep(5)
                print('Бот ответил, продолжаю')
        else:
            id = r['response']['items'][0]['id']
            start = text.find('слово: ')+len('слово: ')
            end = text.find('.', start)
            print(text[start:end]+ ' = ', end = "")
            rnd = str(random.randrange(1000000, 9999999))
            r= requests.get('http://poiskslova.com/anagramma/?query='+text[start:end]).text
            start = r.find('">',r.find('<ul class="list_words">')+len('<ul class="list_words">'))+2
            end = r.find('</a>',start)
            if len(r[start:end])>20:
                print('не разгадано')
                frgt()
            print(r[start:end])
            id = requests.get(zap + 'messages.send?peer_id=-166948584&message='+r[start:end].lower()+'&random_id=' + rnd + vkt).json()['response']

    except:
        requests.get(
            zap + 'messages.send?peer_id=-166948584&message=пропустить&random_id=' + rnd + vkt)
    time.sleep(2)