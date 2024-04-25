import requests
import aiohttp
from bs4 import BeautifulSoup
import asyncio
import time
from threading import Thread



URL_ = 'https://uchet.kz/question/voprosy-truda/'


async def fetch_soup(session, url) -> BeautifulSoup:
    async with session.get(url) as response:
        return await response.text()


async def get_soup(page_count: int = 5) -> list:
    urls = [f'https://uchet.kz/question/voprosy-truda/?PAGEN_1={i}' for i in range(1, page_count + 1)]
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_soup(session, url) for url in urls]
        responses = await asyncio.gather(*tasks)

    return [BeautifulSoup(response, 'html.parser') for response in responses]


# async def get_element():
_question_urls = []
def get_all_urls(soup) -> None:
    global _question_urls
    for link in soup.find_all('a', class_='font-weight-bold text-dark-75 text-hover-danger font-size-h5 mb-1'):
        _question_urls.append(f"{URL_}/{link.get('href').split('/')[-2]}/")


def main(page_count: int = 5) -> list:
    """
    function for getting urls
    :param page_count: default 5
    :return: list of urls for getting questions and answers
    """
    loop = asyncio.get_event_loop()
    soups = loop.run_until_complete(get_soup(page_count))
    threads = [Thread(target=get_all_urls, args=(soup,)) for soup in soups]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    return _question_urls

if __name__ == '__main__':
    start_time = time.time()
    urls = main()
    end_time = time.time()
    print(end_time - start_time)


