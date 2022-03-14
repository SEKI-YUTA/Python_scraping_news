from bs4 import BeautifulSoup
from urllib import request
import datetime

url = "https://www.yahoo.co.jp"
response = request.urlopen(url)
fetchedTime = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")
soup = BeautifulSoup(response, 'lxml')
pageTitle = soup.find('title').text
mainNewsBox = soup.find('div', class_="_2jjSS8r_I9Zd6O9NFJtDN-")
news = mainNewsBox.findAll('li')
for newsItem in news:
    print(newsItem.text)

with open('news.txt', 'a', encoding='shift_jis') as f:
    f.write('fetched time: {0}\n\n'.format(fetchedTime))
    for newsItem in news:
        f.write('{0}\n'.format(newsItem.text))
    f.write('--------- end ---------\n')


