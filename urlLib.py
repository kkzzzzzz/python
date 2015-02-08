#coding:utf-8
import urllib
from bs4 import BeautifulSoup
 
url = 'http://baike.baidu.com/search/word?word='
word = '唐嫣'
urlopen = urllib.urlopen(url + word)
soup = BeautifulSoup(urlopen)
tag = soup.find_all('sapn')

for eachTdSoup in tag:
    print eachTdSoup.text