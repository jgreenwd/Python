import requests
import os
import re
from bs4 import BeautifulSoup
from string import punctuation

if __name__ == '__main__':
    num_pages = int(input())
    classifier = input()

    FAIL_MESSAGE = 'Failed Query: '
    BASE_URL = 'https://www.nature.com'
    HEADERS = {'Accept-Language': 'en-US,en;g=0.5'}
    START_PATH = os.getcwd()

    transtable = {x: '' for x in punctuation}
    transtable[' '] = '_'

    for p in range(num_pages):
        url = f'{BASE_URL}/nature/articles?searchType=journalSearch&sort=PubDate&page={p+1}'

        r = requests.get(url, headers=HEADERS)

        if r.ok:
            try:
                os.mkdir(f'{START_PATH}/Page_{p+1}')
                os.chdir(f'{START_PATH}/Page_{p+1}')
            except FileExistsError:
                print('Directory already exists')

            page = BeautifulSoup(r.content, 'html.parser')
            articles = page.find_all('article')

            for article in articles:
                article_type = article.find('span', attrs={'data-test': 'article.type'}).text.strip()

                if article_type == classifier:
                    anchor_tag = article.find('a', attrs={'data-track-action': 'view article'})
                    title = anchor_tag.text.translate(str.maketrans(transtable))
                    link = BASE_URL + anchor_tag.get('href')

                    page_sub = BeautifulSoup(requests.get(link, headers=HEADERS).content, 'html.parser')
                    body = page_sub.find('div', class_=re.compile('body')).text.strip()

                    file = open(title + '.txt', 'w', encoding='utf8')
                    file.write(body)
                    file.close()

            result = "success"

            os.chdir(START_PATH)

        else:
            result = FAIL_MESSAGE + str(r.status_code)

        print(result)
