__author__ = 'Kevin'
#coding:utf-8
import requests
from bs4 import BeautifulSoup
import lxml.html.soupparser as soupparser

url = 'http://baike.baidu.com/search/word'
params={'word' : '唐嫣'}
req = requests.get(url, params=params)
soup = BeautifulSoup(req.content)
tag = soup.find_all('sapn')


cnt=len(tag)
i=0
while i<cnt:
    s=str(tag[i])
    left=s.find("taglist")
    right=s.find("<",1)
    wds=s[left+9:right]
    i=i+1