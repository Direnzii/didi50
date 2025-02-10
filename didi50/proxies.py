import random
import requests


class Proxielist:
    def __init__(self):
        self.url_proxies_list = ('https://api.proxyscrape.com/v4/free-proxy-list/get?request=display_proxies&protocol'
                             '=http&proxy_format=protocolipport&format=text&timeout=20000')
        response = requests.get(url=self.url_proxies_list)
        response_proxies = response.content.split()
        self.proxies = []
        for p in response_proxies:
            self.proxies.append(f'{str(p).split("'")[1]}')
        random.shuffle(self.proxies)


proxie_list = Proxielist()
