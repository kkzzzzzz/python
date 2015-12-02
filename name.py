#coding:utf-8
import requests
from bs4 import BeautifulSoup
import lxml.html.soupparser as soupparser
 
url = 'http://my.dper.com/search/employee-profile'
params={'serialNumber' : '0011241',
        'ticket':'AAFSsPYAkNKN6Mb0Q6Li8D8gawrtLCUzOKul+5VCSnFSnVRno9C1I1s/'}
req = requests.get(url, params=params)
soup = BeautifulSoup(req.content)
print(soup)
tag = soup.find_all('sapn')


for eachTdSoup in tag:
    soupparser.fromstring(eachTdSoup.text)
    print eachTdSoup.text