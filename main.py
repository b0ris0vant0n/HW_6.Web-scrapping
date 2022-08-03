import requests
import bs4

HEADERS = {'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Cookie' : 'habr_web_home_feed=/all/; hl=ru; fl=ru; _ym_uid=1659373240816635646; _ym_d=1659373240; _ga=GA1.2.1341563118.1659373240',
            'sec-ch-ua': '.Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': 'macOS',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'none',
            'Sec-Fetch-User': '?1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36}' }

KEYWORDS = ['дизайн', 'фото', 'web', 'python', 'linux']

response = requests.get('https://habr.com/ru/all/', headers=HEADERS)
text = response.text

soup = bs4.BeautifulSoup(text, features="html.parser")
articles = soup.find_all('div', class_="tm-article-snippet")
for article in articles:
    texts_preview = article.find_all(class_='tm-article-body tm-article-snippet__lead')
    for text_preview in texts_preview:
        text_words = text_preview.text.split(' ')
        if set(KEYWORDS) & set([word.lower() for word in text_words]):
            article_name = article.find('h2').find('a')
            href = article_name.attrs['href']
            url = 'https://habr.com' + href
            article_date = article.find('time')
            print(f'Дата: {article_date.text}, Статья: {article_name.text} ----> {url}')


print('---------Второе задание - поиск по всему тексту статьи----------')
soup = bs4.BeautifulSoup(text, features="html.parser")
articles = soup.find_all('div', class_="tm-article-snippet")
for article in articles:
    article_name = article.find('h2').find('a')
    href = article_name.attrs['href']
    url = 'https://habr.com' + href
    article_date = article.find('time')
    response2 = requests.get(url, headers=HEADERS)
    text2 = response2.text
    soup = bs4.BeautifulSoup(text2, features="html.parser")
    text_articles = soup.find(class_='tm-article-body')
    text_words = text_articles.text.split()
    if set(KEYWORDS) & set([word.lower() for word in text_words]):
        print(f'Дата: {article_date.text}, Статья: {article_name.text} ----> {url}')



