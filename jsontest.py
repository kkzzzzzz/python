#coding:utf-8
import requests
from bs4 import BeautifulSoup
import lxml.html.soupparser as soupparser
 
url = 'http://baike.baidu.com/search/word'
params={'word' : '唐嫣'}
req = requests.get(url, params=params)
soup = BeautifulSoup(req.content)
tag = soup.find_all('sapn')


for eachTdSoup in tag:
    soupparser.fromstring(eachTdSoup.text)
    print eachTdSoup.text