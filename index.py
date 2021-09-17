import requests as reqs
from bs4 import BeautifulSoup as bs
import re
import csv

from requests.api import post

def get_pages_count(url):
    data = reqs.get(url)
    if data.status_code > 299 or data.status_code < 200:
        print('data status: {}'.format(data.status_code))
        return None
    bsObj = bs(data.content, 'html.parser')
    pages = bsObj.find('div', {'class': 'tm-pagination__pages'}).children
    elem = None
    for el in pages:
        elem = el
    lastPage = None
    for page in elem.children:
        pn = re.search(r'\d+', page.get_text(), flags=0)
        if pn != None:
            lastPage = pn.group()
    return lastPage

def get_articles(url):
    data = reqs.get(url)
    if data.status_code > 299 or data.status_code < 200:
        print('data status: {}'.format(data.status_code))
        return None
    bsObj = bs(data.content, 'html.parser')
    articles = bsObj.findAll('article', 'tm-articles-list__item')
    return articles

def parse_article(article):
    authorElem = article.find('a', {'class' : 'tm-user-info__username'})
    author = ''
    if authorElem != None:
        author = authorElem.get_text().split('\n')[1].strip()
    postLink = article.find('a', {'class' : 'tm-article-snippet__title-link'})
    link = ''
    title = ''
    if postLink != None:
        startUrl = 'https://habr.com/'
        href = postLink['href']
        link = startUrl+href
        title = postLink.get_text()
    short = ' '.join(article.find('div', {'class' : 'article-formatted-body'}).get_text().split('\n')).replace(u'\xa0', u' ')
    data = [author, title, link, short]
    return data

def write_to_csv(articlesData, outPath):
    with open(outPath, "w", newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=';')
        for line in articlesData:
            writer.writerow(line)


homePostsUrl = 'https://habr.com/ru/search/?q=WebAssembly&target_type=posts&order=relevance'
maxPage = get_pages_count(homePostsUrl)
pagesUrl = 'https://habr.com/ru/search/page{}/?q=WebAssembly&target_type=posts&order=relevance'
articlesData = [];
for page in range (1, int(maxPage) + 1):
    pageUrl = pagesUrl.format(str(page))
    articles = get_articles(pageUrl)
    if articles == None:
        continue
    for article in articles:
        data = parse_article(article)
        articlesData.append(data)

outPath = 'out.csv'
write_to_csv(articlesData, outPath)
