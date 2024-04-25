import requests
from bs4 import BeautifulSoup
import csv



URL_ = 'https://uchet.kz/question/voprosy-truda/'
def get_soup():
    soups = []
    for i in range(1, 6):
        url = f'https://uchet.kz/question/voprosy-truda/?PAGEN_1={i}'
        pag = requests.get(url)
        soups.append(BeautifulSoup(pag.text, 'html.parser'))
    return soups

def get_all_urls(soups):
    question_urls = []
    for soup in soups:
        for link in soup.find_all('a', class_='font-weight-bold text-dark-75 text-hover-danger font-size-h5 mb-1'):
            question_urls.append(f"{URL_}/{link.get('href').split('/')[-2]}/")
    return question_urls

soups = get_soup()
urls = get_all_urls(soups)

print(len(urls))




# ?PAGEN_1=2
#
# soup = BeautifulSoup(page.text, 'html.parser')
# question_urls = []
# for link in soup.find_all('a', class_='font-weight-bold text-dark-75 text-hover-danger font-size-h5 mb-1'):
#     question_urls.append(f"{URL_}/{link.get('href').split('/')[-2]}/")

# question_url = []
# for i in range(len(all_questions)):
#     question_url.append(f"{URL}{all_questions[i].find('a', class_='font-weight-bold text-dark-75 text-hover-danger font-size-h5 mb-1')['href']}")
#
# for url in question_url:
#     response = requests.get(url)
#     soup = BeautifulSoup(response.text, 'html.parser')
#     question = soup.h1
#     print(question.text)
#
# # def get_text(text):
# #     texts = text.split('\n')
# #     anwer_question = list(filter(None, texts))
# #     question = anwer_question[0]
# #     answer = ''
# #     if len(anwer_question) > 1:
# #         answer = ' '.join(anwer_question[1:])
# #     return answer, question
# #
# #
# # questions = []
# # answers = []
# # for q in all_questions:
# #     t = q.text
# #     answer, question = get_text(t)
# #     questions.append(question)
# #     answers.append(answer)
# #
# # print(len(questions))
# # print(len(answers))

