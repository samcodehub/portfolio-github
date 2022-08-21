# pip install bs4
# pip install urllib3
# pip install plyer

from bs4 import BeautifulSoup
from urllib.request import urlopen
from plyer import notification
import time

url = 'https://news.google.com/news/rss'

client = urlopen(url)
xml_data = client.read()
client.close()

soup = BeautifulSoup(xml_data,'xml')
news_list = soup.find_all('item')
news_list = news_list[0:5]

for news in news_list:
    notification.notify(title="todays news",message=news.title.text+ '\npublish on :'+
    news.pubDate.text,timeout=20)
    time.sleep(1200)