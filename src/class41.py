from bs4 import BeautifulSoup
from urllib import request

target = request.urlopen('https://www.weather.go.kr/w/index.do')

soup = BeautifulSoup(target, 'html.parser')
for location in soup.select('li'):
    print(location)
