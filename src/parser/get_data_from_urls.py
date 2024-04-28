import asyncio
import time
import csv
import datetime
from src.parser.concurrency_get_urls import main
from bs4 import BeautifulSoup
from aiohttp import ClientSession



URLS = main()

async def get_page(session: ClientSession, url: str) -> BeautifulSoup:
        async with session.get(url) as response:
            return await response.text()

async def main()-> list:
    async with ClientSession() as session:
        tasks = [get_page(session, url) for url in URLS]
        res = await asyncio.gather(*tasks)

        return [BeautifulSoup(response, 'html.parser') for response in res]


loop = asyncio.get_event_loop()
soups = loop.run_until_complete(main())
questions = list()
answers = list()

for soup in soups:
    questions.append(soup.h1.text)
    if len(soup.find('div', class_='card-body py-3').find_all('p')) >=  2:
        answers.append(soup.find('div', class_='card-body py-3').find_all('p')[1].getText(strip=True))
    else: answers.append(soup.find('div', class_='card-body py-3').find_all('p')[0].getText(strip=True))




def get_anwer_question():
    return answers, questions

# with open('../../answers.csv', 'w', newline='') as csvfile:
#     writer = csv.writer(csvfile)
#     writer.writerow("answer")
#     writer.writerows(answers)

