import requests
from bs4 import BeautifulSoup
import asyncio




URL_ = 'https://uchet.kz/question/voprosy-truda/'
async def get_soup():
    soups = []
    for i in range(1, 6):
        url = f'https://uchet.kz/question/voprosy-truda/?PAGEN_1={i}'
        pag = await requests.get(url)
        soups.append(BeautifulSoup(pag.text, 'html.parser'))
    return soups

def get_all_urls(soups):
    question_urls = []
    for soup in soups:
        for link in soup.find_all('a', class_='font-weight-bold text-dark-75 text-hover-danger font-size-h5 mb-1'):
            question_urls.append(f"{URL_}/{link.get('href').split('/')[-2]}/")
    return question_urls

async def main():
    soups = await get_soup()
    urls = get_all_urls(soups)
    print(urls)

asyncio.run(main)
