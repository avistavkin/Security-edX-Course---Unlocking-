#версия1 - работает хорошо! Только надо установать requests -> pip install --upgrade requests


for i in range(10):

    import requests

    time= requests.get("http://google.com").elapsed.total_seconds()

    print ("google\t", time)

    time= requests.get("http://ya.ru").elapsed.total_seconds()

    print ("ya\t", time)


